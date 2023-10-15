def quick_sort(arr):
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
    arr = [67, 100, 84, 82, 9, 54, 83, 94, 72, 48, 24, 63, 15, 1, 58, 89, 64, 47, 42, 88, 10, 85, 70, 74, 81, 68, 3, 86, 8, 31, 46, 73, 90, 26, 80, 33, 25, 61, 4, 69, 17, 95, 43, 65, 71, 53, 6, 21, 52, 62, 59, 98, 97, 92, 66, 41, 37, 57, 19, 7, 29, 22, 38, 16, 56, 87, 79, 78, 36, 77, 13, 96, 32, 51, 35, 11, 93, 50, 76, 5, 44, 39, 30, 60, 55, 27, 14, 75, 28, 45, 49, 20, 2, 40, 91, 34, 23, 12, 18, 99]
    answer = quick_sort(arr)
    print(arr)