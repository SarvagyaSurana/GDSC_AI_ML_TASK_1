def check(str1, str2):
    str3 = set(str2)

    for char in str1:
        if char not in str3:
            return "No"
    
    return "Yes"
t = int(input())
for _ in range():
    input = input().split()
    str1 = input[0]
    str2 = input[1]
    result = check(str1, str2)
    print(result)
