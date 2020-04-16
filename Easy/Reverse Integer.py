def reverse(x):
        rem = abs(x)
        res = 0

        while rem != 0:
            res *= 10
            res += rem % 10
            rem = rem // 10
        
        return res if x > 0 else -res

print(reverse(-1230))