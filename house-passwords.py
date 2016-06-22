def check(data, fun):
    return any(fun(char) for char in data)

def checkio(data):
    return check(data, str.isdigit) and\
           check(data, str.isupper) and\
           check(data, str.islower) and\
           len(data) >= 10
