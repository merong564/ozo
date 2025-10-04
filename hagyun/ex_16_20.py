def punc_match(data:str):
    list_check=[]
    for character in data:
        if character in '[{(':
            list_check.append(character)
        elif character in')}]':
            if not list_check:
                return False
            top=list_check.pop()
            if (character==')' and top != '(') or (character=='}' and top != '{') or (character==']' and top != '['):
                return False
    return not list_check

def punc_match_gpt(data: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in data:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

# a='dsjalgj13k{PE}'
# b='{(}){(}){}(){}}}'
# c='{}{{}}'
# d='({})(}){)}'

# print(punc_match(a))
# print(punc_match(b))
# print(punc_match(c))
# print(punc_match(d))