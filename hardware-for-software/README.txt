Firmware was generated using https://github.com/NordicSemiconductor/pc-nrfutil.

https://github.com/DigitalSecurity/nrf5x-tools/ ;)

...

$ adb logcat | grep `adb shell ps | grep co.sensara.appsense | cut -c10-15`
...
10-20 19:57:23.694 17036 17036 I IRManager: DB_IR: Checking IR Device
10-20 19:57:23.694 17036 17036 D Remote_Test: Checking IR Device
10-20 19:57:23.694 17036 17036 D Remote_Test: Disconnect BLE REMOTE
10-20 19:57:23.695 17036 17036 I BLEScanner: Starting BLE Scan
10-20 19:57:23.695 17036 17036 D BluetoothAdapter: isLeEnabled(): ON
10-20 19:57:23.698  2060  2697 V bt_stack: [VERBOSE1:bta_gattc_act.cc(175)] bta_gattc_register: state:2
10-20 19:57:23.699 17036 23226 D BluetoothLeScanner: onScannerRegistered() - status=0 scannerId=6 mScannerId=0
10-20 19:57:23.713 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:23.806 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:23.850 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:23.892 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:23.934 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:23.974 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.009 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.014 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.058 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.101 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.145 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.192 17036 17036 I SensyHomeFragment: T1: Found devices: 0
10-20 19:57:24.717   747  2702 I vendor.qti.bluetooth@1.0-ibs_handler: DeviceSleep: TX Awake, Sending SLEEP_IND
10-20 19:57:24.717   747  2702 D vendor.qti.bluetooth@1.0-ibs_handler: SerialClockVote: vote for UART CLK OFF
10-20 19:57:33.695 17036 17036 I MainActivity: ENABLE BLE STOPPED
10-20 19:57:33.696 17036 17036 D BluetoothAdapter: isLeEnabled(): ON

After `v1` hack:


