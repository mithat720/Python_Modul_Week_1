n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
for num in arr:
    if num < arr[0]:
        print(num)
        break