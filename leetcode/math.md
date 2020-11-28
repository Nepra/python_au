# MATH

+ [Palindrome Number](#palindrome-number)
<!---->
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

