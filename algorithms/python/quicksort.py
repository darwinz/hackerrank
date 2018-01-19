class Solution:

    def quicksort(self, array):
        print "Starting now"
        try:
            self.qsort(array, 0, len(array) - 1)
        except Exception as e:
            print e.message

    def qsort(self, array, left, right):
        if left >= right:
            return

        pivot = array[(left + right) / 2]
        index = self.partition(array, left, right, pivot)
        self.qsort(array, left, index - 1)
        self.qsort(array, index, right)
        print array

    def partition(self, array, left, right, pivot):
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

try:
    sln = Solution()
    sln.quicksort([52, 23, 17, 27, 4, 78, 10, 12])
except Exception as e:
    print "There was a problem " + e.message
