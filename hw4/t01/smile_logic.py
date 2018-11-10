open_brackets = ('{', '(', '<', '[')
close_brackets = ('}', ')', '>', ']')


def correct_numbers_of_brackets(inp_str):
    num_of_open = len([i for i in inp_str if i in open_brackets])
    num_of_close = len([i for i in inp_str if i in close_brackets])
    if num_of_open != num_of_close:
        return False
    return True


def last_open_bracket_index(inp_list):
    i = len(inp_list) - 1
    ans = 0
    while i > 0:
        if inp_list[i] in open_brackets:
            ans = i
            break
        i -= 1
    return ans


def bracket_correct(inp_str):
    tmp_str = [i for i in inp_str if i in open_brackets + close_brackets]
    num_of_brackets = len(tmp_str)

    if not correct_numbers_of_brackets(inp_str):
        return False

    while num_of_brackets > 0:
        last_open_index = last_open_bracket_index(tmp_str)

        for i in range(last_open_index + 1, len(tmp_str)):
            if tmp_str[i] in close_brackets:
                if close_brackets.index(tmp_str[i]) != \
                        open_brackets.index(tmp_str[last_open_index]):
                    return False
                else:
                    tmp_str.pop(last_open_index)
                    tmp_str.pop(i - 1)
            break
        num_of_brackets -= 2
    return True


print(bracket_correct("()()([)]"))

