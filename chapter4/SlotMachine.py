chips = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0
time = 0

while chips >=1 :
    chips = chips -1

    if time == 0 :
        first = first + 1
        if first == 35 :
            first = 0
            chips = chips + 30

    elif time == 1 :
            second = second + 1
            if second == 100 :
                second = 0
                chips = chips + 60

    elif time == 2 :
            third = third + 1
            if third == 10 :
                third = 0
                chips = chips + 9
    
    plays = plays + 1
    time = time + 1

    if time == 3 :
        time = 0

 
print(f'Martha plays {plays} times before going broke.')
