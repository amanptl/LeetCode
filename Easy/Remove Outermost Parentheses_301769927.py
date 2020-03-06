class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c = 0
        f = 0
        ans = ""
        for i in range(len(S)):
            if S[i] == "(":
                c += 1
            else:
                c -= 1
            if c == 0:
                ans+=S[f+1:i]
                f = i+1
        return ans
