

def bubble(list_a):
    index_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True 
        for i in range(0, index_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                print(list_a)
        
    return list_a

print(bubble([2, 9, 5, 7, 12, 1, 6, 3, 8, 13, 2, 3, 3, 10, 4, 14, 11]))