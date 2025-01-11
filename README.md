
# Welcome to my python project template
This is a template for a python project. It is meant to be used as a starting point for new projects. It also includes a basic test structure and a basic documentation structure. 
## Introduction
What is this tool about? What does it do? What problem does it solve?

## Getting Started
Do this and do that to get started with the tool.

## Installation
### Prerequisites
- Python 3.xx or higher
- pip package manager for Python 3
- virtualenv package for Python 3
### Creating a virtual environment
First create a new virtual environment using the following command:
```bash
python -m venv .venv
```
Then activate the virtual environment using the following command:
```bash
.venv/Scripts/activate
```
If this results in an error, you may need to change the execution policy of your system. You can do this by running the following command:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Then try to activate the virtual environment again.

### Installing the required packages
Install the required packages from the pyproject.toml using the following command:
```bash
pip install .
```
### Installing the development packages
Install the development packages from the pyproject.toml using the following command:
```bash
pip install .[dev]
```
### Removing the virtual environment
When one wants to start with a clean install simply delete the `.venv` directory.

## Testing
### Running the tests
To run the tests, use the following command:
```bash
pytest tests/main_tests.py
```

## Running the App
To run the app, use the following command:
```bash
python src/main/main.py
```


