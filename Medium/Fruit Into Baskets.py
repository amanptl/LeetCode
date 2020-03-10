import collections
def totalFruit(tree):
    ans = windowStart = 0
    basket1EndPos = 0
    basket1 = basket2 = None
    
    for windowEnd, x in enumerate(tree):
        if x != basket1 and x != basket2:
            newSize = windowEnd - windowStart
            if newSize > ans:
                ans = newSize
            basket2 = basket1
            basket1 = x
            windowStart = basket1EndPos
            basket1EndPos = windowEnd
        if x == basket2:
            basket1EndPos = windowEnd
            tempBasket = basket2
            basket2 = basket1
            basket1 = tempBasket
    ans = max(ans, windowEnd-windowStart+1)          
           

print(totalFruit([0]))
print(totalFruit([1,1]))