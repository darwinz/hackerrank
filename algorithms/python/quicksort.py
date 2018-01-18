class Solution:

    def quicksort(array):
        qsort(array, 0, len(array) - 1)

    def qsort(array, left, right):
        if left >= right:
            return

        pivot = array[(left + right) / 2]
        index = partition(array, left, right, pivot)
        qsort(array, left, index - 1)
        qsort(array, index, right)

    def partition(array, left, right, pivot):
        while left <= right:
            while array[left] < pivot:
                left += 1

            while array[right] > pivot:
                right -= 1

            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
        return left

