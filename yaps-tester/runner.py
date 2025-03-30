import subprocess
from config import PUSH_SWAP, CHECKER, COLOUR
import platform

def run_test(bonus, numbers):
	"""
	Executes a test for the push_swap program using the provided list of numbers.

	Parameters:
		bonus (bool): Whether to enable bonus checker verification.
		numbers (list[int]): A list of integers to be sorted by the push_swap program.

	Returns:
		int: The number of operations performed by the push_swap program if successful.
		bool: False if the test fails or the program crashes.
	"""
	args = [str(n) for n in numbers]
	cmd_push = [PUSH_SWAP] + args
	cmd_check = [CHECKER] + args

	try:
		# Run push_swap and count operations
		result = subprocess.run(cmd_push, capture_output=True, text=True, check=True)
		ops = result.stdout.splitlines()
		op_count = len(ops)

		# Verify with checker
		checker = subprocess.run(cmd_check, input=result.stdout, capture_output=True, text=True)
		if "KO" in checker.stdout:
			print(f"❌ Failed on: {numbers}")
			return False

		# Verify with bonus checker if enabled
		if bonus:
			checker_bonus = subprocess.run(cmd_check, input=result.stdout, capture_output=True, text=True)
			if "KO" in checker_bonus.stdout:
				print(f"❌ Bonus checker failed on: {numbers}")
				return False

		return op_count
	except subprocess.CalledProcessError:
		print(f"⚠️  Crash on: {numbers}")
		return False


def run_error_cases(bonus, mem, test_name, test_cases):
	"""
	Executes error-handling test cases to verify the program's robustness.
	"""
	print(COLOUR["HEADER"], f"Running {test_name} tests...", COLOUR["ENDC"])
	cmd_push = [PUSH_SWAP]
	cmd_bonus = [CHECKER]

	if mem:
		print(f"memory tester: {mem}")
		mem_cmd_push = mem.split() + cmd_push
		print(f"cmd_push with memory tester: {mem_cmd_push}")

	for name, test, should_error in test_cases:
		print(f"Running test: {name} - {test}")

		 # Step 1: Run push_swap normally for output validation
		result = subprocess.run(cmd_push + test.split(), capture_output=True, text=True)
		print(f"test cmd: {cmd_push + test.split()}")
		if ("Error" in result.stderr) != should_error:
			print(f"❌ Test failed: {name} - {test}")
			return False

		# Step 2: Run push_swap with leaks or valgrind for memory testing
		if mem:
			print(f"Memory test cmd: {mem_cmd_push + test.split()}")
			try:
				mem_result = subprocess.run(mem_cmd_push + test.split(), capture_output=False, text=True, timeout=30)
				if platform.system() == "Darwin":  # macOS (leaks)
					if "0 leaks for 0 total leaked bytes" not in mem_result.stdout:
						print(f"❌ Memory leak detected for: {name} - {test}")
						return False
				elif platform.system() == "Linux":  # Linux (valgrind)
					if mem_result.returncode != 0:  # Valgrind exits with non-zero code on leaks
						print(f"❌ Memory leak detected for: {name} - {test}")
						print(mem_result.stderr)  # Print valgrind's detailed output
						return False
			except subprocess.TimeoutExpired:
				print(f"❌ Memory test timed out for: {name} - {test}")
				return False

	print(COLOUR["GREEN"], "✅ All error-handling tests passed", COLOUR["ENDC"])
	return True


def run_test_cases(bonus, test_name, test_cases):
	"""
	Executes a series of regular test cases and calculates statistics.

	Parameters:
		bonus (bool): Whether to enable bonus checker verification.
		test_name (str): The name of the test suite.
		test_cases (list[tuple]): A list of tuples, where each tuple contains:
			- name (str): The name of the test case.
			- test (str | list[int]): The input to the push_swap program, either as a string or a list of integers.

	Returns:
		float: The average number of operations across all successful tests, or 0 if no tests succeed.
	"""
	count = 0
	op_total = 0
	op_low = float("inf")
	op_high = float("-inf")

	print(COLOUR["HEADER"], f"Running {test_name} tests...", COLOUR["ENDC"])
	for name, test in test_cases:
		if isinstance(test, str):
			ops = run_test(bonus, test.split())
		elif isinstance(test, list):
			ops = run_test(bonus, test)
		else:
			print(f"⚠️  Invalid test input: {test} (type: {type(test)})")
			continue

		if ops is False:
			print(f"❌ Test failed: {name}")
			continue

		# print(f"✅ TEST: {name} OPS: {ops}")
		if ops < op_low:
			op_low = ops
		if ops > op_high:
			op_high = ops
		op_total += ops
		count += 1
	if count > 0:
		print(COLOUR["BLUE"], f"LOW: {op_low} HIGH: {op_high} AVG: {op_total / count:.2f}", COLOUR["ENDC"])
	else:
		print(COLOUR["RED"], "⚠️  No successful tests to calculate statistics", COLOUR["ENDC"])
	print(COLOUR["GREEN"], COLOUR["BOLD"], f"✅ \"{test_name}\" passed", COLOUR["ENDC"], COLOUR["ENDC"])
	return op_total / count if count > 0 else 0
