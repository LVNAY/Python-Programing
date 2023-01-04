from configparser import SafeConfigParser


song = 'ABCDE'

button = 0

while button != 4:
    button = int(input())
    presses = int(input())
    for i in range(presses):
        if button == 1:
            song = song[1:] + song[0]
        elif button == 2:
            song = song[-1] + song[:-1]
        elif button == 3:
            song = song[1] + song[0] + songs[2:]

output = ''
for s in song :
    output = output + s + ' '

print(output[:-1])
