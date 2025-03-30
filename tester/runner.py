import subprocess
from config import PUSH_SWAP, CHECKER, COLOUR

def run_test(bonus, numbers):
	"""
	Executes a test for the push_swap program using the provided list of numbers.
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


def run_error_cases(bonus, test_name, test_cases):
	"""
	Executes error-handling test cases to verify the program's robustness.
	"""
	print(COLOUR["HEADER"], f"Running {test_name} tests...", COLOUR["ENDC"])
	for name, test, should_error in test_cases:
		result = subprocess.run([PUSH_SWAP] + test.split(), capture_output=True, text=True)
		if bonus:
			result_bonus = subprocess.run([CHECKER] + test.split(), input=result.stdout, capture_output=True, text=True)
			if ("Error" in result_bonus.stderr) != should_error:
				print(f"❌ Error checker test failed: {name} - {test}")
				return False

		if ("Error" in result.stderr) != should_error:
			print(f"❌ Error test failed: {name} - {test}")
			return False

	print(COLOUR["GREEN"], "✅ All error-handling tests passed", COLOUR["ENDC"])
	return True


def run_test_cases(bonus, test_name, test_cases):
	"""
	Executes a series of regular test cases and calculates statistics.
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
