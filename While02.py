def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ans = 0
    i = 0
    while i <= len(s):
        if s[i].isalpha():
            ans += 1
        i += 1
    return ans
print(main('2ython 2022'))

    return