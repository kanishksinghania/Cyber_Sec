def split(a):
    return [char for char in a]

def left_shift(input_list):
    first = input_list[0]
    new_list = input_list[1:] + [first]
    return new_list

def left_shift2(input_list):
    first = input_list[0]
    second = input_list[1]
    new_list = input_list[2:] + [first] + [second]
    return new_list

def p10(old_list):
    indices_order = [2,4,1,6,3,9,0,8,7,5]
    new_order = [old_list[i] for i in indices_order]
    return new_order

def p8(old_list):
    indices_order = [5,2,6,3,7,4,9,8]
    new_elements = [old_list[i] for i in indices_order]
    return new_elements

def key_gen():
    key = input("Enter a 10-bit string: ")
    key_list = split(key)

    p_10 = p10(key_list)
    ls = p_10[:5]
    rs = p_10[5:]
    ls = left_shift(ls)
    rs = left_shift(rs)

    new_shift = ls + rs

    key1 = p8(new_shift)
    print("Key 1: ",key1)

    ls2 = left_shift2(ls)
    rs2 = left_shift2(rs)

    new_shift2 = ls2 + rs2

    key2 = p8(new_shift2)
    print("Key 2: ",key2)

key_gen()
