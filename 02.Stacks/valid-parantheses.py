def is_valid_parentheses(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


# -------- Driver code --------
tests = ["()", "(())", "())", "(()", "", "()()"]

for t in tests:
    print(f"{t} -> {is_valid_parentheses(t)}")