class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__power_status = False

    def get_device_id(self):
        return self.__device_id

    def set_device_id(self, device_id):
        if device_id != "":
            self.__device_id = device_id
        else:
            print("Device ID cannot be empty.")

    def get_power_status(self):
        return self.__power_status

    def set_power_status(self, status):
        self.__power_status = status

    def turn_on(self):
        self.__power_status = True
        print("The", self.name, "device is now on")

    def turn_off(self):
        self.__power_status = False
        print("The", self.name, "device is now off")

    def display_info(self):
        print("\n----- DEVICE INFORMATION -----")
        print("Device Name :", self.name)
        print("Device ID   :", self.__device_id)
        print("Power Status:", "ON" if self.__power_status else "OFF")


class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature):
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        attempt1 = input("Do you want to read the temperature?[yes/no] ")
        if attempt1.lower() == "yes":
            print("The temperature in the room is", self.temperature, "°C")
        elif attempt1.lower() == "no":
            print("Temperature reading ignored")

    def display_info(self):
        super().display_info()
        print("Temperature :", self.temperature, "°C")


class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id, recording_status):
        super().__init__(name, device_id)
        self.recording_status = recording_status

    def start_recording(self):
        attempt2 = input("Do you want to start recording?[yes/no] ")
        if attempt2.lower() == "yes":
            self.recording_status = True
            print("Scene is being recorded")
        elif attempt2.lower() == "no":
            self.recording_status = False
            print("Recording is ignored")

    def stop_recording(self):
        print("Recording has stopped")
        if attempt3.lower() == "no":
            print("Recording is continuing")

    def display_info(self):
        super().display_info()
        print("Recording :", "YES" if self.recording_status else "NO")


class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness):
        super().__init__(name, device_id)
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            self.brightness = 50

    def increase_brightness(self):
        attempt4 = input("Do you want to increase the brightness? [yes/no]: ")
        if attempt4.lower() == "yes":
            level = int(input("Enter the new brightness level (0-100): "))
            if level > 100:
                print("Brightness cannot exceed 100%.")
            elif level < self.brightness:
                print("Brightness must be greater than current brightness.")
            else:
                self.brightness = level
                print(f"Brightness has been increased to {self.brightness}%.")
        else:
            print("Brightness was not changed.")

    def decrease_brightness(self):
        ans = input("Do you want to decrease the brightness? [yes/no]: ")
        if ans.lower() == "yes":
            level = int(input("Enter the new brightness level (0-100): "))
            if level < 0:
                print("Brightness cannot be less than 0%.")
            elif level > self.brightness:
                print("Brightness must be less than current brightness.")
            else:
                self.brightness = level
                print(f"Brightness has been decreased to {self.brightness}%.")
        else:
            print("Brightness was not changed.")

    def display_info(self):
        super().display_info()
        print("Brightness  :", self.brightness, "%")



light = SmartLight("light", 3423, 30)
cctv = SecurityCamera("cctv", 34583, True)
Thermometer = TemperatureSensor("Thermometer", 345867657, 10)

while True:
    print("\n========== SMART DEVICE MANAGEMENT ==========")
    print("a. Display Device Information")
    print("b. Turn Device ON")
    print("c. Turn Device OFF")
    print("d. Read Temperature")
    print("e. Adjust Brightness")
    print("f. Start/Stop Recording")
    print("g. Exit")

    choice = input("Enter your choice: ")

    if choice == "a":
        light.display_info()
        cctv.display_info()
        Thermometer.display_info()

    elif choice == "b":
        print("\na. Smart Light")
        print("b. Security Camera")
        print("c. Temperature Sensor")
        device = input("Choose device: ")

        if device == "a":
            light.turn_on()
        elif device == "b":
            cctv.turn_on()
        elif device == "c":
            Thermometer.turn_on()
        else:
            print("Invalid choice.")

    elif choice == "c":
        print("\na. Smart Light")
        print("b. Security Camera")
        print("c. Temperature Sensor")
        device = input("Choose device: ")

        if device == "a":
            light.turn_off()
        elif device == "b":
            cctv.turn_off()
        elif device == "c":
            Thermometer.turn_off()
        else:
            print("Invalid choice.")

    elif choice == "d":
        Thermometer.read_temperature()

    elif choice == "e":
        print("\na. Increase Brightness")
        print("b. Decrease Brightness")
        option = input("Choose option: ")

        if option == "a":
            light.increase_brightness()
        elif option == "b":
            light.decrease_brightness()
        else:
            print("Invalid choice.")

    elif choice == "f":
        print("\na. Start Recording")
        print("b. Stop Recording")
        option = input("Choose option: ")

        if option == "a":
            cctv.start_recording()
        elif option == "b":
            cctv.stop_recording()
        else:
            print("Invalid choice.")

    elif choice == "g":
        print("Thank you for using Smart Device Management System.")
        break
    else:
        print("Invalid choice.")
