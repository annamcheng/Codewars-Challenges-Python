def averages(arr):
    return [(a +b)//2 for a,b in zip(arr, arr[1:])]

print(averages([1, 3, 5, 1, -10]))
# [2, 4, 3, -4.5]
# i == [0,1,2,3,4]
# arr[0] + arr[1] // 2
# arr[1] + arr[2] // 2
# arr[2] + arr[3] // 2
# arr[3] + arr[4] // 2