class Solution:
    
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        n_str = str(n)
        for num in n_str:
            product *= int(num)
            total += int(num)
        return product-total
        
