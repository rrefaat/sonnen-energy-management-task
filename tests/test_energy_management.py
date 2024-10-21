import pytest
from src.device_page import DevicePage
from src.mock_dut import MockDUT

@pytest.fixture
def dut():
    """Fixture to provide a mock DUT"""
    return MockDUT()

@pytest.fixture
def restore_device_state(dut):
    # Ensure the device returns to a normal state after each test
    yield
    dut.set('system_reset', True)

@pytest.mark.parametrize("system_setup, inverters, battery_modules, controllers", [
    ("Basic", 1, 2, 1),
    ("Standard", 1, 3, 1),
    ("Pro", 1, 5, 1)
])
def test_energy_management_algorithm(dut, restore_device_state, system_setup, inverters, battery_modules, controllers):
    print(f"Testing system setup: {system_setup} with {inverters} inverters, {battery_modules} battery modules, and {controllers} controllers.")

    # Setup system
    device = DevicePage(dut)
    device.set_system_setup(system_setup, inverters, battery_modules, controllers)

    # Simulate the case where PV production exceeds house consumption
    device.set_pv_production(5000)  # PV produces 5000W
    device.set_house_consumption(3000)  # House consumes 3000W
    
    print(f"PV production: {5000}W, House consumption: {3000}W")
    
    # Expect surplus to charge the battery
    device.set_storage_command("charge")
    status = device.get_storage_status()
    print(f"Storage command: 'charge', Storage status: {status}")
    assert status == "charging", "Battery should charge with surplus energy"

    # Verify surplus goes to the grid
    surplus = 5000 - 3000  # Surplus energy
    dut.set("grid_export", surplus)
    grid_export = int(dut.get("grid_export"))
    print(f"Surplus energy to grid: {grid_export}W")
    assert grid_export == surplus, "Remaining surplus should go to the grid"
    
    # Simulate the opposite case where house consumption exceeds PV production
    device.set_pv_production(2000)  # PV produces only 2000W
    device.set_house_consumption(3000)  # House still consumes 3000W

    print(f"PV production: {2000}W, House consumption: {3000}W")
    
    # Expect battery to discharge to meet consumption
    device.set_storage_command("discharge")
    status = device.get_storage_status()
    print(f"Storage command: 'discharge', Storage status: {status}")
    assert status == "discharging", "Battery should discharge to meet house consumption"
    print("Test passed.")


def test_fibonacci_generator():
    """Test the Fibonacci generator"""
    
    dut = MockDUT()
    device = DevicePage(dut)

    # Use the fibonacci generator
    fib_gen = device.fibonacci()

    # Generate the first 10 Fibonacci numbers and compare with expected values
    fib_sequence = [next(fib_gen) for _ in range(10)]
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    assert fib_sequence == expected_sequence, f"Fibonacci sequence mismatch. Expected {expected_sequence}, got {fib_sequence}"

    print("Fibonacci test passed.")