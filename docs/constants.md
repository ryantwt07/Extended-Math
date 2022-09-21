# Constants Documentation

This documentation has detailed information about all constant methods in the Extended Math Library.

If you think that there are any errors with this documentation, feel free to open an [issue](https://github.com/ryantwt07/Extended-Math/issues/new/choose) on GitHub. Think you are in the wrong documentation file? Use this [link](main.md) to return back to the main documentation page.

---

### Pi (.pi)

**Code for Pi**

``` python
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
```

<br/>

This method uses the Leibniz's Formulae to derive the value of Pi. This method does not take in any inputs and returns the value of Pi.

Code:

``` python
import ExtendedMath

print(ExtendedMath.pi())
```

Console:

```
> 3.1415916535897743
```

---

### e (.e)

**Code for e**

``` python
@staticmethod
def e():
    return 2.718281828459045
```

<br/>

This method does not take in any inputs and returns the preset value of e.

Code:

``` python
import ExtendedMath

print(ExtendedMath.e())
```

Console:

```
> 2.718281828459045
```

---

**End of Documentation** - [Return to Main Documentation](main.md)
