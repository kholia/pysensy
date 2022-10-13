/*
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleServer.cpp
    Ported to Arduino ESP32 by Evandro Copercini
    updates by chegewara
*/

#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

// https://github.com/crankyoldgit/IRremoteESP8266
// https://github.com/crankyoldgit/IRremoteESP8266/blob/master/examples/IRsendDemo/IRsendDemo.ino
#include <Arduino.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>

const uint16_t kIrLed = 4;  // ESP GPIO pin to use. Recommended: 4 (D2). Actually this is D4 on my ESP32 WROOM32 board!
IRsend irsend(kIrLed);  // Set the GPIO to be used to sending the message.

#define deviceInformationService "0000180a-0000-1000-8000-00805f9b34fb"
#define protocolCharacteristics "5adbd0e0-847a-11e5-985c-0002a5d5c51b"
#define firmwareVersionCharacteristic "00002a26-0000-1000-8000-00805f9b34fb"

#define configDescriptor "00002902-0000-1000-8000-00805f9b34fb";

#define remoteService "ed1063c0-090c-11e5-aed6-0002a5d5c51b"
#define programUploadCharacteristics "5adbd0e1-847a-11e5-985c-0002a5d5c51b"
#define remoteCodeCharacteristic "064247a0-090d-11e5-9b9a-0002a5d5c51b"  // we hook this

int ledPin = 2;

class CharacteristicCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *characteristic) {
      std::string rxValue = characteristic->getValue();
      char *p = (char *)rxValue.c_str();

      union {
        unsigned long v;
        unsigned char b[4];
      } code;

      int length = rxValue.length();
      for (int i = 0; i < length; i++) {
        Serial.printf("%02x", p[i]);
      }
      Serial.println("");

      /* Extract the IR data */
      int protocol = p[0];
      if (protocol == 0xff)
        return;
      if (protocol == 6) { // NEC
        Serial.println("NEC code found");
      }
      // memcpy(&code.v, &p[6], 4);  // bad-endian ;)
      int idx = 6;
      code.b[3] = p[idx + 0];
      code.b[2] = p[idx + 1];
      code.b[1] = p[idx + 2];
      code.b[0] = p[idx + 3];

      // irsend.sendNEC(0x00FFE01FUL); // test code
      irsend.sendNEC(code.v);
    }
};

void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  delay(5000);
  Serial.println("Booting Sensy Remote...");

  irsend.begin();

  BLEDevice::init("Sensy Remote");
  BLEServer * pServer = BLEDevice::createServer();

  // Reversed from "public void onServicesDiscovered(BluetoothGatt bluetoothGatt, int i)" function
  //
  BLEService *deviceInformationService_ = pServer->createService(deviceInformationService);

  BLECharacteristic *firmwareVersionCharacteristic_ = deviceInformationService_->createCharacteristic(
        firmwareVersionCharacteristic,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

  //
  BLEService *remoteService_ = pServer->createService(remoteService);
  BLECharacteristic *protocolCharacteristics_ = remoteService_->createCharacteristic(
        protocolCharacteristics,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
  BLECharacteristic *programUploadCharacteristics_ = remoteService_->createCharacteristic(
        programUploadCharacteristics,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
  BLECharacteristic *remoteCodeCharacteristic_ = remoteService_->createCharacteristic(
        remoteCodeCharacteristic,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

  remoteCodeCharacteristic_->setCallbacks(new CharacteristicCallbacks());

  // protocolCharacteristics_->setValue("\x00\x00\x00\x06\x00\x00\x00\x00"); // parseSupportedProtocols()
  protocolCharacteristics_->setValue("\x00\x00\x00\x07\x00\x00\x00\x00"); // parseSupportedProtocols()
  firmwareVersionCharacteristic_->setValue("FW 1.5");   // "readFirmwareVersion()"
  deviceInformationService_->start();
  remoteService_->start();
  // BLEAdvertising *pAdvertising = pServer->getAdvertising();  // this still is working for backward compatibility
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(deviceInformationService);
  pAdvertising->addServiceUUID(remoteService);
  pAdvertising->setScanResponse(true);
  pAdvertising->setMinPreferred(0x06);   // functions that help with iPhone connections issue
  pAdvertising->setMinPreferred(0x12);
  BLEDevice::startAdvertising();
  Serial.println("Sensy Remote is up now!");
}

void loop()
{
  // put your main code here, to run repeatedly:

  digitalWrite(ledPin, HIGH);
  delay(100);
  digitalWrite(ledPin, LOW);
  delay(100);

  delay(1000);
  // irsend.sendNEC(0xe0e058a7UL); // test code
}
