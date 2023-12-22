#!/usr/bin/python3
def factoring(num):
    lists = []
    for i in range(1, int((num**0.5) + 1)):
        if num % i == 0:
            lists.extend([i, num // i])

    if len(lists) == 2:
        print(f"{num}={lists[1]}*{lists[0]}")
    else:
        for a in range(1, len(lists)):
            if lists[a] * lists[a + 1] == num:
                print(f"{num}={lists[a + 1]}*{lists[a]}")
                break

