a=[1,4,3,523,23,12,34,56,78,90,11]
def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort(a))
