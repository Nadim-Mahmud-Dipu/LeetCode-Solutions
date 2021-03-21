class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats_no = 0
        
        while left<=right:
            
            if left==right:
                boats_no+=1
                break
            
            if people[left] + people[right] <= limit:
                boats_no+=1
                left+=1
                right-=1
            else:
                boats_no+=1
                right-=1
        
        return boats_no