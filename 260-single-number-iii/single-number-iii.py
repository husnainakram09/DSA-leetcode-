class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dup_removed = 0
        for num in nums:
            dup_removed ^= num

        distinguinshed_bits = dup_removed & -dup_removed
        a = b = 0
        for num in nums:
            if num & distinguinshed_bits:
                a ^= num
            else:
                b ^= num
        return [a,b]