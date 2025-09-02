class Device:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def get_info(self):
        return f"Device Name: {self.name}, Device Type: {self.device_type}"
class Computer(Device):
    def __init__(self, name, cpu, ram):
        super().__init__(name, "Computer")
        self.cpu = cpu
        self.ram = ram

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, CPU: {self.cpu}, RAM: {self.ram}GB"
class Smartphone(Device):
    def __init__(self, name, os, camera_megapixels):
        super().__init__(name, "Smartphone")
        self.os = os
        self.camera_megapixels = camera_megapixels

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, OS: {self.os}, Camera: {self.camera_megapixels}MP"

print("=== Device Information ===")
comp = Computer("MyPC", "Intel i7", 16)
phone = Smartphone("MyPhone", "Android", 12)
print(comp.get_info())
print(phone.get_info())