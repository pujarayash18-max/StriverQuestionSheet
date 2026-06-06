class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])

                # Count inversions
                count += (mid - left + 1)

                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return count

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = 0
        count += self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.merge(arr, low, mid, high)

        return count

    def numberOfInversions(self, nums):
        return self.mergeSort(nums, 0, len(nums) - 1)
nums = [-10, -5, 6, 11, 15, 17]
sol = Solution()
print(sol.numberOfInversions(nums))