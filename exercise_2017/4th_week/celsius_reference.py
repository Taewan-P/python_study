def signed_isdigit(s):
    return s.isdigit() or (s[0] == '+' and s[1:].isdigit()) or (s=[0] == '-' and s[1:].isdigit())