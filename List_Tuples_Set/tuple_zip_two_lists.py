list1 = [10, 20, 30, 40, 50]
list2 = [70, 60, 50, 40, 30]

for x, y in zip(list1, list2):
    if x == y:
        print(f"Match found: {x}")
        break
else:
    print("No match found")

