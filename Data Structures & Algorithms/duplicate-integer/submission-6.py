class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = set()
        for i in nums:
            if i not in out:
                out.add(i)
                continue                
            return True

        return False