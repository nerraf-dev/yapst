import random

random.seed(42)  # Fixed seed for consistency

INT_MIN = -2147483648
INT_MAX = 2147483647
BM_500 = []

for i in range(10):
    test_case = []
    for _ in range(500):
        # 70% chance to pick smaller numbers, 30% chance for large numbers
        if random.random() < 0.7:
            test_case.append(random.randint(-1000, 1000))  # Smaller range
        else:
            test_case.append(random.randint(INT_MIN, INT_MAX))  # Full range
    test_case_str = " ".join(map(str, test_case))
    BM_500.append((f"500 values #{i + 1}", test_case_str))

# Print the BM_500 list to verify
for test in BM_500:
    print(test)
