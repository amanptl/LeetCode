class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        index = collections.deque(range(len(deck)))
        ans = [0]* len(deck)
        
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        
        return ans
        
            
    
                
