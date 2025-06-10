# 🔌 Remote Server Controller with IoT Integration

A professional-grade IoT project for remote server management using a microcontroller (ESP32 or Raspberry Pi), relay board, transistor drivers, and secure cloud connectivity. Developed as part of the Tenmei.tech initiative to demonstrate real-world, scalable IoT applications with a mechatronics foundation.

## 📦 Project Overview

This system enables physical server control remotely via cloud APIs and microcontroller GPIOs. It features:

- **4-Relay Control**:
  - Relay 1: Power Button
  - Relay 2: Reset Button
  - Relay 3: Cooling System
  - Relay 4: Reserved for test/expansion
- **Transistor-based Driving Circuit** (2N2222 + resistors)
- **GPIO-based Control** with secure HTTP or MQTT commands
- **Azure Integration** for Functions and Blob storage
- **Optional Sensor Extensions** (temperature, uptime)

## 🛠 Hardware Requirements

- ESP32 / Raspberry Pi
- 4-Channel Relay Module
- 4x 2N2222 NPN Transistors
- Base Resistors (1kΩ recommended)
- Flyback Diodes (e.g., 1N4007)
- Pin headers, jumper wires, and breadboard or PCB

## 🔧 Circuit Diagram

An illustrated schematic is included to guide the connection between GPIO → resistor → transistor → relay, ensuring safe and reliable switching.

![Relay Diagram](https://tenmei.tech/wp-content/uploads/2025/06/Screenshot-from-2025-06-10-16-14-10.png)

## ☁️ Cloud Architecture

- **Cloud Platform**: Microsoft Azure
- **Functions**: Receive control commands securely
- **Blob Storage**: Logging or status snapshots
- **Security**: Configurable for VPN, IP whitelisting, or token validation

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/satoshinakamoto137/iot_rserver_control.git
   cd server-iot-controller

---

## 🚀 Let’s Build the Future, Together

This project is part of the Tenmei.tech initiative — where innovation, automation, and elegance converge.  
Whether you're a tech enthusiast, enterprise, or visionary collaborator, we invite you to explore more:

👉 **Visit us at [Tenmei.tech](https://tenmei.tech)**  
✨ IoT, AI, and next-gen automation with a touch of excellence.

---

© 2025 Tenmei.tech — All rights reserved.  
This repository and its contents are protected under international copyright.  
Use is permitted under the MIT License (see LICENSE file for details).

