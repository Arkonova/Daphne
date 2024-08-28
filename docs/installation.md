# Installation Guide

## Prerequisites

Before you install the Daphne library, ensure that you have the following prerequisites installed:

- **Python 3.7+**: Daphne requires Python version 3.7 or higher.
- **pip**: The Python package installer.

## Installation Steps

### 1. Clone the Repository

You can clone the Daphne repository from GitHub:

```bash
git clone https://github.com/Arkonova/Daphne.git
cd Daphne
```
### 2. Install Required Dependencies
Install the required Python packages listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```
### 3. Install the Daphne Library
To install the Daphne library, use the following command:

```bash
pip install .
```
### 4. Verify the Installation
To verify that the installation was successful, you can run the unit tests:

```bash
pytest
```
If all tests pass successfully, the installation is complete, and the Daphne library is ready for use.

### Optional: Installing from PyPI (when available)
Once the library is published on PyPI, you can install it directly using pip:

```bash
pip install Daphne
```
### Troubleshooting
If you encounter any issues during installation, consider the following:

- Ensure that Python 3.7 or higher is installed and added to your system's PATH.
- Verify that all required dependencies are correctly installed.
- For any unresolved issues, refer to the GitHub Issues page or open a new issue. 