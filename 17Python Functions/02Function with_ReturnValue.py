def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


s = sum(10, 50)
print(s)