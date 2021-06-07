/*
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleServer.cpp
    Ported to Arduino ESP32 by Evandro Copercini
    updates by chegewara
*/

#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define deviceInformationService "0000180a-0000-1000-8000-00805f9b34fb"
#define protocolCharacteristics "5adbd0e0-847a-11e5-985c-0002a5d5c51b"
#define firmwareVersionCharacteristic "00002a26-0000-1000-8000-00805f9b34fb"

#define remoteCodeCharacteristic "064247a0-090d-11e5-9b9a-0002a5d5c51b"
#define remoteService "ed1063c0-090c-11e5-aed6-0002a5d5c51b"

int ledPin = 2;

void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  Serial.println("Starting BLE work!");

  BLEDevice::init("Sensy Remote");
  BLEServer * pServer = BLEDevice::createServer();
  BLEService *deviceInformationService_ = pServer->createService(deviceInformationService);
  BLEService *remoteService_ = pServer->createService(remoteService);

  BLECharacteristic *protocolCharacteristics_ = deviceInformationService_->createCharacteristic(
        protocolCharacteristics,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

  BLECharacteristic *firmwareVersionCharacteristic_ = deviceInformationService_->createCharacteristic(
        firmwareVersionCharacteristic,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

  BLECharacteristic *remoteCodeCharacteristic_ = deviceInformationService_->createCharacteristic(
        remoteCodeCharacteristic,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

  protocolCharacteristics_->setValue("Hello World says Neil");
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
  Serial.println("Characteristic defined! Now you can read it in your phone!");
}

void loop()
{
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
  delay(500);
}
