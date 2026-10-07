class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(':')',
            '{':'}',
            '[':']'
        }
        open_brackets = brackets.keys()
        close_brackets = brackets.values()
        size = len(s)

        if size == 0:
            return True
        elif size%2 != 0:
            return False
        else:
            bracket_stack = []
            for bracket in s:
                if bracket in open_brackets:
                    bracket_stack.insert(0,bracket)
                elif bracket in close_brackets and len(bracket_stack) > 0:
                    last_open_bracket = bracket_stack.pop(0)
                    if brackets[last_open_bracket] != bracket:
                        return False
                else: return False
        
        if len(bracket_stack) == 0:
            return True
        else:
            return False