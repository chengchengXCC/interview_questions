class Solution:
    def nthUglyNumber(self, n):
        if n == 1:
            return 1
        i2 = 0
        i3 = 0
        i5 = 0
        nums = []
        nums.append(1)
        while n > 1:
            num_2 = nums[i2] * 2
            num_3 = nums[i3] * 2
            num_5 = nums[i5] * 5
            num = min(min(num_2, num_3), num_5)
            if num > nums[-1]:
                nums.append(num)
                n -= 1
                if num == num_2:
                    i2 += 1
                if num == num_3:
                    i3 =+ 1
                if num == num_5:
                    i5 += 1
        return nums[-1]
