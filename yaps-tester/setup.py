import platform, os
from config import PUSH_SWAP, CHECKER, COLOUR

def check_bonus() -> bool:
	# Check if bonus checker is available
	if not os.path.isfile("./checker"):
		print(COLOUR["YELLOW"],"⚠️  Bonus checker not found", COLOUR["ENDC"])
		return False
	else:
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

def set_mem_tester():
	# if macOS use leaks
	# if linux use valgrind
	# check platform
	# check if mem tester available
	# if leaks/valgrind not available print message and contrinue
	# if leaks/valgrind available set flag to use additional commands

	if platform.system() == "Darwin":
		if not os.path.isfile("/usr/bin/leaks"):
			print(COLOUR["YELLOW"],"⚠️  Leaks not found", COLOUR["ENDC"])
			return ""
		else:
			print(COLOUR["GREEN"],"Leaks found", COLOUR["ENDC"])
			return "leaks -atExit -- "
	elif platform.system() == "Linux":
		if not os.path.isfile("/usr/bin/valgrind"):
			print(COLOUR["YELLOW"],"⚠️  Valgrind not found", COLOUR["ENDC"])
			return ""
		else:
			print(COLOUR["GREEN"],"Valgrind found", COLOUR["ENDC"])
			return "valgrind --leak-check=full"
	else:
		print(COLOUR["YELLOW"],"⚠️  Unknown OS, no memory leak check", COLOUR["ENDC"])
		return ""


