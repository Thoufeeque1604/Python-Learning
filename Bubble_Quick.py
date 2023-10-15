import random
import time


def unique_number_generation(max):
    a = []
    while len(a) < max:
        y = random.randint(1, max)
        if y not in a:
            a.append(y)
    return a


def confirmsorted(nums):
    if nums == sorted(nums, reverse=False):
        print("Confirmed sorted")
    else:
        print("Confirmed Not Sorted")


def bubble(nums):
    print("Sorting using Bubblesort")
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def quicksort(arr):
    print("Sorting using QuickSort")

    def partition(arr, lo, hi):
        # Choose pivot
        mid = (lo + hi) // 2
        if arr[hi] < arr[lo]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[mid] < arr[lo]:
            arr[lo], arr[mid] = arr[mid], arr[lo]
        if arr[hi] < arr[mid]:
            arr[mid], arr[hi] = arr[hi], arr[mid]
        pivot = arr[mid]

        # Hoare partition algorithm
        i = lo - 1
        j = hi + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def helper(arr, lo, hi):
        if lo < hi:
            p = partition(arr, lo, hi)
            helper(arr, lo, p)
            helper(arr, p + 1, hi)

    helper(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    start = time.time()
    size = int(input("Enter ur data size"))
    numbers = unique_number_generation(size)
    confirmsorted(numbers)
    #sorted_final = bubble(numbers)
    sorted_final = quicksort(numbers)
    confirmsorted(numbers)
    print(sorted_final)
    end = time.time()
    print(end-start)

