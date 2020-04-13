def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans =[0]*(n+2)
        for book in bookings:
            ans[book[0]]+=book[2]
            ans[book[1]+1]-=book[2]
        print(ans)
        cur =0
        for i in range(1,n+1):
            cur += ans[i]
            ans[i] = cur
        return ans[1:-1]