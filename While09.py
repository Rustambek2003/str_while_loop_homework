def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ans = 0
    i = 0
    while i < len(s):
        ans += int(s[i])
        i += 1
    return ans