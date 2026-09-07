class Solution:
    def isValid(self, s: str) -> bool:


        '''
        #brute force (string manipulation not double iteration or two pointer)
        # Keep removing valid adjacent pairs until no more can be removed
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        
        # If valid, all pairs dissolve and s becomes empty
        return len(s) == 0
        '''

        stack = list()

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            
            elif char in [')', '}', ']']:
                if not bool(stack) or stack[-1] + char not in  ['()', '{}', '[]']:
                    return False
                stack.pop()
            
        return len(stack) == 0



            
            





                