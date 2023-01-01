P = int(input())
B = int(input())
D = int(input())

Bedges = P//B

Answer = Bedges * D + (P - B * Bedges)
print(Answer)