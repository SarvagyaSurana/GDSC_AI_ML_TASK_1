def shortest_string(final):
    left = 0
    right = len(final) - 1
    operations = 0
    
    while left < right:
        if final[left] != final[right]:
            break
        left += 1
        right -= 1
        operations += 2

    return operations

def main():
    t = int(input())
    for _ in range(t):
        final = input().strip()
        shortest_len = shortest_string(final)
        print(shortest_len)

if __name__ == "__main__":
    main()
