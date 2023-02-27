'''
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if 
the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

def isValid(s: str) -> bool:
    # # Python list as stack
    # # T: O(n) S: O(n)
    
    # stack = [] # Could be up to S: O(n)
    
    # for c in s:
    #     if c in ['(', '{', '[']:
    #         stack.append(c)
    #     else:
    #         if len(stack) == 0: return False
    #         removed = stack.pop()
    #         if c == ')' and removed != '(':
    #             return False
    #         if c == '}' and removed != '{':
    #             return False            
    #         if c == ']' and removed != '[':
    #             return False
    
    # return True if len(stack) == 0 else False



    # Neetcode solution using a hashmap as well
    # T: O(n), S: O(n)

    stack = []
    closeToOpen = {
        ')' : '(',
        '}' : '{',
        ']' : '['
                   }
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
