def emphasize_n_characters(word, n_chars):
    new_word = ""
    for i in range(len(word)):
        if i < n_chars:
            new_word += word[i] + "!"
        else:
            new_word += word[i]
    return new_word

print(emphasize_n_characters('watermelon', 5))