for dataset in range(10):
    lst = input().split()
    T = int(lst[0])
    N = int(lst[1])

    cat = 0

    for i in range(N):
        day = input()
        if day == 'B':
            cat = cat + T - 1
        else:
            if cat > 0:
                cat = cat - 1

    print(cat)
