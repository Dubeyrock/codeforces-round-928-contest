t = int(input())  # Number of test cases
 
for _ in range(t):
    s = input()  # Input string of length 5
    count_a = s.count('A')  # Count occurrences of A
    count_b = s.count('B')  # Count occurrences of B
 
    if count_a > count_b:
        print('A')
    else:
        print('B')
