#!/usr/bin/env python3

# https://github.com/bschwind/ir-slinger/blob/master/pyslinger.py
#
# Python IR transmitter
# Requires pigpio library
# Supports NEC, RC-5 and raw IR.
# Danijel Tudek, Aug 2016

import sys

# Since both NEC and RC-5 protocols use the same method for generating waveform,
# it can be put in a separate class and called from both protocol's classes.
class Wave_generator():
    def __init__(self, protocol):
        self.protocol = protocol
        self.data = []

    # Pull the specified output pin low
    def zero(self, duration):
        self.data.append(duration)

    # Protocol-agnostic square wave generator
    def one(self, duration):
        self.data.append(duration)

# NEC protocol class
class NEC():
    def __init__(self,
                frequency=38000,
                leading_pulse_duration=9000,
                leading_gap_duration=4500,
                one_pulse_duration=562,
                # one_gap_duration=1686,
                one_gap_duration=1580,  # to match sensara stuff
                zero_pulse_duration=562,
                zero_gap_duration=562,
                trailing_pulse=0):
        self.wave_generator = Wave_generator(self)
        self.frequency = frequency # in Hz, 38000 per specification
        # Durations of high pulse and low "gap".
        # The NEC protocol defines pulse and gap lengths, but we can never expect
        # that any given TV will follow the protocol specification.
        self.leading_pulse_duration = leading_pulse_duration # in microseconds, 9000 per specification
        self.leading_gap_duration = leading_gap_duration # in microseconds, 4500 per specification
        self.one_pulse_duration = one_pulse_duration # in microseconds, 562 per specification
        self.one_gap_duration = one_gap_duration # in microseconds, 1686 per specification
        self.zero_pulse_duration = zero_pulse_duration # in microseconds, 562 per specification
        self.zero_gap_duration = zero_gap_duration # in microseconds, 562 per specification
        self.trailing_pulse = trailing_pulse # trailing 562 microseconds pulse, some remotes send it, some don't
        # print("NEC protocol initialized")

    # Send AGC burst before transmission
    def send_agc(self):
        # print("Sending AGC burst")
        self.wave_generator.one(self.leading_pulse_duration)
        self.wave_generator.zero(self.leading_gap_duration)

    # Trailing pulse is just a burst with the duration of standard pulse.
    def send_trailing_pulse(self):
        # print("Sending trailing pulse")
        self.wave_generator.one(self.one_pulse_duration)

    # This function is processing IR code. Leaves room for possible manipulation
    # of the code before processing it.
    def process_code(self, ircode):
        if (self.leading_pulse_duration > 0) or (self.leading_gap_duration > 0):
            self.send_agc()
        for i in ircode:
            if i == "0":
                self.zero()
            elif i == "1":
                self.one()
            else:
                print("ERROR! Non-binary digit!")
                assert False

        if self.trailing_pulse == 1:
            self.send_trailing_pulse()

        return self.wave_generator.data

    def zero(self):
        self.wave_generator.one(self.zero_pulse_duration)
        self.wave_generator.zero(self.zero_gap_duration)

    # One is represented by a pulse and a gap three times longer than the pulse
    def one(self):
        self.wave_generator.one(self.one_pulse_duration)
        self.wave_generator.zero(self.one_gap_duration)

# RC-5 protocol class
# Note: start bits are not implemented here due to inconsistency between manufacturers.
# Simply provide them with the rest of the IR code.
class RC5():
    def __init__(self,
                master,
                frequency=36000,
                duty_cycle=0.33,
                one_duration=889,
                zero_duration=889):
        self.master = master
        self.wave_generator = Wave_generator(self)
        self.frequency = frequency # in Hz, 36000 per specification
        self.duty_cycle = duty_cycle # duty cycle of high state pulse
        # Durations of high pulse and low "gap".
        # Technically, they both should be the same in the RC-5 protocol, but we can never expect
        # that any given TV will follow the protocol specification.
        self.one_duration = one_duration # in microseconds, 889 per specification
        self.zero_duration = zero_duration # in microseconds, 889 per specification
        print("RC-5 protocol initialized")

    # This function is processing IR code. Leaves room for possible manipulation
    # of the code before processing it.
    def process_code(self, ircode):
        for i in ircode:
            if i == "0":
                self.zero()
            elif i == "1":
                self.one()
            else:
                print("ERROR! Non-binary digit!")
                assert False
        return self.wave_generator.data

    # Generate zero or one in RC-5 protocol
    # Zero is represented by pulse-then-low signal
    def zero(self):
        self.wave_generator.one(self.zero_duration)
        self.wave_generator.zero(self.zero_duration)

    # One is represented by low-then-pulse signal
    def one(self):
        self.wave_generator.zero(self.one_duration)
        self.wave_generator.one(self.one_duration)

# RAW IR ones and zeroes. Specify length for one and zero and simply bitbang the GPIO.
# The default values are valid for one tested remote which didn't fit in NEC or RC-5 specifications.
# It can also be used in case you don't want to bother with deciphering raw bytes from IR receiver:
# i.e. instead of trying to figure out the protocol, simply define bit lengths and send them all here.
class RAW():
    def __init__(self,
                master,
                frequency=36000,
                duty_cycle=0.33,
                one_duration=520,
                zero_duration=520):
        self.master = master
        self.wave_generator = Wave_generator(self)
        self.frequency = frequency # in Hz
        self.duty_cycle = duty_cycle # duty cycle of high state pulse
        self.one_duration = one_duration # in microseconds
        self.zero_duration = zero_duration # in microseconds

    def process_code(self, ircode):
        for i in ircode:
            if i == "0":
                self.zero()
            elif i == "1":
                self.one()
            else:
                print("ERROR! Non-binary digit!")
                return 1
        return 0

    # Generate raw zero or one.
    # Zero is represented by low (no signal) for a specified duration.
    def zero(self):
        self.wave_generator.zero(self.zero_duration)

    # One is represented by pulse for a specified duration.
    def one(self):
        self.wave_generator.one(self.one_duration)


def translator(arr):
    for index, value in enumerate(arr):
        arr[index] = int(value * 0.038)  # 38 kHz

def nec_stuff(hex_code):
    nec = NEC(trailing_pulse=1)
    # nec = NEC()
    code = bin(hex_code).replace("0b", "")
    data = nec.process_code(code)
    translator(data)
    # print(data)
    # print(len(data))

    return data


if __name__ == "__main__":
    # nec_stuff(0xE0E058A7)
    # data = nec_stuff(0xE0E058A7)
    number = int(sys.argv[1], 16)
    data = nec_stuff(number)
    print(len(data), data)
