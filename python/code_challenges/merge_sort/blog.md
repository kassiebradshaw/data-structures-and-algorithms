# My Article About Merge Sort

The explanation of "merge sort" from [GeeksforGeeks](geeksforgeeks.org/merge-sort/) tells us that Merge Sort is a "divide and conquer algorithm" - it divides the input list into two halves, calls itself for the two halves, and then merges the two halves back together after they've each been sorted.

## Given Pseudo-code

```Python
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Understanding the Algorithm

This algorithm takes a list as input. 

It finds the middle of the list by dividing the length of the list by two.

Then it splits the list into a "left" side and a "right" side:

* The "left" side is assigned the values from the start of the input list up to the middle.
* The "right" side is assigned the values from the middle of the input list to the end.

The algorithm then calls itself again on each the "left" side and the "right" side.

## Sample List

`[8,4,23,42,16,15]`

## PASS BY PASS BREAKDOWN

![merge sort process step-by-step](merge_sort.jpg)