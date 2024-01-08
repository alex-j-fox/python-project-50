### Hexlet and user tests and linter status, Code Climate badges:
[![Actions Status](https://github.com/alex-j-fox/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alex-j-fox/python-project-50/actions)
[![Actions Status](https://github.com/alex-j-fox/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/alex-j-fox/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d86503c410f675872721/maintainability)](https://codeclimate.com/github/alex-j-fox/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d86503c410f675872721/test_coverage)](https://codeclimate.com/github/alex-j-fox/python-project-50/test_coverage)

# Difference Generator - Gendiff
Gendiff is a program that determines the difference between two data structures.

### Utility Features:

- Support for different input formats: yaml, json
- Generating a report in the form of plain text, stylish and json

## Minimal requirements

- Python version 3.10
- Poetry version 1.5

## Installation

### Installation from GitHub

```
pip install --user --upgrade pip
pip install git+https://github.com/alex-j-fox/python-project-50
```

### Manual installation

1. Clone the repository

```
git clone https://github.com/alex-j-fox/python-project-50
```

2. Navigate to the project directory 

```
cd /home/<user>/python-project-50
```

3. To build and install the package, run the following commands 

```
make build
make publish
make package install
```
[![asciicast](https://asciinema.org/a/omodt3ibXmIsy21j9mgdZnA5E.svg)](https://asciinema.org/a/omodt3ibXmIsy21j9mgdZnA5E)

4. Gendiff documentation
```
usage: gendiff [-h] [-f FORMAT] [--version] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output: stylish, plain, json.
  --version             show gendiff version
```

## Examples of using the program

### Comparison of flat files (JSON) 
[![asciicast](https://asciinema.org/a/NS9uNKDBVSpY29W492FSIMooN.svg)](https://asciinema.org/a/NS9uNKDBVSpY29W492FSIMooN)

### Comparison of flat files (YAML) 
[![asciicast](https://asciinema.org/a/xZMQzmSfHG8adu2Inkski6sw1.svg)](https://asciinema.org/a/xZMQzmSfHG8adu2Inkski6sw1)

### Recursive comparison - stylish format
[![asciicast](https://asciinema.org/a/xoYG8jHFAlYs0y7OxczJqpiCa.svg)](https://asciinema.org/a/xoYG8jHFAlYs0y7OxczJqpiCa)

### Recursive comparison - plain (flat) format
[![asciicast](https://asciinema.org/a/Z9yDonNs28R86ll4Gun3Sum6M.svg)](https://asciinema.org/a/Z9yDonNs28R86ll4Gun3Sum6M)

### Recursive comparison - JSON format
[![asciicast](https://asciinema.org/a/FdUIT7IQ9uTCnYsJ05Ctb4OF2.svg)](https://asciinema.org/a/FdUIT7IQ9uTCnYsJ05Ctb4OF2)