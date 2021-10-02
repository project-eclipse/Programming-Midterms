# 주어진 평문을 주어진 키에 XOR해서 암호문 얻기

(key, plaintext) = (
    "cipher",
    "Each character on a computer is assigned a unique code.",
)  # 키와 평문을 동시에 입력받기
print(
    list(
        map(
            lambda x, y: int(ord(y) ^ ord(x)),
            key * (len(plaintext) // len(key)) + key[0 : len(plaintext) % len(key)],
            plaintext,
        )
    )
)

# lambda, map을 이용해 평문과 키를 평문과 같은 길이가 될 때까지 반복한 배열에서 한 글자씩 차례대로 XOR을 수행함
#
# 사실상 다음과 동일하다:
# cipher = []
# for i in range(len(plaintext)):
#    x = plaintext[i]
#    y = key[i%len(key)]
#    cipher.append(int(ord(y)^ord(x)))
# print(cipher)
