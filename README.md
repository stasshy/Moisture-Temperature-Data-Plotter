# Moisture & Temperature Data Plotter

This project reads real-time moisture and temperature data from an Arduino sensor (e.g., DHT22/AM2302) and visualizes it using Python's matplotlib.

## Features

- Real-time plotting of moisture and temperature
- Serial communication with Arduino
- Dual y-axes for clear visualization

## Requirements

- Python 3.x
- Arduino board (e.g., UNO)
- DHT22/AM2302 sensor
- Libraries: matplotlib, pyserial

## Setup

1. Install Python dependencies: pip install -r requirements.txt
  
2. Upload the Arduino code from `arduino/sensor_reader.ino` to your board.

3. Connect your Arduino to your PC.

4. Update the serial port in `startGraph.py` as needed (e.g., `"COM6"` or `"/dev/cu.usbmodem1101"`).

## Usage

Run the Python script to start real-time plotting: python startGraph.py


## Example Output

![Example Plot]
![test1](https://github.com/user-attachments/assets/231340f6-c01e-4ec6-9364-0a66868668dd)





