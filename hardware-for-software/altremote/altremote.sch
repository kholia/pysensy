EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 6890 6890
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L ESP32-DEVKITC-V1:ESP32-DEVKITC-V1 U1
U 1 1 5F981201
P 2800 2450
F 0 "U1" H 2750 3600 50  0000 C CNN
F 1 "ESP32-DEVKITC-V1" H 2800 3500 50  0000 C CNN
F 2 "esp32_devkit_v1_doit:esp32_devkit_v1_doit_modded" H 2800 2450 50  0001 L BNN
F 3 "Espressif Systems" H 2800 2450 50  0001 L BNN
F 4 "4" H 2800 2450 50  0001 L BNN "Field4"
	1    2800 2450
	1    0    0    -1  
$EndComp
$Comp
L altremote-rescue:IR26-21C_L110_TR8-LED D1
U 1 1 5F98DCD6
P 4800 2600
F 0 "D1" V 4839 2482 50  0000 R CNN
F 1 "IR_LED" V 4748 2482 50  0000 R CNN
F 2 "LED_THT:LED_D5.0mm_Horizontal_O1.27mm_Z3.0mm_IRGrey" H 4800 2800 50  0001 C CNN
F 3 "http://www.everlight.com/file/ProductFile/IR26-21C-L110-TR8.pdf" H 4800 2600 50  0001 C CNN
	1    4800 2600
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3600 3350 3700 3350
$Comp
L Device:R R2
U 1 1 5F99F404
P 4300 2950
F 0 "R2" V 4093 2950 50  0000 C CNN
F 1 "1K" V 4184 2950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 4230 2950 50  0001 C CNN
F 3 "~" H 4300 2950 50  0001 C CNN
	1    4300 2950
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x03_Female J1
U 1 1 5F9CC3EC
P 3900 3250
F 0 "J1" H 3900 3450 50  0000 R CNN
F 1 "TestPoints" H 3950 3650 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 3900 3250 50  0001 C CNN
F 3 "~" H 3900 3250 50  0001 C CNN
	1    3900 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 2100 4800 2150
Wire Wire Line
	3600 3250 3700 3250
Wire Wire Line
	3600 2950 3700 2950
Wire Wire Line
	3700 3150 3700 2950
$Comp
L altremote-rescue:R-Device R1
U 1 1 5F99051A
P 4800 2300
F 0 "R1" H 4870 2346 50  0000 L CNN
F 1 "18" H 4870 2255 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 4730 2300 50  0001 C CNN
F 3 "~" H 4800 2300 50  0001 C CNN
	1    4800 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 3350 3700 3350
Connection ~ 3700 3350
Wire Wire Line
	3700 2950 4150 2950
Connection ~ 3700 2950
$Comp
L altremote-rescue:PN2222A-Transistor_BJT Q1
U 1 1 5F983A1F
P 4700 2950
F 0 "Q1" H 4890 2996 50  0000 L CNN
F 1 "PN2222A" H 4890 2905 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4900 2875 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/PN/PN2222A.pdf" H 4700 2950 50  0001 L CNN
	1    4700 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 2950 4500 2950
Wire Wire Line
	3700 3250 4800 3250
Wire Wire Line
	4800 3250 4800 3150
Connection ~ 3700 3250
Wire Wire Line
	4800 2100 4050 2100
Wire Wire Line
	4050 2100 4050 3350
$EndSCHEMATC
