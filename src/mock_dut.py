class MockDUT:
    """Mock class to simulate the Device Under Test (DUT)"""
    def __init__(self):
        self.values = {}

    def set(self, key: str, value):
        """Mock set method to store values"""
        self.values[key] = value
        return True

    def get(self, key: str):
        """Mock get method to retrieve values"""
        return str(self.values.get(key, "unknown"))
