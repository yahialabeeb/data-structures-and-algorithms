# Merge sort 
It is dividing  array into two halves then calling itself for the two halves and devid them untilreach length =1 and then merges the two sorted halves by The merge() function

## Pseudo code
```
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
## Trace
#### Sample Array: [8,4,23,42,16,15]

### Pass 1:
![pass1](mergesortpasses/pass1.PNG)
* Dividing the array to two halfs and divid tthe halfs to halfs until reach length of 1
### Pass 2:
![pass2](mergesortpasses/pass2.PNG)
* merge the halfs and sort during merging  


## Efficency
- Time: O(nLogn) The basic operation of this algorithm is recurrence. 

- Space: O(n) No additional space is being created.