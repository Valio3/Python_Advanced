seq_parentheses = input()
opening_brackets = []
pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}
condition = True

for char in seq_parentheses:
    if char in '({[':
        opening_brackets.append(char)
    elif len(opening_brackets) <= 0 and char not in '{[(':
        condition = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != char:
            condition = False
    if not condition:
        break
if condition and len(opening_brackets) == 0:
    print("YES")
else:
    print("NO")

# seq_parentheses = input()
# stack = []
# condition = True
# for par in seq_parentheses:
#     if len(stack) <= 0 and (par == "}" or par == "]" or par == ")"):
#         condition = False
#         print("NO")
#         break
#     if par == "{" or par == "[" or par == "(":
#         stack.append(par)
#     elif par == "}":
#         if stack[-1] != "{":
#             condition = False
#             print("NO")
#             break
#         else:
#             stack.pop()
#     elif par == "]":
#         if stack[-1] != "[":
#             condition = False
#             print("NO")
#             break
#         else:
#             stack.pop()
#     elif par == ")":
#         if stack[-1] != "(":
#             print("NO")
#             condition = False
#             break
#         else:
#             stack.pop()
#
# if condition and len(stack) == 0:
#     print("YES")
