n = int(input('Введите число от 3 до 20 '))
answer = []
for i in range(1, n):
    for j in range(2, n):
        if i > j and n % (i + j) == 0:
            a = [i, j]
            for k in range(len(answer)):
                if answer[k][::-1] == a:
                    continue
        elif i != j and n % (i + j) == 0:
            answer.append([i, j])
b = []
for row in answer:
    for elem in row:
        b.append(str(elem))
result = ''.join(b)
print('Пароль для числа ' + result)
