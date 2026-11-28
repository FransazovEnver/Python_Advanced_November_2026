from collections import deque

liters = int(input())
names = input()
queue = deque()

while names == "Start":
    queue.append(names)
    names = input()

data = input()

while data != "End":
    if data.startswith("refill"):
        liter_to_fill = int(data.split()[-1])
        liters += liter_to_fill
    elif data.isdigit():
        names = queue.popleft()
        liter_wated = int(data)
        if liter_wated <= liters:
            liters -= liter_wated
            print(f"{names} got water")
        else:
            print(f"{names} must wait")
    data = input()
print(f"{liters} liters left")
