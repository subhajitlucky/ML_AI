def sum_to_n(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    return result

ans = sum_to_n(5)
print(ans)