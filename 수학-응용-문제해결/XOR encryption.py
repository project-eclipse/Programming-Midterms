(key,ASCII) = ('cipher', [38, 8, 19, 0, 69, 17, 11, 8, 2, 9, 6, 6, 6, 27, 80, 7, 11, 82, 2, 73, 19, 7, 8, 2, 22, 29, 21, 26, 69, 27, 16, 73, 17, 27, 22, 27, 4, 7, 21, 12, 69, 19, 67, 28, 30, 1, 20, 7, 6, 73, 19, 7, 1, 23, 77])
for i in range(len(ASCII)): print(chr(ASCII[i]^ord('cipher'[i%6])), end='')