#selection sort.py
a=[1,4,3,523,23,12,34,56,78,90,11]
def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(selection_sort(a))