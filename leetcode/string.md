# STRING

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [To Lower Case](#to-lower-case)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
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

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
ans = ""
for c in str:
    if ord('A') <= ord(c) <= ord('Z'):
        ans += chr(ord(c) + ord('a') - ord('A'))
    else:
        ans += c
return ans
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
rev = ""
for c in s:
    rev = c + rev
return rev
reverseWords(self, s: str) -> str:
ans = ""
temp = ""
for c in s:
    if c == " ":
        ans += self.reverse(temp) + " "
        temp = ""
    else:
        temp += c
ans += self.reverse(temp)
return ans
```