```
10-20 20:37:23.719 17060 24013 D BluetoothGatt: onClientConnectionState() - status=0 clientIf=6 device=24:6F:28:B1:03:4A
10-20 20:37:23.719 17060 24013 I BLEConnection: Connected device: 24:6F:28:B1:03:4A
10-20 20:37:23.719 17060 24013 I BLEConnection: Refreshing GATT.
10-20 20:37:23.720 17060 24013 D BluetoothGatt: refresh() - device: 24:6F:28:B1:03:4A
10-20 20:37:23.720 17060 24013 D BluetoothGatt: onClientConnectionState() - status=0 clientIf=6 device=24:6F:28:B1:03:4A
10-20 20:37:23.720 17060 24013 I BLEConnection: Connected device: 24:6F:28:B1:03:4A
10-20 20:37:23.721 17060 24013 I BLEConnection: Starting GATT Discovery
10-20 20:37:23.721 17060 24013 D BluetoothGatt: discoverServices() - device: 24:6F:28:B1:03:4A
10-20 20:37:23.731  2060  2697 I bt_stack: [INFO:gatt_main.cc(919)] gatt_data_process op_code = 17, msg_len = 13
10-20 20:37:23.731  2060  2697 V bt_stack: [VERBOSE1:gatt_cl.cc(1100)] gatt_client_handle_server_rsp op_code: 17, len = 13rsp_code: 17
10-20 20:37:23.746  2060  2697 I bt_stack: [INFO:gatt_main.cc(919)] gatt_data_process op_code = 17, msg_len = 21
10-20 20:37:23.746  2060  2697 V bt_stack: [VERBOSE1:gatt_cl.cc(1100)] gatt_client_handle_server_rsp op_code: 17, len = 21rsp_code: 17

10-20 20:37:23.761  2060  2697 I bt_stack: [INFO:gatt_main.cc(919)] gatt_data_process op_code = 17, msg_len = 21
10-20 20:37:23.761  2060  2697 V bt_stack: [VERBOSE1:gatt_cl.cc(1100)] gatt_client_handle_server_rsp op_code: 17, len = 21rsp_code: 17
10-20 20:37:23.836 17060 24013 D BluetoothGatt: onConnectionUpdated() - Device=24:6F:28:B1:03:4A interval=36 latency=0 timeout=500 status=0
10-20 20:37:24.220 17060 17060 I BLEConnection: Starting GATT Discovery
10-20 20:37:24.220 17060 17060 D BluetoothGatt: discoverServices() - device: 24:6F:28:B1:03:4A
10-20 20:37:24.376 17060 24013 D BluetoothGatt: onConnectionUpdated() - Device=24:6F:28:B1:03:4A interval=6 latency=0 timeout=500 status=0
10-20 20:37:24.513 17060 24013 D BluetoothGatt: onSearchComplete() = Device=24:6F:28:B1:03:4A Status=0
10-20 20:37:24.514 17060 24013 I BLEConnection: Discovering Characteristics: 24:6F:28:B1:03:4A
10-20 20:37:24.514 17060 24013 I BLEConnection: Unable to find characteristic and service on device: 24:6F:28:B1:03:4A
10-20 20:37:24.514 17060 24013 I BLEConnection: GATT Discovery Timed out. Retrying connection.
10-20 20:37:24.514 17060 24013 D BluetoothGatt: close()
10-20 20:37:24.514 17060 24013 D BluetoothGatt: unregisterApp() - mClientIf=6
10-20 20:37:24.516 17060 24013 I BLEConnection: Initiating connection.
10-20 20:37:24.516 17060 24013 D BluetoothGatt: connect() - device: 24:6F:28:B1:03:4A, auto: false
10-20 20:37:24.516 17060 24013 D BluetoothGatt: registerApp()
10-20 20:37:24.516 17060 24013 D BluetoothGatt: registerApp() - UUID=cdc9ef0c-fdbe-4a9c-9cc1-611afe1abb7d
10-20 20:37:24.518  2060  2697 V bt_stack: [VERBOSE1:bta_gattc_act.cc(175)] bta_gattc_register: state:2
10-20 20:37:24.519 17060 24013 D BluetoothGatt: onClientRegistered() - status=0 clientIf=6
10-20 20:37:24.522 17060 24013 D BluetoothGatt: onClientConnectionState() - status=0 clientIf=6 device=24:6F:28:B1:03:4A
10-20 20:37:24.522 17060 24013 I BLEConnection: Connected device: 24:6F:28:B1:03:4A
10-20 20:37:24.522 17060 24013 I BLEConnection: Refreshing GATT.
10-20 20:37:24.522 17060 24013 D BluetoothGatt: refresh() - device: 24:6F:28:B1:03:4A
10-20 20:37:24.522 17060 24013 D BluetoothGatt: onClientConnectionState() - status=0 clientIf=6 device=24:6F:28:B1:03:4A
10-20 20:37:24.523 17060 24013 I BLEConnection: Connected device: 24:6F:28:B1:03:4A
10-20 20:37:24.523 17060 24013 I BLEConnection: Starting GATT Discovery
10-20 20:37:24.523 17060 24013 D BluetoothGatt: discoverServices() - device: 24:6F:28:B1:03:4A
```

Logs:

