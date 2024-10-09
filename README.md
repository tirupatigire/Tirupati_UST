# Word Frequency Counter and Password Validator

This project consists of two functionalities:
1. Program1.py *check_frequency_of_words*: Counts the frequency of each word from a specified text file.
2. Program2.py *check_the_validity_of_password*: Validates a list of passwords based on specific criteria read from another text file.

## Table of Contents

- [Prerequisites](#prerequisites)
- [File Structure](#file-structure)
- [Input Files](#input-files)
- [Usage](#usage)
- [Expected Output](#expected-output)

## Prerequisites

- Python 3.x should be installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## File Structure

/project-directory
│
├── program1.py # Contains the logic for the word frequency counter 
├── program2.py # Contains the logic for password validation 
├── main.py # The main script that runs both functionalities 
├── inputs
      │
      ├── program1_input.txt # Input file for the word frequency counter 
      ├── program2_input.txt # Input file for password validation 
└── README.md # Documentation for this project


## Input Files

### `program1_input.txt`

This file should contain the input string for which you want to count word frequencies. Words should be separated by spaces.

**Example Content:**
which is better python 2 or python 3

### `program2_input.txt`

This file should input string which contain a comma-separated list of passwords that you want to validate.

**Example Content:**
asqwr1234@1,aF145#,2w3E*,2We3345

## Usage

1. **Clone the repository** or download the project files to your local machine.

2. **Update input files**:
   - Open `program1_input.txt` and enter your desired text.
   - Open `program2_input.txt` and enter the passwords you wish to validate.

3. **Run the main script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the project files.
   - Execute the following command:   python main.py
   - If using any IDE like Pycharm or VS code, etc then directly open the project files in new window and execute the main.py file.
   
   
## Expected Output

1. Program1 (The word frequency counter) will print the frequency of each word from program1_input.txt in the format ('word': count).
2. Program2 (The password validator) will print valid passwords from program2_input.txt, separated by commas.
