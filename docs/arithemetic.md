# Arithemetic Documentation

This documentation has detailed information about all arithemetic methods in the Extended Math Library.

If you think that there are any errors with this documentation, feel free to open an [issue](https://github.com/ryantwt07/Extended-Math/issues/new/choose) on GitHub. Think you are in the wrong documentation file? Use this [link](main.md) to return back to the main documentation page.

---

### Addition (.add)

**Code for Addition**

``` python
@staticmethod
def add(num1: float, num2: float) -> tuple:
    verify_num1 = verification.verify_type(num1)
    verify_num2 = verification.verify_type(num2)
    if verify_num1 and verify_num2 == True:
        return num1 + num2
    else:
        raise ValueError("Value type is not a float/integer.")
```

<br/>

This method takes in two floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code: 

``` python
import ExtendedMath

print(ExtendedMath.add("Hello", "World"))
```

Console:

``` 
> ValueError: Value type is not a float/integer.
```

If all inputs are entered correctly, the code takes the two numbers and uses Python's basic arithemetic to solve for the answer.

Code:

``` python
import ExtendedMath

print(ExtendedMath.add(4, 8))
```

Console:

```
> 12
```

---

### Subtraction (.subtract)

**Code for Subtraction**

``` python
@staticmethod
def subtract(num1: float, num2: float) -> tuple:
    verify_num1 = verification.verify_type(num1)
    verify_num2 = verification.verify_type(num2)
    if verify_num1 and verify_num2 == True:
        return num1 - num2
    else:
        raise ValueError("Value type is not a float/integer.")
```

<br/>

This method takes in two floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code: 

``` python
import ExtendedMath

print(ExtendedMath.subtract("Hello", "World"))
```

Console:

``` 
> ValueError: Value type is not a float/integer.
```

If all inputs are entered correctly, the code takes the two numbers and uses Python's basic arithemetic to solve for the answer.

Code:

``` python
import ExtendedMath

print(ExtendedMath.subtract(8, 4))
```

Console:

```
> 4
```

---

### Multiplication (.multiply)

**Code for Multiplication**

``` python
@staticmethod
def multiply(num1: float, num2: float) -> tuple:
    verify_num1 = verification.verify_type(num1)
    verify_num2 = verification.verify_type(num2)
    if verify_num1 and verify_num2 == True:
        return num1 * num2
    else:
        raise ValueError("Value type is not a float/integer.")
```

<br/>

This method takes in two floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code: 

``` python
import ExtendedMath

print(ExtendedMath.multiply("Hello", "World"))
```

Console:

``` 
> ValueError: Value type is not a float/integer.
```

If all inputs are entered correctly, the code takes the two numbers and uses Python's basic arithemetic to solve for the answer.

Code:

``` python
import ExtendedMath

print(ExtendedMath.multiply(8, 4))
```

Console:

```
> 32
```

---

### Division (.divide)

**Code for Division**

``` python
@staticmethod
def subtract(num1: float, num2: float) -> tuple:
    verify_num1 = verification.verify_type(num1)
    verify_num2 = verification.verify_type(num2)
    if verify_num1 and verify_num2 == True:
        return num1 / num2
    else:
        raise ValueError("Value type is not a float/integer.")
```

<br/>

This method takes in two floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code: 

``` python
import ExtendedMath

print(ExtendedMath.divide("Hello", "World"))
```

Console:

``` 
> ValueError: Value type is not a float/integer.
```

If all inputs are entered correctly, the code takes the two numbers and uses Python's basic arithemetic to solve for the answer.

Code:

``` python
import ExtendedMath

print(ExtendedMath.divide(8, 4))
```

Console:

```
> 2
```

---

### Square Root (.sqrt)

**Code for Square Root**

``` python
@staticmethod
def sqrt(num: float) -> float:
    verify = verification.verify_type(num)
    if verify == True:
        return num ** 0.5
    else:
        raise ValueError("Value type is not a float/integer.")
```

<br/>

This method takes in two floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code: 

``` python
import ExtendedMath

print(ExtendedMath.sqrt("Hello"))
```

Console:

``` 
> ValueError: Value type is not a float/integer.
```

If all inputs are entered correctly, the code takes the two numbers and uses Python's basic arithemetic to solve for the answer.

Code:

``` python
import ExtendedMath

print(ExtendedMath.sqrt(4))
```

Console:

```
> 2
```

---

### Cube Root (.cbrt)

**Code for Cube Root**

``` python
@staticmethod
def sqrt(num: float) -> float:
    verify = verification.verify_type(num)
    if verify == True:
        return round(num ** (1/3))
    else:
        raise ValueError("Value type is not a float/integer.")
```

<br/>

This method takes in two floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code: 

``` python
import ExtendedMath

print(ExtendedMath.cbrt("Hello"))
```

Console:

``` 
> ValueError: Value type is not a float/integer.
```

If all inputs are entered correctly, the code takes the two numbers and uses Python's basic arithemetic to solve for the answer.

Code:

``` python
import ExtendedMath

print(ExtendedMath.cbrt(8))
```

Console:

```
> 2
```

---

**End of Documentation** - [Return to Main Documentation](main.md)