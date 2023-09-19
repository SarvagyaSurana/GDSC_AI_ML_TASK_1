def check_characters(str1, str2):
    str3 = set(str2)

    for char in str1:
        if char not in str3:
            return "No"
    
    return "Yes"
T = int(input())
for _ in range(T):
    input_strings = input().split()
    str1 = input_strings[0]
    str2 = input_strings[1]
    result = check_characters(str1, str2)
    print(result)
