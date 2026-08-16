class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in range(len(numbers)):
            l,r = x+1, len(numbers)-1
            ansi = target- numbers[x]
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid]== ansi:
                    return [x+1,mid+1]
                elif ansi> numbers[mid]:
                    l = mid+1
                elif ansi < numbers[mid]:
                    r = mid-1
                


        