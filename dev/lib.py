class verification:
    @staticmethod
    def verify_type(num):
        if type(num) == "<class 'float'>" or "<class 'int'>":
            return True
        else:
            return False

class ExtenededMath:
    @staticmethod
    def add(num1: float, num2: float) -> tuple:
        verify_num1 = verification.verify_type(num1)
        verify_num2 = verification.verify_type(num2)
        if verify_num1 and verify_num2 == True:
            return num1 + num2
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def subtract(num1: float, num2: float) -> tuple:
        verify_num1 = verification.verify_type(num1)
        verify_num2 = verification.verify_type(num2)
        if verify_num1 and verify_num2 == True:
            return num1 - num2
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def multiply(num1: float, num2: float) -> tuple:
        verify_num1 = verification.verify_type(num1)
        verify_num2 = verification.verify_type(num2)
        if verify_num1 and verify_num2 == True:
            return num1 * num2
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def divide(num1: float, num2: float) -> tuple:
        verify_num1 = verification.verify_type(num1)
        verify_num2 = verification.verify_type(num2)
        if verify_num1 and verify_num2 == True:
            return num1 / num2
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def sqrt(num: float) -> float:
        verify = verification.verify_type(num)
        if verify == True:
            return num ** 0.5
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def cbrt(num: float) -> float:
        verify = verification.verify_type(num)
        if verify == True:
            return round(num ** (1/3))
        else:
            raise ValueError("Value type is not a float/integer.")

    @staticmethod
    def discriminant(a: float, b: float, c: float) -> tuple:
        verify_a = verification.verify_type(a)
        verify_b = verification.verify_type(b)
        verify_c = verification.verify_type(c)
        if verify_a and verify_b and verify_c == True:
            return (b ** 2) - 4 * a * c
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def find_solution(a: float, b: float, c: float) -> tuple:
        verify_a = verification.verify_type(a)
        verify_b = verification.verify_type(b)
        verify_c = verification.verify_type(c)
        if verify_a and verify_b and verify_c == True:
            return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def log(power: float, num: float) -> float:
        verify_num = verification.verify_type(num)
        verify_pow = verification.verify_type(power)
        if verify_num and verify_pow == True:
            return round(num ** (1/power))
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def log10(num: float) -> float:
        verify_num = verification.verify_type(num)
        if verify_num == True:
            return round(num ** (1/10))
        else:
            raise ValueError("Value type is not a float/integer.")
    
    @staticmethod
    def pi():
        k = 1
        s = 0
        for i in range(1000000):
            if i % 2 == 0:
                s += 4 / k
            else:
                s -= 4 / k
            k += 2
        return s

    @staticmethod
    def e():
        return 2.718281828459045