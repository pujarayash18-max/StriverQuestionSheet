def findRepeatingMissing(nums):
    n = len(nums)

    S = sum(nums)
    SN = n * (n + 1) // 2

    S2 = sum(x * x for x in nums)
    SN2 = n * (n + 1) * (2 * n + 1) // 6

    diff = S - SN            
    diff_sq = S2 - SN2       

    sum_ab = diff_sq // diff 

    A = (diff + sum_ab) // 2 
    B = sum_ab - A

    return [A, B]


nums = [3, 1, 2, 5, 3]
print(findRepeatingMissing(nums))