# Drone Control Scripts

This repository contains Python scripts for controlling and interacting with a drone using the MAVSDK library. The scripts demonstrate various functionalities such as connecting to the drone, executing offboard control, reading telemetry data, taking off, and running waypoint missions.

---

## Table of Contents
1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Physical Connection](#physical-connection)
4. [Scripts Overview](#scripts-overview)
5. [Usage](#usage)

---

## Requirements
- Python 3.7+
- MAVSDK-Python Library
- Compatible Drone Hardware with MAVLink Support
- Connection Interface (e.g., Serial)

---

## Setup
1. Clone the repository:
```bash
git clone https://github.com/slsecrets357/drone.git
cd drone
```

2. Install dependencies:
```bash
pip install mavsdk
```

3. Connect the drone via UART.

---

## Physical Connection
To establish communication between the PX4-based flight controller and a Jetson device, follow these steps:

1. **PX4 Setup:**
   - Modify MAVLink instance `MAV_1_CONFIG` in QGroundControl to use `TELEM 3` for MAVLink communication.
   - Set the baud rate and mode settings appropriately (e.g., 57600 baud for telemetry).

2. **Hardware Wiring:**
   - Connect the `TELEM 3` port of the PX4 to the Jetson device.
   - Wiring Configuration:
     - **TX** on PX4 -> **RX** on Jetson.
     - **RX** on PX4 -> **TX** on Jetson.
     - **GND** on PX4 -> **GND** on Jetson.

3. **Verification:**
   - Ensure the connections are secure and verify communication using a serial terminal before running the scripts.

---

## Scripts Overview

### 1. `connect_drone.py`
**Purpose:**
- Connects to the drone via a specified serial port.
- Verifies and confirms the connection status.

**Usage:**
```bash
python connect_drone.py
```

---

### 2. `offboard_example.py`
**Purpose:**
- Demonstrates offboard control by setting target positions in a local coordinate frame.
- Moves the drone through a sequence of waypoints.

**Usage:**
```bash
python offboard_example.py
```

---

### 3. `read_sensors.py`
**Purpose:**
- Fetches and displays telemetry data such as GPS position, battery status, altitude, and attitude.

**Usage:**
```bash
python read_sensors.py
```

---

### 4. `takeoff.py`
**Purpose:**
- Arms the drone.
- Executes a takeoff sequence.
- Lands the drone after a delay.

**Usage:**
```bash
python takeoff.py
```

---

### 5. `waypoint_mission.py`
**Purpose:**
- Defines a series of waypoints.
- Uploads a mission to the drone.
- Executes the mission and monitors progress.

**Usage:**
```bash
python waypoint_mission.py
```

---

## Usage
Make sure your drone is connected and powered on before running any of the scripts. Replace the serial port or system address in the scripts if needed. Each script provides output logs for real-time feedback during execution.

