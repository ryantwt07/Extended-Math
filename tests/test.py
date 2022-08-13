import sys
sys.path.insert(1, 'dev')

from lib import verification
from lib import ExtenededMath

class Colours:
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    RESET = '\u001b[00m'

solution = 8
test_passed = 0
test_failed = 0

print()
print(f"{Colours.YELLOW}Running Checks....{Colours.RESET}")
print()

calculated_solution = ExtenededMath.add(5, 3)
if calculated_solution == solution:
     print(f"Check 1 (Addition) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 1 (Addition) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.subtract(9, 1)
if calculated_solution == solution:
     print(f"Check 2 (Subtraction) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 2 (Subtraction) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.multiply(4, 2)
if calculated_solution == solution:
     print(f"Check 3 (Multiplication) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 3 (Multiplication) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.divide(24, 3)
if calculated_solution == solution:
     print(f"Check 4 (Division) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 4 (Division) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.sqrt(64)
if calculated_solution == solution:
     print(f"Check 5 (Square Root) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 5 (Square Root) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.cbrt(512)
if calculated_solution == solution:
     print(f"Check 6 (Cube Root) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 6 (Cube Root) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.discriminant(2, 4, 1)
if calculated_solution == solution:
     print(f"Check 7 (Discriminant) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
     test_passed += 1
else:
    print(f"Check 7 (Discriminant) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.find_solution(1, -16, 64)
if calculated_solution == (solution, solution):
    print(f"Check 8 (Solution) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
    test_passed += 1
else:
    print(f"Check 8 (Solution) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.log(2, 64)
if calculated_solution == solution:
    print(f"Check 9 (Log) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
    test_passed += 1
else:
    print(f"Check 9 (Log) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

calculated_solution = ExtenededMath.log10(1073741824)
if calculated_solution == solution:
    print(f"Check 10 (Log10) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
    test_passed += 1
else:
    print(f"Check 10 (Log10) ------------ {Colours.RED}FAILED{Colours.RESET}")
    print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
    test_failed += 1

print()
print("Tests Concluded.")
print(f"{Colours.YELLOW}Compiling Results... {Colours.RESET}")
print(f"{Colours.GREEN}{test_passed}{Colours.RESET} Passed, {Colours.RED}{test_failed}{Colours.RESET} Failed.")
print()
