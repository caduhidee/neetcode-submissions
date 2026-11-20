class Solution:
    def isValid(self, s: str) -> bool:
        # python doesn't appear to have a stack class; we'll use an array
        # Key methods: .append(x), .pop(), isEmpty = not bool(stack)
        stack = []
        closeToOpen = { 
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        if s[0] in closeToOpen:
            return False

        # append to stack
        
        for c in s:
            if c in closeToOpen:
                # check the last item added against the map
                # we're destroying any combo as it appears
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # mismatch for invalid
                    return False
            else:
                stack.append(c)

        # True on empty
        return not bool(stack)
        

            