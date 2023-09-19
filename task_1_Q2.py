n = int(input("Enter the value of n: "))
current_num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(current_num, end=" ")
        current_num = (current_num % n) + 1
    print()
