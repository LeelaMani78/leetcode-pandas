class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for x in range(2, int(sqrt(n)) + 1):
            for y in range (1,x):
                if (x-y) % 2==0 or gcd(x,y) !=1:
                    continue
                c =x**2 + y**2
                if c > n:
                    continue
                res +=2 *(n//c)
        return res
        