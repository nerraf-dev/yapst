#!/usr/bin/env python3
import subprocess
import random
import sys
from config import PUSH_SWAP, MAX_TEST_SIZE, TEST_COUNT, COLOUR, CHECKER
from setup import check_push_swap, check_checker, check_bonus
from tests import (
	ERROR_HANDLING,
	EDGE_CASES,
	ALMOST_SORTED,
	DESCENDING_ORDER,
	RANDOM_ORDER,
	BM_3,
	BM_5,
	BM_100,
	BM_500,
	)
from runner import run_test_cases, run_error_cases
from utils import print_error_exit


def run_test(bonus, numbers):
	"""
	Executes a test for the push_swap program using the provided list of numbers.

	This function runs the push_swap program with the given numbers, counts the
	number of operations performed, and verifies the result using the CHECKER
	program. Optionally, it also verifies the result using a bonus checker.

	Args:
		numbers (list of int): A list of integers to be sorted by the push_swap program.

	Returns:
		int: The number of operations performed by the push_swap program if the test passes.
		bool: False if the test fails or if the program crashes.

	Behavior:
		- Converts the list of numbers into string arguments for the push_swap program.
		- Runs the push_swap program and captures its output.
		- Counts the number of operations performed by push_swap.
		- Verifies the output using the CHECKER program.
		- Optionally verifies the output using a bonus checker if BONUS is enabled.
		- Prints error messages if the test fails or the program crashes.

	Raises:
		subprocess.CalledProcessError: If the push_swap program crashes during execution.
	"""
	args = [str(n) for n in numbers]
	cmd_push = [PUSH_SWAP] + args
	cmd_check = [CHECKER] + args
	cmd_bonus = ["./checker"] + args

	try:
		# Run push_swap and count operations
		result = subprocess.run(cmd_push, capture_output=True, text=True, check=True)
		ops = result.stdout.splitlines()
		op_count = len(ops)
		# Verify with checker
		checker = subprocess.run(cmd_check, input=result.stdout, capture_output=True, text=True)
		# print(f"Checker: {checker.stdout}")
		if "KO" in checker.stdout:
			print(f"❌ Failed on: {numbers}")
			return False
		if bonus:
			# Verify with bonus checker
			checker_bonus = subprocess.run(cmd_bonus, input=result.stdout, capture_output=True, text=True)
			if "KO" in checker_bonus.stdout:
				print(f"❌ Bonus checker failed on: {numbers}")
				return False
		return op_count
	except subprocess.CalledProcessError:
		print(f"⚠️  Crash on: {numbers}")
		return False

def test_random(size):
	"""
	Tests the push_swap program with a list of random integers of the specified size.

	This function generates a list of random integers within the range of a 32-bit signed integer
	and tests the push_swap program using these numbers. It then prints the number of operations
	performed if the test is successful.

	Args:
		size (int): The number of random integers to generate for the test.

	Returns:
		int: The number of operations performed by the push_swap program if the test is successful,
			 or 0 if the test fails.
	"""
	numbers = random.sample(range(-2147483648, 2147483647 + 1), size)
	op_count = run_test(numbers)
	if op_count:
		print(f"✅ Size {size}: {op_count} ops")
		return op_count
	return 0

def test_error_handling(bonus: bool):
	"""
	Tests the error handling capabilities of the PUSH_SWAP program and its optional BONUS checker.

	This function iterates through a predefined list of test cases (`ERROR_HANDLING`), where each test case
	includes a name, the input arguments (`test`), and a boolean (`should_error`) indicating whether an error
	is expected. It runs the PUSH_SWAP program with the given input and verifies if the output matches the
	expected error behavior.

	If the BONUS feature is enabled, the function also tests the `checker` program by passing the output of
	PUSH_SWAP as input and verifying its error handling behavior.

	Prints:
		- A success message if all tests pass.
		- A failure message with details if any test fails.

	Returns:
		bool: True if all tests pass, False otherwise.
	"""
	count, bonus_count = 0, 0
	for name, test, should_error in ERROR_HANDLING:
		result = subprocess.run([PUSH_SWAP] + test.split(), capture_output=True, text=True)
		if bonus:
			result_bonus = subprocess.run(["./checker"] + test.split(), input=result.stdout, capture_output=True, text=True)
			if ("Error" in result_bonus.stderr) != should_error:
				print(f"❌ Error checker test failed: {name} - {test}")
				return False
			bonus_count += 1
		count+=1
		if ("Error" in result.stderr) != should_error:
			print(f"❌ Error test failed: {name} - {test}")
			return False
	print(COLOUR["GREEN"],f"✅ Push Swap \"Error\" cases passed",COLOUR["ENDC"])
	if bonus:
		print(COLOUR["PURPLE"],f"✅ Checker \"Error\" cases passed",COLOUR["ENDC"])
	return True

def main():
	"""
	Main function to execute the push_swap tester.
	"""
	try:
		check_push_swap()
		check_checker()
		bonus = check_bonus()
	except Exception as e:
		print_error_exit(e)
	if bonus:
		print(COLOUR["GREEN"], "Bonus Checker found", COLOUR["ENDC"])
	# Run tests
	print(COLOUR["HEADER"], "Starting tests...", COLOUR["ENDC"])
	run_error_cases(bonus, "Error Handling", ERROR_HANDLING)
	run_test_cases(bonus, "Edge Cases", EDGE_CASES)
	run_test_cases(bonus, "Almost Sorted", ALMOST_SORTED)
	run_test_cases(bonus, "Descending Order", DESCENDING_ORDER)
	run_test_cases(bonus, "Random Order", RANDOM_ORDER)
	run_test_cases(bonus, "Benchmarks: 3", BM_3)
	run_test_cases(bonus, "Benchmarks: 5", BM_5)
	run_test_cases(bonus, "Benchmarks: 100", BM_100)
	run_test_cases(bonus, "Benchmarks: 500", BM_500)

if __name__ == "__main__":
	main()
