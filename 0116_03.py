from collections import deque
a = input()
cycle_a = deque(a[:])
for i in range(len(a)):
    cycle_a.rotate(1)
    print("".join(cycle_a))
