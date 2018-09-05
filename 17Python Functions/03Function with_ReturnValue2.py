def sum(start, end):
    if (start > end):
        print("start should be less than end")
        return  # here we are not returning any value so a special value None is returned
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


s = sum(110, 50)
print(s)