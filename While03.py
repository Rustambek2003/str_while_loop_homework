def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ans = 0
    i = 0
    while i <= len(s):
        if s[i].isdigit() or s[i].isalpha():
            ans += 0
        else:
            ans += 1
        i += 1
    return ans