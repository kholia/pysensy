#!/usr/bin/env python3
#pylint: disable=line-too-long,anomalous-backslash-in-string

"""
Example driver for the Sensara IR Cable

Layout of the "Car MP3 remote":

References:

- http://www.geeetech.com/wiki/index.php/Arduino_IR_Remote_Control

- https://gist.github.com/steakknife/e419241095f1272ee60f5174f7759867

   ------------------
 /                    \
|  CH-    CH     CH+   |
| FFA25D FF629D FFE21D |
|                      |
|  |<<     >>|   |>||  |
| FF22DD FF02FD FFC23D |
|                      |
|   -       +     EQ   |
| FFE01F FFA857 FF906F |
|                      |
|   0      100+  200+  |
| FF6897 FF9867 FFB04F |
|                      |
|   1       2     3    |
| FF30CF FF18E7 FF7A85 |
|                      |
|   4       5     6    |
| FF10EF FF38C7 FF5AA5 |
|                      |
|   7       8     9    |
| FF42BD FF4AB5 FF52AD |
|                      |
|         Car          |
|         mp3          |
 \                    /
   ------------------
(FFFFFFFF for repeat when a button is held)

Specs for "Car MP3 remote":

- Remote control distance: more than 8 meters
- Launch tube infrared wavelength: 940Nm
- Crystal: the oscillation frequency of 455 KHz
- IR carrier frequency: 38KHz
- Encoding: the encoding format of the NEC, upd6122 encoding scheme, the user code 00FF, key coding below picture
- Size: 86 * 40 * 6mm
- Frequency: 38K
- Power supply: CR2025/160mAH

References:

- http://irdb.tk/codes/
- http://www.hifi-remote.com/infrared/IR-PWM.shtml
- https://github.com/bschwind/ir-slinger/blob/master/pyslinger.py
- http://www.harctoolbox.org/arduino_nano.html
- https://github.com/bengtmartensson/AGirs
- http://www.harctoolbox.org/arduino_nano.html#Use+in+IrScrutinizer
"""

import usb.core
import usb.util
import pyslinger

# Constants (from co.sensara.appsense_2020-07-28.apk)
BUFFER_FRAME_SIZE = 64
CODE_BAD_FREQUENCY = 4
CODE_BAD_SIZE = 6
CODE_ERROR = 255
CODE_ILLEGAL = 7
CODE_OK = 0
CODE_RESET = 250
CODE_START_UP = 1
CODE_SUCCESS = 3
CODE_TOO_BIG_SIGNAL = 5
CODE_UNDERFLOW = 254
OP_END_BUFFERING = 4
OP_GET_CONFIG = 1
OP_GET_DEVICE_VERSION = 127
OP_RESET = 120
OP_SET_CONFIG = 2
OP_START_BUFFERING = 3
RESULT_CODE_FAILURE = 255
RESULT_CODE_SUCCESS = 0
STATE_BUFFERING = 2
STATE_BUFFERING_EMITTING = 3
STATE_CONFIGURED = 1
STATE_EMITTING = 4
STATE_IDLE = 0

# Note
IS_USABLE = False
PACKET_SIZE = 64
BLOCK_SIZE = 64


def interface_matcher(interface):
    """
    Match interface properties for Sensara IR Cable.
    """
    if interface.bInterfaceClass == 0xff and interface.bInterfaceSubClass == 0xff \
            and interface.bInterfaceProtocol == 0xff and interface.bNumEndpoints == 4:
        return True

    return False


def find_device():
    """
    Detect Sensara IR Cable.
    """

    # find our device
    devs = usb.core.find(find_all=True)
    target_interface = None
    target_dev = None

    for dev in devs:
        if dev.iManufacturer != 0x1 :  # Hack (iManufacturer -> 0x1 -> Sensara Technologies)
            continue
        for configuration in dev.configurations():
            for interface in configuration.interfaces():
                if interface_matcher(interface):
                    target_interface = interface
                    target_dev = dev

    return target_dev, target_interface


