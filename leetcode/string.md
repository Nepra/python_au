# STRING

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
<!---->
## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
first = sorted(s)
second = sorted(t)
return first == second
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
for i in range(len(s) // 2):
    s[i], s[-i - 1] = s[-i - 1], s[i]
return None

```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
vowels = []
for c in s:
    if c in "AaEeIiOoUu":
        vowels.append(c)
return vowels
reverseVowels(self, s: str) -> str:
rev = self.getVowel(s)
ans = ""
for c in s:
    if c in "AaEeIiOoUu":
        ans += rev.pop()
    else:
        ans += c
return ans
```

