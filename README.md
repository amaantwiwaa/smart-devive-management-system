# smart-device-management-system

A Python-based command-line application that simulates a Smart Home Management System. This project fulfills the Object-Oriented Programming (OOP) assignment requirements to model real-world smart appliances using foundational programming architectures.

##  Academic Details
* **Project By:** Boateng Nana Ama Antwiwaa
* **Class/ID:** El 1A FOE.41.006.065.25

---

## Task Summary
The objective of this project is to build a smart device ecosystem using Python OOP. It establishes a master `SmartDevice` base class containing shared properties (device name, unique ID, and power status) and branches into three distinct, functional subclasses:
1. **SmartLight:** Controls ambient brightness percentages with custom limits.
2. **SecurityCamera:** Manages live stream recording status workflows.
3. **TemperatureSensor:** Exposes a simulation interface to read room metrics.

The program includes interactive console menus enabling full runtime control over every device's state, parameters, and power configurations.

---

##  OOP Concepts Implemented

* **Encapsulation:** Protects sensitive metrics (`__device_id`, `__power_status`) via private attributes managed strictly through explicit getters and setters.
* **Inheritance:** Extends structural features from the parent `SmartDevice` class down to domain-specific appliance types using `super().__init__()`.
* **Polymorphism:** Customizes data reporting by overriding the parent `display_info()` routine within specialized subclasses.

---

##  How to Run the Program

### Prerequisites
* Ensure you have **Python 3.x** installed on your computer.

### Steps to Run

1. Clone this repository to your local machine:
   ```bash
   git clone 
2. Open your terminal or command prompt and navigate to the project directory:
   ```bash
   cd smart-device-management-system
   ```

3. Run the script using Python:
   ```bash
   python main.py
   ```
   *(Note: Change `main.py` if your file has a different name).*

---

##  Menu Interface Overview

Upon execution, interact with the system using numerical choices (1-7):
* **1-3:** General device state evaluation and master power switches.
* **4-6:** Subclass hardware triggers (readings, dims, and recordings).
* **7:** Gracefully exit the loop.
