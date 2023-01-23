def isValid(s: str) -> bool:
        if len(s) == 0:
            return True
        stacked = []
        stacked.append(s[0])
        mapping = {}
        mapping['('] = ')'
        mapping[')'] = '('
        mapping['{'] = '}'
        mapping['}'] = '{'
        mapping['['] = ']'
        mapping[']'] = '['
        for i in range(1,len(s)):
            if len(stacked) == 0:
                stacked.append(s[i])
                continue
            if mapping[stacked[-1]] == s[i] == ')' or mapping[stacked[-1]] == s[i] == '}' or mapping[stacked[-1]] == s[i] == ']':
                stacked.pop() #Remove the topmost element in the stack.
            else:
                stacked.append(s[i]) #Add a new element at the top of the stac
        if len(stacked) == 0: #2
            return True
        return False #False

ans = isValid("()[]{}")
print(ans)