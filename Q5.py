class floatstack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Underflow: Stack is empty")

    def print_stack(self):
        if not self.is_empty():
            print("Stack Contents (up to 4 decimal places):")
            for item in self.stack:
                print(f"{item:.4f}")
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0


def main():
    stack = floatstack()
    while True:
        print("\nStack Menu:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Print all elements")
        print("4. Exit")
        choice = input()
        
        if choice == "1":
            value = float(input())
            stack.push(value)
        elif choice == "2":
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"popped element: {popped_value:.4f}")
        elif choice == "3":
            stack.print_stack()
        elif choice == "4":
            break
        else:
            print("invalid choice. choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
