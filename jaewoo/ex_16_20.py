def is_balanced_stack(s: str) -> bool:          # 문자열 s의 괄호 균형 여부를 반환
    stack = []                                  # 여는 괄호를 담을 스택
    pair = {')': '(', ']': '[', '}': '{'}       # 닫힘→여는 괄호 매핑

    for ch in s:                                # 문자열의 각 문자 순회
        if ch in '([{':                         # 여는 괄호면
            stack.append(ch)                    # 스택에 push
        elif ch in ')]}':                       # 닫는 괄호면
            if not stack:                       # 스택이 비었으면 짝이 성립 불가
                return False                    # 실패
            top = stack[-1]                     # 스택 꼭대기(마지막 요소)
            if top != pair[ch]:                 # 짝이 다르면
                return False                    # 실패
            stack.pop()                         # 짝이 맞으므로 pop
        # 그 외 문자(알파벳 등)는 무시
    return not stack                            # 전부 처리 후 스택이 비었으면 균형(True)

print(is_balanced_stack("doc[(df)]"))
print(is_balanced_stack("doc[(df]"))