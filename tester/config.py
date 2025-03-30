import platform


# Config
# You can change these values to test different scenarios
MAX_TEST_SIZE			= 500  # Test up to 500 numbers
TEST_COUNT 				= 5      # Tests per size

# Probably don't need to change these
PUSH_SWAP 				= "./push_swap"
BONUS_CHECKER 			= "./checker"


# Determine the correct checker binary based on the OS
userOs = platform.system()
if userOs == "Darwin":  # MacOS
    CHECKER = "./checker_Mac"
elif userOs == "Linux":
    CHECKER = "./checker_linux"
else:
    CHECKER = None
print(f"checker: {CHECKER}")


# COLOURS
COLOUR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
	"YELLOW": "\033[93m",
    "RED": "\033[91m",
	"PURPLE": "\033[95m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "ENDC": "\033[0m",
}