def read_device_version(command_endpoint, response_endpoint):
    """
    Retrieve the Device API version

    Will throw an implicit exception in case of timeouts.
    """
    global IS_USABLE

    command = bytearray(1)
    command[0] = OP_GET_DEVICE_VERSION
    command_endpoint.write(command)
    response = response_endpoint.read(PACKET_SIZE)

    IS_USABLE = True
    marker, status, value = response[:3]
    if marker == OP_GET_DEVICE_VERSION and status == 0:
        return value

    print("Unable to read device version. Assuming Prototype version")
    return 0


def read_device_state(command_endpoint, response_endpoint):
    """
    Read device status
    """

    if not IS_USABLE:
        return False

    command = bytearray(1)
    command[0] = OP_GET_CONFIG
    command_endpoint.write(command)
    response = response_endpoint.read(PACKET_SIZE)

    marker, status, value, state = response[:4]

    if marker == OP_GET_CONFIG and status == 0 and value != 0:
        if state < 0 or state > 4:
            print("Unknown state reported")
        return state

    print("Device reported an error reading configuration")
    return False


def wait_for_state(command_endpoint, response_endpoint, desired_state, tries):
    """
    Wait for the device to be in the desired state
    """
    # private boolean waitForState(int i, int i2) {

    for _ in range(0, tries):
        state = read_device_state(command_endpoint, response_endpoint)
        if state == desired_state:
            return True

    return False


def get_state_name(i):
    """
    Map state code to a readable string
    """
    if i == STATE_IDLE:
        return "Idle"
    if i == STATE_CONFIGURED:
        return "Configured"
    if i == STATE_BUFFERING:
        return "Buffering"
    if i == STATE_BUFFERING_EMITTING:
        return "BufferringEmitting"
    if i == STATE_EMITTING:
        return "Emitting"

    return "Unknown?"


def get_code_name(i):
    """
    Map status code to a readable string
    """
    if i == CODE_OK:
        return "Code OK"
    if i == CODE_ERROR:
        return "Code Error"


    return "Unknown/Unimplemented?"


def uint16_to_bytes(value):
    """
    uinit16_t -> LSB, MSB
    """
    return (value & 0xff), ((value & 0xff00) >> 8)


def uint32_to_bytes(value):
    """
    uinit32_t -> LSB . . MSB
    """
    return (value & 0xff), ((value & 0xff00) >> 8), ((value & 0xff0000) >> 16), ((value & 0xff000000) >> 24)


def configure_device(command_endpoint, response_endpoint, length):
    """
    Configure the device (frequency + buffer size for IR data)
    """
    command = bytearray(5)
    command[0] = OP_SET_CONFIG
    # writeUInt16(allocate, i)
    # writeUInt16(allocate, i2)
    frequency = 38000  # NEC 38 kHz
    command[1], command[2] = uint16_to_bytes(frequency)
    command[3], command[4] = uint16_to_bytes(length)
    command_endpoint.write(command)
    response = response_endpoint.read(length)

    marker, status = response[:2]
    if marker == OP_SET_CONFIG and status == 0:
        print("[+] Device configured OK")
        return wait_for_state(command_endpoint, response_endpoint, STATE_CONFIGURED, 10)

    return False


def start_buffering(command_endpoint, response_endpoint):
    """
    Start buffering IR data
    """
    command = bytearray(1)
    command[0] = OP_START_BUFFERING
    command_endpoint.write(command)
    response = response_endpoint.read(PACKET_SIZE)

    marker, status = response[:2]
    if marker == OP_START_BUFFERING and status == 0:
        print("[+] Started buffering OK")
        return wait_for_state(command_endpoint, response_endpoint, STATE_BUFFERING, 10)

    print("Start buffering failed")
    return False


