def asquare():
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    prev = 0
 
    for i in range(n):
        curr = sum(arr[i])
        if prev != 0:
            if prev == curr:
                print("SQUARE")
                return
            else:
                print("TRIANGLE")
                return
        prev = curr
 
# Main
t = int(input())
for _ in range(t):
    asquare()
