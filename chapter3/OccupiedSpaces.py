n = int(input())
Yesterday = input()
Today = input()

occupied = 0

for i in range(len(Yesterday)) :
    if Yesterday[i] == 'C' and Today[i] == 'C' : 
        occupied = occupied +1

print(occupied)