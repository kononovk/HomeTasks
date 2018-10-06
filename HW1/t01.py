def rotate(inp_list):
    if len(inp_list) == 0:
        return inp_list
    temp_list = inp_list.copy()
    temp_list.insert(0, temp_list.pop(len(temp_list) - 1))
    return temp_list


a = [1, 2, 3]
rot_a = rotate(a)
print("a = {}, rotated a = {}".format(a, rot_a))
