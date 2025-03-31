#!/usr/bin/env python3
import subprocess
import random
import sys
from config import PUSH_SWAP, MAX_TEST_SIZE, TEST_COUNT, COLOUR, CHECKER
from setup import check_push_swap, check_checker, check_bonus, set_mem_tester
from tests import (
	ERROR_HANDLING,
	NO_ARGUMENT,
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
		mem = set_mem_tester()
		bonus = check_bonus()
	except Exception as e:
		print_error_exit(e)
	if bonus:
		print(COLOUR["GREEN"], "Bonus Checker found", COLOUR["ENDC"])
	# Run tests
	print(COLOUR["HEADER"], "Starting tests...", COLOUR["ENDC"])
	run_error_cases(bonus, mem, "Error Handling", ERROR_HANDLING)
	# run_test_cases(bonus, "No Arguments", NO_ARGUMENT)
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
