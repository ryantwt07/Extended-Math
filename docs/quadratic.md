# Quadratic Documentation

This documentation has detailed information about all quadratic methods in the Extended Math Library.

If you think that there are any errors with this documentation, feel free to open an [issue](https://github.com/ryantwt07/Extended-Math/issues/new/choose) on GitHub. Think you are in the wrong documentation file? Use this [link](main.md) to return back to the main documentation page.

---

### Discriminant (.discriminant)

**Code for Discirminant**

``` python
@staticmethod
def discriminant(a: float, b: float, c: float) -> tuple:
    verify_a = verification.verify_type(a)
    verify_b = verification.verify_type(b)
    verify_c = verification.verify_type(c)
    if verify_a and verify_b and verify_c == True:
        return (b ** 2) - 4 * a * c
    else:
        raise ValueError("Value type is not a float/integer.")
```

This method takes in three floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code:

``` python
import ExtendedMath

print(ExtendedMath.discriminant("Hello", "World", "!"))
```

Console:

```
> ValueError: Value type is not a float/integer.
```

If all the inputs are entered correctly, the code takes the three numbers and uses the discriminant formulae to solve for the value of the discriminant.

Code:

``` python
import ExtendedMath

print(ExtendedMath.discriminant(2, 4, 1))
```

Console:

```
> 8
```

---

### Find Solution (.find_solution)

**Code for Finding Solutions**

``` python
@staticmethod
def find_solution(a: float, b: float, c: float) -> tuple:
    verify_a = verification.verify_type(a)
    verify_b = verification.verify_type(b)
    verify_c = verification.verify_type(c)
    if verify_a and verify_b and verify_c == True:
        return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    else:
        raise ValueError("Value type is not a float/integer.")
```

This method takes in three floats/integer values as a tuple. The code then verifies whether the numbers are in fact floats/integers. If the inputs given when calling the method are strings, the following will occur.

Code:

``` python
import ExtendedMath

print(ExtendedMath.find_solution("Hello", "World", "!"))
```

Console:

```
> ValueError: Value type is not a float/integer.
```

If all the inputs are entered correctly, the code takes the three numbers and uses the discriminant formulae to solve for the solutions of the graph.

Code:

``` python
import ExtendedMath

print(ExtendedMath.find_solution(2, 4, 2))
```

Console:

```
> -1
```

---

**End of Documentation** - [Return to Main Doumentation](main.md)