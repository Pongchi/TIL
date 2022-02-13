X = int(input())


# Line 라인 번호 찾기. 또한 x는 그 라인의 인덱스가 됨.
line = 1
while X > line:
    X -= line
    line += 1

# 라인이 홀수라면 분자가 오름차순, 짝수라면 분모가 오름차순.
# 각 라인의 요소 분자, 분모의 합은 라인+1
print(f"{line+1 - X}/{X}" if line % 2 == 1 else f"{X}/{line+1 - X}")
