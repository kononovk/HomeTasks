def get_guessed_word(secret_word, used_letters):
    tmp = ""
    for i in secret_word:
        if i in used_letters:
            tmp += (i + ' ')
            continue
        tmp += '_ '
    return tmp


def is_word_guessed(secret_word, used_letters):
    if set(secret_word) == used_letters:
        return True
    return False
