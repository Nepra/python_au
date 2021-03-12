# INTERVALS

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
<!---->
## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
if len(intervals) < 2:
    return 0
intervals.sort(key=lambda x:x[1])
remove = 0
end = intervals[0][0]
for element in intervals:
    start = element[0]
    if start < end:
        remove += 1
    else:
        end = element[1]
return remove
```


## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
merged = []
intervals.sort(key=lambda x: x[0])
for i in range(len(intervals) - 1):
    if not self.isOverlap(intervals[i], intervals[i + 1]):
        merged.append(intervals[i])
    else:
        intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
        intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
if self.isOverlap(intervals[len(intervals) - 2], intervals[len(intervals) - 1]):
    intervals[len(intervals) - 1][0] = min(intervals[len(intervals) - 2][0], intervals[len(intervals) - 1][0])
    intervals[len(intervals) - 1][1] = max(intervals[len(intervals) - 2][1], intervals[len(intervals) - 1][1])
merged.append(intervals[len(intervals) - 1])
return merged
isOverlap(self, a, b):
return a[0] <= b[1] and b[0] <= a[1]
```

