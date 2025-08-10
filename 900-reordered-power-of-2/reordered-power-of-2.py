class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def digit_count(num):
            count = [0] * 10  # index = digit
            while num > 0:
                count[num % 10] += 1
                num //= 10
            return count
        
        target_count = digit_count(n)
        
        for i in range(31):  # 2^0 to 2^30
            if digit_count(1 << i) == target_count:
                return True
        return False
