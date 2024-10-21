
# Sonnen Energy Management Task

This repository contains the implementation and testing of an energy management algorithm for the **sonnenBatterie** system. The project simulates different setups of energy storage systems (Basic, Standard, and Pro) and covers the logic for energy flow between photovoltaic (PV) panels, battery storage, and grid exports using Python and pytest.

## Project Structure

```
sonnen-energy-management-task/
│
├── src/                        # Source code
│   ├── __init__.py             # Package file for src
│   ├── device_page.py          # Page Object Model (POM) for interacting with DUT
│   └── mock_dut.py             # Mock class for the Device Under Test (DUT)
│
├── tests/                      # Test files
│   ├── __init__.py             # Package file for tests
│   ├── test_energy_management.py # Tests for energy management algorithm
│
├── .gitignore                  # Files to be ignored by Git
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── venv/                       # Virtual environment (if used)
```

## Setup Instructions

To get started with the project, follow these steps:

### 1. Clone the Repository

```bash
https://github.com/rrefaat/sonnen-energy-management-task.git
cd sonnen-energy-management-task
```

### 2. Set Up Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to isolate dependencies:

- On Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Run the Tests

To run the test cases for the energy management algorithm and other features (such as the Fibonacci generator), execute the following command:

```bash
pytest -s
```

The `-s` option shows the output (print statements) in the terminal.

## Usage and Features

This project includes:
- **Energy Management Algorithm Testing**: Simulates different setups of the sonnenBatterie system to ensure energy flows correctly between the PV, battery, and grid.
- **MockDUT**: Mocks the Device Under Test (DUT) for running tests without needing actual hardware.

## How the Algorithm Works

The energy management algorithm follows these rules:
1. If **PV production** exceeds **house consumption**:
   - Charge the **storage** with the surplus.
   - Send any remaining power to the **grid**.
2. If **house consumption** exceeds **PV production**:
   - Use **storage** to power the house.
   - If more power is needed, get it from the **grid**.

## Dependencies

The following Python packages are required for this project:
- `pytest` (for testing)

For more details, see `requirements.txt`.

## Future Improvements

Here are a few ideas for future improvements:
- Adding logging instead of `print()` statements for better test output control.
- Expanding the algorithm to handle edge cases like grid failure or overcharging.
- Implementing continuous integration (CI) for automatic test runs on every commit.