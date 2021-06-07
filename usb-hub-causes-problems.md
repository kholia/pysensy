With the IR Blaster is connected via a USB hub, it results in following
failures randomly.

```
$ python3 example.py
[!] Device has been reset
[+] Device version is 1
[+] State: Idle
[+] State: Idle
Traceback (most recent call last):
  File "example.py", line 417, in <module>
    main()
  File "example.py", line 411, in main
    transmit(command_endpoint, data_endpoint, response_endpoint, code=0xFF6897)
  File "example.py", line 327, in transmit
    configure_device(command_endpoint, response_endpoint, raw_data_length)
  File "example.py", line 253, in configure_device
    response = response_endpoint.read(length)
  File "/home/user/.local/lib/python3.8/site-packages/usb/core.py", line 423, in read
    return self.device.read(self, size_or_buffer, timeout)
  File "/home/user/.local/lib/python3.8/site-packages/usb/core.py", line 1019, in read
    ret = fn(
  File "/home/user/.local/lib/python3.8/site-packages/usb/backend/libusb1.py", line 864, in intr_read
    return self.__read(self.lib.libusb_interrupt_transfer,
  File "/home/user/.local/lib/python3.8/site-packages/usb/backend/libusb1.py", line 954, in __read
    _check(retval)
  File "/home/user/.local/lib/python3.8/site-packages/usb/backend/libusb1.py", line 604, in _check
    raise USBError(_strerror(ret), ret, _libusb_errno[ret])
usb.core.USBError: [Errno 5] Input/Output Error
```
