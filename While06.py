def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    ans = 0
    i = 0
    while i < len(s):
        if s[i] == 'A' or s[i]=='a' or s[i]=='E' or s[i]=='e' or s[i]=='I' or s[i]=='i' or s[i]=='U' or s[i]=='u' or s[i]=='O' or s[i]=='o' or s[i]=="O'" or s[i]=="o'":
            ans += 0
        else:
            ans += 1
        i += 1
    return ans