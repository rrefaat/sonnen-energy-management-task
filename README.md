# sonnen-energy-management-task
A Python-based implementation and testing task for simulating energy management in a sonnenBatterie system. Includes energy flow algorithm testing using pytest, a Fibonacci generator, and insights into integrating machine learning in hardware-dependent automation frameworks.

This repository contains the implementation and testing of the energy management algorithm for the sonnenBatterie system using Python and pytest.

Installation Guide
Follow the steps below to set up the environment and run the tests using VS Code:

1. Install Python
Download and install the latest version of Python from python.org.
During installation, make sure to check "Add Python to PATH".
Verify the installation by running this command in the VS Code terminal:
bash
Copy code
python --version
2. Install pytest
Open the terminal in VS Code.
Install pytest by running the following command:
bash
Copy code
pip install pytest
Verify the pytest installation:
bash
Copy code
pytest --version
3. Install Python Extension in VS Code
Open VS Code and go to the Extensions sidebar (Ctrl + Shift + X).
Search for Python by Microsoft and install it.
4. Configure Python Interpreter in VS Code
Open the Command Palette (Ctrl + Shift + P).
Search for Python: Select Interpreter.
Choose the Python interpreter installed on your system.
5. Set up pytest in VS Code
Open the Command Palette (Ctrl + Shift + P).
Search for Python: Configure Tests.
Choose pytest as the default test framework.
6. Running Tests
Create a test file, for example test_example.py:
python
Copy code
def test_example():
    assert 1 + 1 == 2
Run the tests using pytest:
bash
Copy code
pytest
7. (Optional) Create and Use a Virtual Environment
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install pytest in the virtual environment:

bash
Copy code
pip install pytest
Configure VS Code to use the virtual environment:

Open the Command Palette (Ctrl + Shift + P).
Search for Python: Select Interpreter and select the interpreter from the venv folder.
