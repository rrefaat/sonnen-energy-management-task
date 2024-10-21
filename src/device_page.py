class DevicePage:
    def __init__(self, dut):
        self.dut = dut

    def set_system_setup(self, setup_type, inverters, battery_modules, controllers):
        """Set the system configuration (Basic, Standard, Pro)"""
        self.dut.set("system_setup", setup_type)
        self.dut.set("inverters", inverters)
        self.dut.set("battery_modules", battery_modules)
        self.dut.set("controllers", controllers)

    def set_pv_production(self, power):
        """Set PV production (in Watts)"""
        self.dut.set("pv_production", power)

    def set_house_consumption(self, power):
        """Set house consumption (in Watts)"""
        self.dut.set("house_consumption", power)

    def set_storage_command(self, command):
        """Set storage command (charge/discharge) and update status"""
        self.dut.set("battery_storage_command", command)
        if command == "charge":
            self.dut.set("storage_status", "charging")
        elif command == "discharge":
            self.dut.set("storage_status", "discharging")

    def get_storage_status(self):
        """Get the status of the storage system (charging/discharging)"""
        return self.dut.get("storage_status")

    def get_grid_export(self):
        """Get the power exported to the grid"""
        return int(self.dut.get("grid_export"))

    def get_battery_storage(self):
        """Get the current battery storage value"""
        return int(self.dut.get("battery_storage"))
    
    def fibonacci(self):
        """A generator for Fibonacci numbers"""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