```
$ adb logcat | grep `adb shell ps | grep co.sensara.appsense | cut -c15-18`

10-25 17:34:59.818  2023  2023 I SensyHomeFragment: T1: Found devices: 1
10-25 17:34:59.818  2023  2023 I SensyHomeFragment: T1: Allowing : 24:6F:28:B1:03:4A Sensy Remote
10-25 17:35:00.371  2023  2023 I MainActivity: ENABLE BLE STOPPED
10-25 17:35:00.372  2023  2023 D BluetoothAdapter: isLeEnabled(): ON
10-25 17:35:00.374  2023  2023 I BLEScanner: Connecting to device: 24:6F:28:B1:03:4A
10-25 17:35:00.375  2023  2023 D BluetoothAdapter: isLeEnabled(): ON
10-25 17:35:00.375  2023  2023 D BluetoothLeScanner: could not find callback wrapper
10-25 17:35:00.375  2023  2023 I TVRemoteFragment: ROX Updating TV Remote Overlay
10-25 17:35:00.375  2023  2023 I ACRemoteFragment: ROX Updating AC Remote Fragment
10-25 17:35:00.377  2023  2023 I BLEConnection: Initiating connection.
10-25 17:35:00.377  2023  2023 D BluetoothGatt: connect() - device: 24:6F:28:B1:03:4A, auto: false
10-25 17:35:00.377  2023  2023 D BluetoothGatt: registerApp()
10-25 17:35:00.378  2023  2023 D BluetoothGatt: registerApp() - UUID=863e6088-9080-4439-8fa2-c5cef6c5953a
10-25 17:35:00.379  2023  2023 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 17:35:00.380  2023 15759 D BluetoothGatt: onClientRegistered() - status=0 clientIf=5
10-25 17:35:00.386  2023  2023 I MainActivity: In TV Provider Changed
10-25 17:35:00.387  2023  2023 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 17:35:00.387  2023  2023 I TVRemoteFragment: ROX Updating TV Remote Overlay
10-25 17:35:00.387  2023  2023 I ACRemoteFragment: ROX Updating AC Remote Fragment
10-25 17:35:00.713  2023 15759 D BluetoothGatt: onClientConnectionState() - status=0 clientIf=5 device=24:6F:28:B1:03:4A
10-25 17:35:00.713  2023 15759 I BLEConnection: Connected device: 24:6F:28:B1:03:4A
10-25 17:35:00.713  2023 15759 I BLEConnection: Starting GATT Discovery
10-25 17:35:00.713  2023 15759 D BluetoothGatt: discoverServices() - device: 24:6F:28:B1:03:4A
10-25 17:35:01.243  2023 15759 D BluetoothGatt: onConnectionUpdated() - Device=24:6F:28:B1:03:4A interval=6 latency=0 timeout=500 status=0
10-25 17:35:01.484  2023 15759 D BluetoothGatt: onSearchComplete() = Device=24:6F:28:B1:03:4A Status=0
10-25 17:35:01.485  2023 15759 I BLEConnection: Discovering Characteristics: 24:6F:28:B1:03:4A
10-25 17:35:01.485  2023 15759 I BLEConnection: Unable to find characteristic and service on device: 24:6F:28:B1:03:4A
...

447999 ms  <= "Connected device: 24:6F:28:B1:03:4A"

```
447999 ms  StringBuilder.toString()
447999 ms  <= "discoverServices() - device: 24:6F:28:B1:03:4A"
448023 ms  StringBuilder.toString()
448024 ms  <= "onConnectionUpdated() - Device=24:6F:28:B1:03:4A interval=6 latency=0 timeout=500 status=35"
448114 ms  StringBuilder.toString()
448114 ms  <= "onConnectionUpdated() - Device=24:6F:28:B1:03:4A interval=6 latency=0 timeout=500 status=0"
448325 ms  ParcelUuid.getUuid()
448326 ms  <= "<instance: java.util.UUID>"
448327 ms  StringBuilder.toString()
448327 ms  <= "00002902-0000-1000-8000-00805f9b34fb"
448326 ms  00002902-0000-1000-8000-00805f9b34fb
448328 ms  StringBuilder.toString()
448328 ms  <= "onSearchComplete() = Device=24:6F:28:B1:03:4A Status=0"
448328 ms  StringBuilder.toString()
448329 ms  <= "Discovering Characteristics: 24:6F:28:B1:03:4A"
448329 ms  StringBuilder.toString()
```

```
$ frida-trace -U -n co.sensara.appsense -j '*!*scanF*/su' -j '*!*getUu*/' -j '*StringB*!*toString*/'
```

After `v2`:

```
$ adb logcat | grep `adb shell ps | grep co.sensara.appsense | cut -c15-18`
10-25 18:31:20.222  1659  1782 I ActivityManager: Start proc 2030:co.sensara.appsense/u0a207 for pre-top-activity {co.sensara.appsense/co.sensara.appsense.SplashActivity}
10-25 19:08:56.625  2030  2030 I RemoteManager: Restoring remotes from user account
10-25 19:08:56.625  2030  2030 I RemoteManager: Account.TVProvider value: null
10-25 19:08:56.626  2030  2030 I RemoteManager: DB0: selectedAC: null and Application.acSubremoteID = null
10-25 19:08:56.627  2030  2030 I BLEConnection: New Persist state: true
10-25 19:08:56.627  2030  2030 I IRManager: DB_IR: Checking IR Device
10-25 19:08:56.627  2030  2030 D Remote_Test: Checking IR Device
10-25 19:08:56.627  2030  2030 D Remote_Test: BLE REMOTE Usable true
10-25 19:08:56.627  2030  2030 I Application: Firing onActivityShown
10-25 19:08:56.633  2030  2030 I Account : Login ID: 62895523
10-25 19:08:56.638  2030  2030 I MainActivity: In TV Provider Changed
10-25 19:08:56.638  2030  2030 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 19:08:56.638  2030  2030 I TVRemoteFragment: ROX Updating TV Remote Overlay
10-25 19:08:56.638  2030  2030 I ACRemoteFragment: ROX Updating AC Remote Fragment
10-25 19:08:56.643  2030 20387 I IRManager: DB_IR: Checking IR Device
10-25 19:08:56.643  2030 20387 D Remote_Test: Checking IR Device
10-25 19:08:56.643  2030 20387 D Remote_Test: BLE REMOTE Usable true
10-25 19:08:56.643  2030 20387 I IRManager: Wifi Is Enabled. Starting Scan
10-25 19:08:56.643  2030 20387 I WifiScanner: WiFi: In startScan with forceScan as: false
10-25 19:08:56.644  2030 20387 I WifiScanner: WiFi: Setting isScanning to True
10-25 19:08:56.644  2030 20387 I WifiScanner: WiFi: Scanning for 10s
```

Nothing extra was needed to make `Remote_Test: BLE REMOTE Usable true`.

```
10-25 19:22:37.942  2030  2030 D Remote_Test: BLE REMOTE Usable true
10-25 19:22:37.943  2030  2030 I TVRemoteFragment: ROX Updating TV Remote Overlay
10-25 19:22:37.943  2030  2030 I ACRemoteFragment: ROX Updating AC Remote Fragment
10-25 19:22:37.946  2030  2030 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 19:22:37.956  2030  2030 I MainActivity: In TV Provider Changed
10-25 19:22:37.956  2030  2030 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 19:22:37.957  2030  2030 I TVRemoteFragment: ROX Updating TV Remote Overlay
10-25 19:22:37.957  2030  2030 I ACRemoteFragment: ROX Updating AC Remote Fragment
10-25 19:22:37.963  2030  2030 I BLEConnection: Reading supported Protocols
10-25 19:22:37.982  2030 19228 I BLEConnection: Supported Custom Protocol: 1214606444
10-25 19:22:37.982  2030 19228 I BLEConnection: Supported Custom Protocol: 1864390511
10-25 19:22:37.982  2030 19228 I BLEConnection: Supported Custom Protocol: 1919706144
10-25 19:22:37.982  2030 19228 I BLEConnection: Supported Custom Protocol: 1935767923
10-25 19:22:37.982  2030 19228 I BLEConnection: Supported Custom Protocol: 542008681
10-25 19:22:37.983  2030 19228 W BluetoothGatt: Unhandled exception in callback
10-25 19:22:37.983  2030 19228 W BluetoothGatt: java.nio.BufferUnderflowException
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at java.nio.Buffer.nextGetIndex(Buffer.java:521)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at java.nio.HeapByteBuffer.getInt(HeapByteBuffer.java:319)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at co.sensara.sensy.infrared.bluetooth.BLEConnection.parseSupportedProtocols(BLEConnection.java:817)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at co.sensara.sensy.infrared.bluetooth.BLEConnection.access$1000(BLEConnection.java:40)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at co.sensara.sensy.infrared.bluetooth.BLEConnection$SupportedProtocolReadOperation.onCharacteristicRead(BLEConnection.java:970)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at co.sensara.sensy.infrared.bluetooth.BLEConnection.onCharacteristicRead(BLEConnection.java:769)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.bluetooth.BluetoothGatt$1$6.run(BluetoothGatt.java:394)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.bluetooth.BluetoothGatt.runOrQueueCallback(BluetoothGatt.java:780)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.bluetooth.BluetoothGatt.access$200(BluetoothGatt.java:41)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.bluetooth.BluetoothGatt$1.onCharacteristicRead(BluetoothGatt.java:388)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.bluetooth.IBluetoothGattCallback$Stub.onTransact(IBluetoothGattCallback.java:246)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.os.Binder.execTransactInternal(Binder.java:1021)
10-25 19:22:37.983  2030 19228 W BluetoothGatt: 	at android.os.Binder.execTransact(Binder.java:994)
10-25 19:22:38.038  2030 19228 D BluetoothGatt: onConnectionUpdated() - Device=24:6F:28:B1:03:4A interval=36 latency=0 timeout=500 status=0
```

We need to implement this part (i.e. "supported protocols") now.


After `v3`: Add `Samsung TV` and press a key on the on-screen remote.

```
10-25 19:51:17.765  2030  2030 I RemoteControl: Sequencer: 52Will emit: key: 6 32 e0e058a7; device: e0e00000
10-25 19:51:17.765  2030  2030 I RemoteControl: Final sleep: 241; Gap: 400; Used: 159
10-25 19:51:17.765  2030  2030 I BLEConnection: Writing Characteristic: 24:6F:28:B1:03:4A
10-25 19:51:17.767  2030  2030 I Analytics: AX2 sendEvent 1
10-25 19:51:17.767  2030  2030 I Analytics: AX2 sendEvent 1
10-25 19:51:17.841  2030  2030 I BLEConnection: Writing Characteristic: 24:6F:28:B1:03:4A
10-25 19:51:24.303  2030  2030 I WifiScanner: WiFi: Inside stopScan
10-25 19:51:24.303  2030  2030 I WifiScanner: WiFi: Setting isScanning to False
10-25 19:51:24.303  2030  2030 I WifiScanner: WiFi: Stopped Scan. Here are the devices found:
10-25 19:51:24.303  2030  2030 I WifiScanner: WiFi: Sending it to Sensy Home Fragment.. I guess. Posting Event
10-25 19:51:24.303  2030  2030 I MainActivity: WiFi Devices Found Event Triggered
10-25 19:51:24.305  2030 19200 I WifiScanner: WiFi: Stopped Wifi Discovery
10-25 19:51:48.098  2030  2030 I Application: Firing onActivityHidden
10-25 19:52:04.321  2030  2030 I BLEConnection: New Persist state: false
10-25 19:52:04.322  2030  2030 I BLEConnection: Fast Restart.
10-25 19:52:04.322  2030  2030 I BLEConnection: Writing Characteristic: 24:6F:28:B1:03:4A
10-25 19:52:04.323  2030  2030 I IRManager: DB_IR: Checking IR Device
10-25 19:52:04.323  2030  2030 D Remote_Test: Checking IR Device
10-25 19:52:04.323  2030  2030 D Remote_Test: BLE REMOTE Usable true
10-25 19:52:04.326  2030  2030 I RemoteManager: Changing TV Configuration - Provider: null, TV Manufacturer: 3, Selected Remote: null, Referrer: RemoteManager
10-25 19:52:04.326  2030  2030 I RemoteManager: Operator Selection: Change TV Configuration called with provider: Null
10-25 19:52:04.326  2030  2030 I RemoteManager: Operator Selection: Trying to getTelevision with Provider: Null
10-25 19:52:04.326  2030  2030 I Backend : Operator Selection: Building Result with provider: null
10-25 19:52:04.425  2030  2030 I MainActivity: In TV Provider Changed
10-25 19:52:04.425  2030  2030 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 19:52:04.427  2030  2030 I TVRemoteFragment: ROX Updating TV Remote Overlay
10-25 19:52:04.427  2030  2030 I ACRemoteFragment: ROX Updating AC Remote Fragment
10-25 19:52:04.429  2030  2030 D BluetoothGatt: cancelOpen() - device: 24:6F:28:B1:03:4A
10-25 19:52:04.431  2030 19100 D BluetoothGatt: onClientConnectionState() - status=0 clientIf=10 device=24:6F:28:B1:03:4A
10-25 19:52:04.431  2030 19100 I BLEConnection: Finished output on: 24:6F:28:B1:03:4A
10-25 19:52:04.431  2030 19100 D BluetoothGatt: close()
10-25 19:52:04.431  2030 19100 D BluetoothGatt: unregisterApp() - mClientIf=10
10-25 19:52:04.431  2030  2030 I RemoteUtils: Remote: Current remote ID is null
10-25 19:52:04.435  2030 19147 I LCNStore: Using Offline remote control data for remotes: 52, 92
10-25 19:52:04.443  2030  2030 I MainActivity: In TV Provider Changed
10-25 19:52:04.443  2030  2030 I RemoteOverlayFragment: ROX Updaing Remote Overlay
10-25 19:52:04.445  2030  2030 I TVRemoteFragment: ROX Updating TV Remote Overlay
```


```
$ frida-trace -U -n co.sensara.appsense -j '*!*writeCha*/'
 60899 ms  BluetoothGatt.writeCharacteristic("<instance: android.bluetooth.BluetoothGattCharacteristic>")
 60900 ms     | IBluetoothGatt$Stub$Proxy.writeCharacteristic(9, "24:6F:28:B1:03:4A", 61, 2, 0, [6,32,0,0,0,0,-32,-32,88,-89,0,0,0,0,0,0,0,0,0,0])
 60901 ms  <= true
 60969 ms  BluetoothGatt.writeCharacteristic("<instance: android.bluetooth.BluetoothGattCharacteristic>")
 60969 ms     | IBluetoothGatt$Stub$Proxy.writeCharacteristic(9, "24:6F:28:B1:03:4A", 61, 2, 0, [-1,0,0,1,85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
 60971 ms  <= true
```

```
Started tracing 80 functions. Press Ctrl+C to stop.
           /* TID 0x3ddd */
  4073 ms  Sequencer.parseCode("0xe0e08679")
  4073 ms  <= "3772810873"
  4074 ms  NEC_SHORT.encode("3772810873", 32)
  4075 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4075 ms  Sequencer.parseCode("0xe0e06897")
  4075 ms  <= "3772803223"
  4075 ms  NEC_SHORT.encode("3772803223", 32)
  4075 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4076 ms  Sequencer.parseCode("0xe0e0f807")
  4076 ms  <= "3772839943"
  4076 ms  NEC_SHORT.encode("3772839943", 32)
  4076 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4076 ms  Sequencer.parseCode("0xe0e0e01f")
  4076 ms  <= "3772833823"
  4076 ms  NEC_SHORT.encode("3772833823", 32)
  4076 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4076 ms  Sequencer.parseCode("0xe0e046b9")
  4076 ms  <= "3772794553"
  4076 ms  NEC_SHORT.encode("3772794553", 32)
  4077 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4077 ms  Sequencer.parseCode("0xe0e006f9")
  4077 ms  <= "3772778233"
  4077 ms  NEC_SHORT.encode("3772778233", 32)
  4077 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4077 ms  Sequencer.parseCode("0xe0e016e9")
  4077 ms  <= "3772782313"
  4077 ms  NEC_SHORT.encode("3772782313", 32)
  4077 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4077 ms  Sequencer.parseCode("0xe0e0a659")
  4077 ms  <= "3772819033"
  4078 ms  NEC_SHORT.encode("3772819033", 32)
  4078 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4078 ms  Sequencer.parseCode("0xe0e031ce")
  4078 ms  <= "3772789198"
  4078 ms  NEC_SHORT.encode("3772789198", 32)
  4078 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4078 ms  Sequencer.parseCode("0xe0e048b7")
  4078 ms  <= "3772795063"
  4078 ms  NEC_SHORT.encode("3772795063", 32)
  4079 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4079 ms  Sequencer.parseCode("0xe0e040bf")
  4079 ms  <= "3772793023"
  4079 ms  NEC_SHORT.encode("3772793023", 32)
  4079 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4079 ms  Sequencer.parseCode("0xe0e0d02f")
  4079 ms  <= "3772829743"
  4079 ms  NEC_SHORT.encode("3772829743", 32)
  4079 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4079 ms  Sequencer.parseCode("0xe0e028d7")
  4079 ms  <= "3772786903"
  4079 ms  NEC_SHORT.encode("3772786903", 32)
  4080 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4080 ms  Sequencer.parseCode("0xe0e0f00f")
  4080 ms  <= "3772837903"
  4080 ms  NEC_SHORT.encode("3772837903", 32)
  4080 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4080 ms  Sequencer.parseCode("0xe0e016e9")
  4080 ms  <= "3772782313"
  4080 ms  NEC_SHORT.encode("3772782313", 32)
  4080 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4080 ms  Sequencer.parseCode("0xe0e08877")
  4080 ms  <= "3772811383"
  4080 ms  NEC_SHORT.encode("3772811383", 32)
  4081 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4081 ms  Sequencer.parseCode("0xe0e036c9")
  4081 ms  <= "3772790473"
  4081 ms  NEC_SHORT.encode("3772790473", 32)
  4081 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4081 ms  Sequencer.parseCode("0xe0e020df")
  4081 ms  <= "3772784863"
  4081 ms  NEC_SHORT.encode("3772784863", 32)
  4081 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4081 ms  Sequencer.parseCode("0xe0e0a05f")
  4082 ms  <= "3772817503"
  4082 ms  NEC_SHORT.encode("3772817503", 32)
  4082 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4082 ms  Sequencer.parseCode("0xe0e0609f")
  4082 ms  <= "3772801183"
  4082 ms  NEC_SHORT.encode("3772801183", 32)
  4082 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4082 ms  Sequencer.parseCode("0xe0e010ef")
  4082 ms  <= "3772780783"
  4083 ms  NEC_SHORT.encode("3772780783", 32)
  4083 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4083 ms  Sequencer.parseCode("0xe0e0906f")
  4083 ms  <= "3772813423"
  4083 ms  NEC_SHORT.encode("3772813423", 32)
  4083 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4083 ms  Sequencer.parseCode("0xe0e050af")
  4083 ms  <= "3772797103"
  4083 ms  NEC_SHORT.encode("3772797103", 32)
  4084 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4084 ms  Sequencer.parseCode("0xe0e030cf")
  4084 ms  <= "3772788943"
  4084 ms  NEC_SHORT.encode("3772788943", 32)
  4084 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4084 ms  Sequencer.parseCode("0xe0e0807f")
  4084 ms  <= "3772809343"
  4084 ms  NEC_SHORT.encode("3772809343", 32)
  4084 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4085 ms  Sequencer.parseCode("0xe0e0b04f")
  4085 ms  <= "3772821583"
  4085 ms  NEC_SHORT.encode("3772821583", 32)
  4085 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4085 ms  Sequencer.parseCode("0xe0e0708f")
  4085 ms  <= "3772805263"
  4085 ms  NEC_SHORT.encode("3772805263", 32)
  4085 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4085 ms  Sequencer.parseCode("0xe0e01ae5")
  4086 ms  <= "3772783333"
  4086 ms  NEC_SHORT.encode("3772783333", 32)
  4086 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4086 ms  Sequencer.parseCode("0xe0e058a7")
  4086 ms  <= "3772799143"
  4086 ms  NEC_SHORT.encode("3772799143", 32)
  4086 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4086 ms  Sequencer.parseCode("0xe0e0a857")
  4086 ms  <= "3772819543"
  4086 ms  NEC_SHORT.encode("3772819543", 32)
  4087 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4087 ms  Sequencer.parseCode("0xe0e008f7")
  4087 ms  <= "3772778743"
  4087 ms  NEC_SHORT.encode("3772778743", 32)
  4087 ms  <= "<instance: co.sensara.sensy.infrared.PulseSequence>"
  4087 ms  Sequencer.parseCode("0x800")
  4087 ms  <= "2048"
  4087 ms  Sequencer.parseCode("0x1fee")
  4087 ms  <= "8174"
  4088 ms  Sequencer.parseCode("0x1fea")
  4088 ms  <= "8170"
  4088 ms  Sequencer.parseCode("0x1fef")
  4088 ms  <= "8175"
  4088 ms  Sequencer.parseCode("0x0ff3")
  4088 ms  <= "4083"
  4088 ms  Sequencer.parseCode("0x1fea")
  4088 ms  <= "8170"
  4088 ms  Sequencer.parseCode("0x0ff2")
  4088 ms  <= "4082"
  4088 ms  Sequencer.parseCode("0x0fe1")
  4088 ms  <= "4065"
  4088 ms  Sequencer.parseCode("0x1fe9")
  4088 ms  <= "8169"
  4089 ms  Sequencer.parseCode("0x0fc7")
  4089 ms  <= "4039"
  4089 ms  Sequencer.parseCode("0x1fce")
  4089 ms  <= "8142"
  4089 ms  Sequencer.parseCode("0x1fe9")
  4089 ms  <= "8169"
  4089 ms  Sequencer.parseCode("0x1fef")
  4089 ms  <= "8175"
  4089 ms  Sequencer.parseCode("0x1fee")
  4089 ms  <= "8174"
  4089 ms  Sequencer.parseCode("0x0fe1")
  4089 ms  <= "4065"
  4089 ms  Sequencer.parseCode("0x1fce")
  4089 ms  <= "8142"
```

```
           /* TID 0x3ddf */
  9332 ms  RemoteControl.sendCode("MENU", "tv")
  9356 ms     | RemoteControl.sendCode("MENU", true)
  9356 ms     |    | InterleavedRemote.dispatchCode("MENU", true)
  9357 ms     |    |    | InterleavedRemote$InterleavedRemoteSet.sendCode("MENU", true)
  9357 ms     |    |    |    | Sequencer$SimpleSequencer.getBurstSequence("MENU")
  9358 ms     |    |    |    | <= "<instance: co.sensara.sensy.infrared.BurstSequence>"
  9358 ms     |    |    |    | BurstSequence.getBursts()
  9359 ms     |    |    |    | <= "<instance: java.util.List, $className: java.util.Collections$UnmodifiableRandomAccessList>"
  9359 ms     |    |    |    | BurstSequence.getBursts()
  9360 ms     |    |    |    | <= "<instance: java.util.List, $className: java.util.Collections$UnmodifiableRandomAccessList>"
  9360 ms     |    |    | InterleavedRemote$InterleavedRemoteSet.sendCode("MENU", false)
  9360 ms     |    |    |    | Sequencer$ToggleSequencer.getBurstSequence("MENU")
  9360 ms     |    |    |    | <= null
  9361 ms     | BluetoothGatt.writeCharacteristic("<instance: android.bluetooth.BluetoothGattCharacteristic>")
  9362 ms     |    | IBluetoothGatt$Stub$Proxy.writeCharacteristic(5, "24:6F:28:B1:03:4A", 61, 2, 0, [6,32,0,0,0,0,-32,-32,88,-89,0,0,0,0,0,0,0,0,0,0])
```

062000000000e0e058a700000000000000000000

06 -> NEC protocol

0x20 -> 32 -> length of the code (4 bytes -> 32 bits)

-32,-32,88,-89 is actually -> e0e058a7 -> neat!


Next steps ->

-> Build a safe IR led circuit for ESP32 (3.3v pins).

Easiest -> https://github.com/crankyoldgit/IRremoteESP8266/blob/master/examples/IRsendDemo/IRsendDemo.ino

https://www.analysir.com/blog/2015/09/01/simple-infrared-pwm-on-arduino-part-3-hex-ir-signals/

https://www.analysir.com/blog/2015/05/12/simple-infrared-pwm-on-arduino/

https://github.com/Darryl-Scott/ESP32-RMT-Library-IR-code-RAW

https://github.com/crankyoldgit/IRremoteESP8266

...
