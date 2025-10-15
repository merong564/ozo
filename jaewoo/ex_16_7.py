def evaluate_rpn(expr: str):
    stack = [] # 결과를 쌓을 스택(피연산자 저장)

    operator = {"+", "-", "*", "/"} # 연산자 집합

    if not expr.strip(): # 공백만 있는 경우에 막는다
        raise ValueError("빈 식입니다.")
    
    for tok in expr.split(): # 공백 기준으로 토큰을 하나씩 순회
        if tok in operator: # 토큰이 연산자
            if len(stack) < 2: #피연산자가 2개가 부족하면 에러
                raise ValueError("피연산자가 부족합니다.")
            b = stack.pop() #스택에서 오른쪽 피연산자 꺼냄
            a = stack.pop() #스택에서 왼쪽 피연산자 꺼냄

            if tok =="+":
                stack.append(a + b)
            elif tok =="-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                if b == 0: # 0으로 나누기 방지
                    raise ZeroDivisionError("0으로 나눌 수 없습니다.")
                stack.append(a / b)
        else:
            # 숫자 토큰이면 스택에 push (정수/실수 모두 지원)
            if "." in tok:                  # 소수점이 있으면 실수로
                stack.append(float(tok))
            else:                           # 없으면 정수로
                stack.append(int(tok))

    if len(stack) != 1:                     # 모든 처리가 끝났을 때 스택에 결과 하나만 남아야 정상
        raise ValueError("잘못된 식(남은 항이 1개가 아님)")

    result = stack[0]                       # 최종 결과
    # 정수로 딱 떨어지면 int로 깔끔하게 변환해서 반환
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result

print(evaluate_rpn("3 4 + 5 * 4 + 7 -"))