def returns_odd(arr):
    temp_arr = []
    for i in arr:
        if i % 2 == 0:
            temp_arr.append(i)
    return temp_arr
