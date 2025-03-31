# YAPSTester

**Yet Another Push Swap Tester** is a tester for the Push Swap project. This tool automates the testing of your `push_swap` program by running a variety of test cases, including error handling, edge cases, and performance benchmarks. It also verifies the correctness of the output using the provided `checker` binaries.

---

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Test Categories](#test-categories)
7. [Contributing](#contributing)
8. [License](#license)

---

## Description

The `YAPST` project is designed to simplify the testing process for the Push Swap program. It ensures that your program handles various scenarios correctly, including invalid inputs, edge cases, and large datasets. The tester also evaluates the performance of your program by counting the number of operations performed.

The tool checks for the presence of the `push_swap`, `checker_OS`, and optional `checker` binaries in the project directory. It uses these binaries to validate the output of your program.

---

## Features

- **Error Handling Tests**: Verifies how your program handles invalid inputs.
- **Edge Case Tests**: Tests scenarios like single elements, sorted inputs, and boundary values.
- **Performance Benchmarks**: Measures the number of operations for datasets of varying sizes.
- **Randomized Tests**: Generates random test cases for additional robustness.
- **Bonus Checker Support**: Optionally validates results using a bonus `checker` binary.

---

## Requirements

- Python 3.6 or higher
- `push_swap` and `checker` binaries
- A Unix-based system (Linux or macOS)

---

## Setup

1. Clone this repository into your `push_swap` project directory:
   ```bash
   git clone https://github.com/nerraf-dev/yapst.git
   ```
1. Copy `test_push_swap.sh` into your `push_swap` project directory:
   ```bash
   cp -r yapst/test_push_swap.sh .
   ```
1. Ensure the push_swap and checker executables are in the same directory as test_push_swap.sh:
   ```
   push_swap
   ├── Makefile
   ├── push_swap
   ├── checker
   ├── checker_OS
   ├── test_push_swap.sh
   ├── src
   │   └── push_swap .c files
   └── tester
       └── tester .py files
   ```
1. Make the script executable:
   ```bash
   chmod +x test_push_swap.sh
   ```
1. Run the script:
   ```bash
   ./test_push_swap.sh
   ```

## Usage

1. Run the script:
   ```bash
   ./test_push_swap.sh
   ```
2. The script will automatically:
   - Check for the presence of the required binaries (`push_swap`, `checker`, and `checker_OS`).
   - Run various test cases.
   - Display results, including the number of operations and any errors.
3. To test specific scenarios, modify the test cases in the `tester/tests.py` file

### Test Categories

The tester includes the following categories of tests:

1. **Error Handling**: Ensures invalid inputs are handled gracefully.
1. **Edge Cases**: Tests scenarios like single elements, sorted inputs, and boundary values.
1. **Almost Sorted**: Evaluates performance on nearly sorted datasets.
1. **Descending Order**: Tests reverse-sorted inputs.
1. **Random Order**: Generates random datasets for testing.
1. **Benchmarks**: Measures performance on datasets of sizes 3, 5, 100, and 500.

## Contributing
Contributions are welcome! If you have ideas for new test cases or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Notes
Ensure that the `push_swap` and `checker` binaries are compiled and functional before running the tester.
For bonus validation, include the `checker` binary in the project directory.
