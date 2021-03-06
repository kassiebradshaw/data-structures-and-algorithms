# Code Challenge 26 - Insertion Sort

[Link to Pull Request](https://github.com/kassiebradshaw/data-structures-and-algorithms/pull/40)

[Link to my code](insertion_sort.py)

[Link to my "blog article"](blog.md)

---

## Assignment

Review the pseudocode, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done, code a working, tested implementation of Insertion Sort based on the pseudocode provided.

Example document [here](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/BLOG)

---

## Pseudocode

```Python
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

---

## Sample Arrays

In your blog article, visually show the output of processing this input array:

`[8,4,23,42,16,15]`

For your own understanding, consider also stepping through these inputs:

* Reverse-sorted: `[20,18,12,8,5,-2]`
* Few uniques: `[5,12,7,5,5,7]`
* Nearly-sorted: `[2,3,5,7,13,11]`

---

## Implementation

* Provide a visual step-through for each of the sample arrays based on the provided pseudocode
* Convert the pseudo-code into working code
* Present a complete set of working tests.
