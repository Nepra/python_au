# ARRAY

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
<!---->
## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
counter = 0
maxNum = 0
for i in range (len(nums)):
    if nums[i] == 1:
        counter += 1
    else:
        if counter > maxNum:
            maxNum = counter
        counter = 0
if counter > maxNum:
    maxNum = counter
return maxNum
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
    return nums
ans = [0] * r
for i in range(r):
    ans[i] = [0] * c
rows = 0
columns = 0
for i in range (len(nums)):
    for j in range (len(nums[0])):
        ans[rows][columns] = nums[i][j]
        columns += 1
        if columns == c:
            rows += 1
            columns = 0
return ans
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
r, c = len(M), len(M[0])
ans = [[0] * c for k in M]
for i in range(r):
    for j in range(c):
        count = 0
        for nr in (i - 1, i, i + 1):
            for nc in (j - 1, j, j + 1):
                if 0 <=nr < r and 0 <= nc < c:
                    ans[i][j] += M[nr][nc]
                    count += 1
        ans[i][j] //= count
return ans
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
for row in A:
    for i in range ((len(A[0]) + 1) // 2):
        row[i], row[-i-1] = (row[-i-1] + 1) % 2, (row[i] + 1) % 2
return A
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
r, c = len(A), len(A[0])
B = [[None] * r for k in range(c)]
for i, row in enumerate(A):
    for j, val in enumerate(row):
        B[j][i] = val
return B
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
lastNonZero = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[lastNonZero] = nums[i]
        lastNonZero += 1
for i in range(lastNonZero, len(nums)):
    nums[i] = 0
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
for i in range (len(nums)):
    nums[i] = nums[i] * nums[i]
nums.sort()
return nums
```

