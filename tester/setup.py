import platform, os
from config import PUSH_SWAP, CHECKER, COLOUR

def check_bonus() -> bool:
	# Check if bonus checker is available
	if not os.path.isfile("./checker"):
		raise Exception("⚠️  Bonus checker not found")
	return True

def check_push_swap():
	# Check if push_swap is available
	if not os.path.isfile(PUSH_SWAP):
		raise FileNotFoundError(f"⚠️  push_swap not found")
	return False

def	check_checker() -> bool:
	# Check if checker is available
	if not os.path.isfile(CHECKER):
		raise FileNotFoundError("⚠️  Checker binary not found")
	return True
