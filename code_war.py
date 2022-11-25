def returns_odd(arr):
    temp_arr = arr[0]
    odd = 0
    even = 0
    odd_num = None
    even_num = None
    for i in arr:
        if i % 2 != 0:
            odd += 1
            odd_num = i
        else:
            even += 1
            even_num = i
    if odd == 1:
        return odd_num
    else:
        return even_num
