def checkio(data):
    data.sort()
    total = len(data)
    half = int(total / 2)
    if total % 2:
        return data[half]
    elif total > 0:
        return (data[half] + data[half - 1]) / 2.0