def end_buffering(command_endpoint, response_endpoint):
    """
    End buffering IR data
    """
    command = bytearray(1)
    command[0] = OP_END_BUFFERING
    command_endpoint.write(command)
    response = response_endpoint.read(PACKET_SIZE)

    marker, status, value = response[:3]
    if marker == OP_END_BUFFERING and status == 0:
        print("[+] Ended buffering OK")
        return value

    print("End buffering failed with an error (%s)" % get_code_name(status))
    return False


def send_data(data_endpoint, data):
    """
    Send IR data - yay!
    """
    for i in range(0, len(data), 64):
        block = data[i:i+64]
        # print(block)
        data_endpoint.write(block)

    data_endpoint.clear_halt()


def transmit(command_endpoint, data_endpoint, response_endpoint, code=0xE0E058A7):
    """
    High-level transmit code
    """
    data_endpoint.clear_halt()

    # nec stuff
    data = pyslinger.nec_stuff(code)  # 32-bit code
    raw_data_length = len(data) * 4  # uint32 -> 4 bytes
    rdata = bytearray(raw_data_length)
    idx = 0
    for _, value in enumerate(data):
        rdata[idx:idx+4] = uint32_to_bytes(value)
        idx = idx + 4

    # configure device
    configure_device(command_endpoint, response_endpoint, raw_data_length)

    start_buffering(command_endpoint, response_endpoint)
    state = read_device_state(command_endpoint, response_endpoint)
    print("[+] State: %s" % get_state_name(state))

    # transmit stuff
    send_data(data_endpoint, rdata)

    end_buffering(command_endpoint, response_endpoint)
    state = read_device_state(command_endpoint, response_endpoint)
    print("[+] State: %s" % get_state_name(state))

    ret = wait_for_state(command_endpoint, response_endpoint, STATE_IDLE, 1000)
    assert ret

    state = read_device_state(command_endpoint, response_endpoint)
    print("[+] State: %s" % get_state_name(state))


def reset_device(command_endpoint, response_endpoint):
    """
    Reset the Sensara IR Cable
    """

    command = bytearray(1)
    command[0] = OP_RESET
    command_endpoint.write(command)
    response = response_endpoint.read(PACKET_SIZE)

    marker, status = response[:2]
    if marker == OP_RESET and status == 0:
        print("[!] Device has been reset")
        return wait_for_state(command_endpoint, response_endpoint, STATE_IDLE, 10)

    print("Unable to reset the device")
    return False


def main():
    """
    Driver code
    """

    # was it found?
    dev, interface = find_device()
    if dev is None:
        raise ValueError('Device not found')
    dev.reset()  # note!

    # print(dev)

    for endpoint in interface.endpoints():
        if usb.util.endpoint_direction(endpoint.bEndpointAddress) == usb.util.ENDPOINT_IN and endpoint.bmAttributes == 0x3:
            response_endpoint = endpoint
        if usb.util.endpoint_direction(endpoint.bEndpointAddress) == usb.util.ENDPOINT_OUT and endpoint.bmAttributes == 0x3:
            command_endpoint = endpoint
        if usb.util.endpoint_direction(endpoint.bEndpointAddress) == usb.util.ENDPOINT_OUT and endpoint.bmAttributes == 0x2:
            data_endpoint = endpoint

    ret = reset_device(command_endpoint, response_endpoint)
    assert ret

    # Debug code
    # print(response_endpoint)
    # print(command_endpoint)
    # print(data_endpoint)

    try:
        version = read_device_version(command_endpoint, response_endpoint)
        if version != 0:
            print("[+] Device version is %s" % version)

        state = read_device_state(command_endpoint, response_endpoint)
        print("[+] State: %s" % get_state_name(state))

        data_endpoint.clear_halt()

        state = read_device_state(command_endpoint, response_endpoint)
        print("[+] State: %s" % get_state_name(state))

        # transmit stuff
        transmit(command_endpoint, data_endpoint, response_endpoint, code=0xFF6897)

    finally:
        pass

if __name__ == "__main__":
    main()
