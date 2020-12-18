# MATH

+ [Base 7](#base-7)
+ [Sqrt(x)](#sqrtx)
+ [Fibonacci Number](#fibonacci-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Palindrome Number](#palindrome-number)
+ [Reverse Integer](#reverse-integer)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
<!---->
## Base 7

https://leetcode.com/problems/base-7/

```python
if num < 0:
    isNeg = True
else:
    isNeg = False
if num == 0:
    return "0"
num = abs(num)
while num != 0:
    ans = str(num % 7) + ans
    num //= 7
if isNeg:
    ans = "-" + ans
return ans
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
while root * root <= x:
    root += 1
return root - 1
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
if N == 0:
    return 0
if N == 1:
    return 1
return self.fib(N - 1) + self.fib(N - 2)
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
answer = []
for i in range (1, n + 1):
    if i % 15 == 0:
        answer.append('FizzBuzz')
    elif i % 3 == 0:
        answer.append('Fizz')
    elif i % 5 == 0:
        answer.append('Buzz')
    else:
        answer.append(str(i))
return answer
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
if x < 0:
    return False
if x < 10:
    return True
x = str(x)
for i in range (len(x)):
    if x[i] != x[len(x) - i - 1]:
        return False
return True
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
x = str(x)
if x[0] == '-':
    IsNeg = True
    x = x.replace('-', '')
    y = '-'
else:
    IsNeg = False
    y = ''
for i in range(len(x) - 1, -1, -1):
    y += x[i]
y = int(y)
if (y > - (2 ** 31)) and (y < 2 ** 31 - 1):
    return y
else:
    return 0

```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
ans = 0
A.sort()
for i in range (len(A) - 1, 1, -1):
    if A[i] < A[i - 1] + A[i - 2]:
        return A[i] + A[i - 1] + A[i - 2]
return ans

```

