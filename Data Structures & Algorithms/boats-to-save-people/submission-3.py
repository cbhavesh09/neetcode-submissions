class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        bc = 0
        while l<=r:
            if people[l]+people[r]<= limit:
                bc+=1
                l+=1
                r-=1
            elif people[l]+people[r]>limit:
                bc+=1
                r-=1
        return bc
            
            
            

        