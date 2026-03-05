# AERT Toolkit
# Data Structures Unit 1 Assignment


# PART A - Stack ADT

class StackADT:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)



# PART B - Factorial


def factorial(n):
    if n < 0:
        return "Invalid Input"

    if n == 0:
        return 1

    return n * factorial(n - 1)



# Fibonacci (Naive)


naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_naive(n - 1) + fib_naive(n - 2)



# Fibonacci (Memoized)


memo_calls = 0

def fib_memo(n, memo):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]



# PART C - Tower of Hanoi


def hanoi(n, source, helper, destination, stack):
    if n == 1:
        move = "Move disk 1 from " + source + " to " + destination
        print(move)
        stack.push(move)
        return

    hanoi(n - 1, source, destination, helper, stack)

    move = "Move disk " + str(n) + " from " + source + " to " + destination
    print(move)
    stack.push(move)

    hanoi(n - 1, helper, source, destination, stack)



# PART D - Binary Search


def binary_search(arr, key, low, high, stack):

    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)



# MAIN FUNCTION

def main():

    print("----- STACK DEMO -----")
    s = StackADT()
    s.push(5)
    s.push(10)
    print("Top element:", s.peek())
    print("Size:", s.size())
    print("Popped:", s.pop())
    print()

    print("----- FACTORIAL -----")
    test_values = [0, 1, 5, 10]
    for value in test_values:
        print("Factorial of", value, "=", factorial(value))
    print()

    print("----- FIBONACCI -----")
    fib_tests = [5, 10, 20, 30]

    for n in fib_tests:
        global naive_calls
        global memo_calls

        naive_calls = 0
        memo_calls = 0

        result1 = fib_naive(n)
        result2 = fib_memo(n, {})

        print("n =", n)
        print("Naive Result:", result1)
        print("Naive Calls:", naive_calls)
        print("Memo Result:", result2)
        print("Memo Calls:", memo_calls)
        print()

    print("----- TOWER OF HANOI (n=3) -----")
    stack_hanoi = StackADT()
    hanoi(3, "A", "B", "C", stack_hanoi)
    print()

    print("----- BINARY SEARCH -----")
    arr = [1, 3, 5, 7, 9, 11, 13]

    search_keys = [7, 1, 13, 2]

    for key in search_keys:
        stack_bs = StackADT()
        index = binary_search(arr, key, 0, len(arr) - 1, stack_bs)
        print("Searching", key, "Index:", index)
        print("Mid positions visited:", stack_bs.data)
        print()

    # Empty array case
    empty = []
    stack_bs = StackADT()
    index = binary_search(empty, 5, 0, -1, stack_bs)
    print("Search in empty array:", index)


if __name__ == "__main__":
    main()
