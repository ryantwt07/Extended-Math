# Extended Math Libary Documentation

This documentation is a complete guide to using the Extended Math Library Documentation. If you feel that any part of the documentation is incorrect, please create an [issue](https://github.com/ryantwt07/Extended-Math/issues/new/choose) in GitHub.

---
<br>

## Addition (.add)


This function accepts two integer/float values. This function uses simple built-in addition arithemtic to calculate the answer.

*Example of Function Implementation*

```python
answer = ExtendedMath.add(8, 2)
print(answer)
> 10
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Subtraction (.subtract)

This function accepts two integer/float values. This function uses simple built-in subtraction arithemtic to calculate the answer.

*Example of Function Implementation*

```python
answer = ExtendedMath.subtract(8, 2)
print(answer)
> 6
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Mupltiplication (.multiply)

This function accepts two integer/float values. This function uses simple built-in multiplication arithemtic to calculate the answer.

*Example of Function Implementation*

```python
answer = ExtendedMath.multiply(8, 2)
print(answer)
> 16
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Division (.divide)

This function accepts two integer/float values. This function uses simple built-in division arithemtic to calculate the answer.

*Example of Function Implementation*

```python
answer = ExtendedMath.subtract(8, 2)
print(answer)
> 4
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Square Root (.sqrt)

This function accepts an integer/float value. This function uses simple built-in power arithemtic to calculate the answer.

*Example of Function Implementation*

```python
answer = ExtendedMath.sqrt(4)
print(answer)
> 2
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Cube Root (.cbrt)

This function accepts an integer/float value. This function uses simple built-in power arithemtic to calculate the answer.

*Example of Function Implementation*

```python
answer = ExtendedMath.cbrt(8)
print(answer)
> 2
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Discrimnant Value (.discriminant)

This function accepts 3 integer/float values. This function uses simple built-in arithemtic by applying the discriminant formula to calculate the answer.

*Example of Function Implementation*

```python
ExtendedMath.discrimant(a: float, b: float, c: float)
```

```python
answer = ExtendedMath.discriminant(2, 2, 1)
print(answer)
> 0
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

## Find Solution (.find_solution)

This function accepts 3 integer/float values. This function uses simple built-in arithemtic by applying the discriminant formula to calculate the solutions to a graph.

*Example of Function Implementation*

```python
ExtendedMath.discrimant(a: float, b: float, c: float)
```

```python
answer = ExtendedMath.discriminant(2, 2, 1)
print(answer)
> -4
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Logarithm (.log)

This function accepts an integer/float value. This function uses simple built-in power arithemtic to calculate the answer.

*Example of Function Implementation*

```python
log(power: int, num: float)
```

```python
answer = ExtendedMath.log(2, 64)
print(answer)
> 8
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.

<br>

---

<br>

## Logarithm Base-10 (.log10)

This function accepts an integer/float value. This function uses simple built-in power arithemtic to calculate the answer.

*Example of Function Implementation*

```python
log10(num: float)
```

```python
answer = ExtendedMath.log10(1073741824)
print(answer)
> 8
```

> NOTE: You **must** enter a integer/float value. The library will throw a *ValueError* if a non-integer or float value has been introduced.
