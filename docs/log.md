# Logarithm Documentation

This documentation has detailed information about all logarithm methods in the Extended Math Library.

If you think that there are any errors with this documentation, feel free to open an [issue](https://github.com/ryantwt07/Extended-Math/issues/new/choose) on GitHub. Think you are in the wrong documentation file? Use this [link](main.md) to return back to the main documentation page.

---

### Log (.log)

**Code for Log**

``` python
@staticmethod
def log(power: float, num: float) -> float:
    verify_num = verification.verify_type(num)
    verify_pow = verification.verify_type(power)
    if verify_num and verify_pow == True:
        return round(num ** (1/power))
    else:
        raise ValueError("Value type is not a float/integer.")
```

This method takes in two floats/integer values. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code:

``` python
import ExtendedMath

print(ExtendedMath.log("Hello", "World!"))
```

Console:

```
> ValueError: Value type is not a float/integer.
```

If all the inputs are entered correctly, the code takes the two numbers and calculates the first number to the power of the inverse of the second number to solve for the base.

Code:

``` python
import ExtendedMath

print(ExtendedMath.log(2, 64))
```

Console: 

```
> 8
```

---

### Log Base-10 (.log10)

**Code for Log Base-10**

``` python
@staticmethod
def log10(num: float) -> float:
    verify_num = verification.verify_type(num)
    if verify_num == True:
        return round(num ** (1/10))
    else:
        raise ValueError("Value type is not a float/integer.")
```

This method takes in a floats/integer. The code then verifies whether the number is in fact a floats/integer. If the input given when calling the method is a string, the following will occur.

Code:

``` python
import ExtendedMath

print(ExtendedMath.log10("Hello!"))
```

Console:

```
> ValueError: Value type is not a float/integer.
```

If all the inputs are entered correctly, the code takes the number and calculates it to the power of 0.1 to solve for the base.

Code:

``` python
import ExtendedMath

print(ExtendedMath.log10(100))
```

Console: 

```
> 10
```

---

**End of Documentation** - [Return to Main Documentation](main.md)