def checkio(text):
    text = list(filter(str.isalpha, text.lower()))
    letters = list(set(text))
    # save ord of z - letter to sort descending
    text = [(text.count(c), ord('z') - ord(c)) for c in letters]
    text.sort(reverse=True)
    # recover correct letter
    return chr(ord('z') - text[0][1])

