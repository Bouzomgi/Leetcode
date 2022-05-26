class Solution:
    def isValid(self, s: str) -> bool:
        para = {')': '(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in para:
                if not stack or stack.pop() != para[i]:
                    return False
            else:
                stack.append(i)
                
        if stack:
            return False
        
        return True