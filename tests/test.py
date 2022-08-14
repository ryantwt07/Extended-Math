import sys
sys.path.insert(1, 'dev')

from lib import ExtenededMath

class Colours:
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    RESET = '\u001b[00m'

print()
print(f"{Colours.YELLOW}Running Checks....{Colours.RESET}")
print()

class TestExtendedMath:
    solution = 8
    test_passed = 0
    test_failed = 0

    def test_add(self):
        calculated_solution = ExtenededMath.add(5, 3)
        if calculated_solution == self.solution:
            print(f"Check 1 (Addition) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 1 (Addition) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1

    def test_subtract(self):
        calculated_solution = ExtenededMath.subtract(9, 1)
        if calculated_solution == self.solution:
            print(f"Check 2 (Subtraction) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 2 (Subtraction) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1

    def test_multiply(self):
        calculated_solution = ExtenededMath.multiply(4, 2)
        if calculated_solution == self.solution:
            print(f"Check 3 (Multiplication) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 3 (Multiplication) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1

    def test_divide(self):
        calculated_solution = ExtenededMath.divide(16, 2)
        if calculated_solution == self.solution:
            print(f"Check 4 (Division) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 4 (Division) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
    
    def test_square_root(self):
        calculated_solution = ExtenededMath.sqrt(64)
        if calculated_solution == self.solution:
            print(f"Check 5 (Square Root) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 5 (Square Root) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
    
    def test_cube_root(self):
        calculated_solution = ExtenededMath.cbrt(512)
        if calculated_solution == self.solution:
            print(f"Check 6 (Cube Root) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 6 (Cube Root) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
    
    def test_discriminant(self):
        calculated_solution = ExtenededMath.discriminant(1, -16, 64)
        if calculated_solution == 0:
            print(f"Check 7 (Discriminant) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 7 (Discriminant) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
    
    def test_solution(self):
        calculated_solution = ExtenededMath.find_solution(1, -16, 64)
        if calculated_solution == (self.solution, self.solution):
            print(f"Check 8 (Solution) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 8 (Solution) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
    
    def test_log(self):
        calculated_solution = ExtenededMath.log(2, 64)
        if calculated_solution == self.solution:
            print(f"Check 9 (Log) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 9 (Log) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
        
    def test_log10(self):
        calculated_solution = ExtenededMath.log10(1073741824)
        if calculated_solution == self.solution:
            print(f"Check 10 (Log10) ------------ {Colours.GREEN}PASSED{Colours.RESET}")
            self.test_passed += 1
        else:
            print(f"Check 10 (Log10) ------------ {Colours.RED}FAILED{Colours.RESET}")
            print(f"{Colours.RED}ERROR{Colours.RESET} >>> Calculated solution is {calculated_solution}. Expected solution is {solution}.")
            self.test_failed += 1
    
    def end_test(self):
        print()
        print("Tests Concluded.")
        print(f"{Colours.YELLOW}Compiling Results... {Colours.RESET}")
        print(f"{Colours.GREEN}{self.test_passed}{Colours.RESET} Passed, {Colours.RED}{self.test_failed}{Colours.RESET} Failed.")
        print()
    
TestExtendedMath.test_add(self=TestExtendedMath)
TestExtendedMath.test_subtract(self=TestExtendedMath)
TestExtendedMath.test_multiply(self=TestExtendedMath)
TestExtendedMath.test_divide(self=TestExtendedMath)
TestExtendedMath.test_square_root(self=TestExtendedMath)
TestExtendedMath.test_cube_root(self=TestExtendedMath)
TestExtendedMath.test_discriminant(self=TestExtendedMath)
TestExtendedMath.test_solution(self=TestExtendedMath)
TestExtendedMath.test_log(self=TestExtendedMath)
TestExtendedMath.test_log10(self=TestExtendedMath)
TestExtendedMath.end_test(self=TestExtendedMath)
