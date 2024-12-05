# Raspberry Pi Programs Collection

This repository contains a collection of Python programs designed to work with a Raspberry Pi, covering various use cases such as controlling LEDs, interacting with Firebase, and handling RFID data. Each project demonstrates practical applications of Raspberry Pi GPIO and other peripherals.

## Table of Contents

1. [GUI PWM Control](#1-gui-pwm-control)
2. [GUI Using Tkinter](#2-gui-using-tkinter)
3. [Get Started with Bottle](#3-get-started-with-bottle)
4. [LED Blinking](#4-led-blinking)
5. [LED PWM Control](#5-led-pwm-control)
6. [RFID Read](#6-rfid-read)
7. [Buzzer Control](#7-buzzer-control)
8. [Interrupt Handling](#8-interrupt-handling)
9. [RFID Firebase Integration](#9-rfid-firebase-integration)
10. [RFID Firebase Test](#10-rfid-firebase-test)

## 1. GUI PWM Control

### What it does:
This program allows the user to control the brightness of an LED using PWM on the Raspberry Pi. It provides a GUI using Tkinter, where users can adjust the PWM duty cycle.

### How it’s done:
- The program uses the `Tkinter` library to create a vertical slider.
- The `RPi.GPIO` library is used to control the PWM signal on GPIO pin 18.
- The slider adjusts the brightness of the LED in real-time.

### Specs:
- **GPIO Pin**: 18
- **PWM Frequency**: 500Hz
- **GUI Framework**: Tkinter

---

## 2. GUI Using Tkinter

### What it does:
This program creates a simple graphical interface to toggle an LED connected to GPIO pin 18. The user can turn the LED on and off using a checkbox.

### How it’s done:
- Utilizes the `Tkinter` library to create a checkbox.
- The state of the checkbox controls the GPIO pin to turn the LED on or off.

### Specs:
- **GPIO Pin**: 18
- **GUI Framework**: Tkinter

---

## 3. Get Started with Bottle

### What it does:
A simple web application created with the Bottle web framework. It serves a basic webpage that can greet the user.

### How it’s done:
- The `Bottle` web framework is used to handle HTTP requests.
- A simple `GET` request is made to display a greeting message on the web page.

### Specs:
- **Web Framework**: Bottle
- **Port**: 8080

---

## 4. LED Blinking

### What it does:
This program blinks an LED connected to GPIO pin 18, turning it on and off at regular intervals.

### How it’s done:
- The `RPi.GPIO` library is used to control the state of the LED on GPIO pin 18.
- A simple loop with `time.sleep()` creates the blinking effect.

### Specs:
- **GPIO Pin**: 18
- **Blink Interval**: 0.5 seconds

---

## 5. LED PWM Control

### What it does:
This program controls the brightness of an LED using Pulse Width Modulation (PWM) on GPIO pin 18.

### How it’s done:
- The `RPi.GPIO` library is used to control the PWM signal on GPIO pin 18.
- The user can input a value to adjust the brightness of the LED.

### Specs:
- **GPIO Pin**: 18
- **PWM Frequency**: 50Hz

---

## 6. RFID Read

### What it does:
This program reads RFID tags using the `MFRC522` module and displays the RFID card ID and associated text.

### How it’s done:
- The `mfrc522` library is used to interface with the MFRC522 RFID reader.
- Upon detecting an RFID card, the program prints the card’s ID and text.

### Specs:
- **Module**: MFRC522
- **GPIO Pin**: Configured for the MFRC522 module

---

## 7. Buzzer Control

### What it does:
This program controls the pitch and duration of a buzzer connected to GPIO pin 18.

### How it’s done:
- The program generates sound using a buzzer connected to GPIO pin 18.
- The user can input the pitch (frequency) and duration (time) of the sound.

### Specs:
- **GPIO Pin**: 18
- **Frequency Range**: 200 Hz to 2000 Hz

---

## 8. Interrupt Handling

### What it does:
This program demonstrates the use of GPIO interrupts. It detects when a button connected to GPIO pin 18 is pressed and triggers an action.

### How it’s done:
- The `RPi.GPIO` library is used to detect a falling edge on GPIO pin 18.
- When the button is pressed, an interrupt is triggered, and a callback function is executed.

### Specs:
- **GPIO Pin**: 18
- **Interrupt Trigger**: Falling edge (button press)

---

## 9. RFID Firebase Integration

### What it does:
This program integrates RFID reading with Firebase. It reads RFID cards and stores the data (such as ID and text) into Firebase in real-time.

### How it’s done:
- The program uses the `firebase_admin` library to interface with Firebase.
- Upon reading an RFID card, the data is uploaded to a Firebase Realtime Database.

### Specs:
- **Module**: MFRC522
- **Database**: Firebase Realtime Database

---

## 10. RFID Firebase Test

### What it does:
This test program simulates RFID operations with Firebase. It allows reading and writing actions to Firebase based on RFID events.

### How it’s done:
- The program interacts with Firebase by setting or deleting actions in the database when an RFID card is read.
- It simulates real-time interaction with Firebase based on specific timings.

### Specs:
- **Database**: Firebase Realtime Database
- **Firebase Action**: Write and delete data


