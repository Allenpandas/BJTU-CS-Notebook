def gcd(a, b):
    """辗转相除，求最大公约数"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


T = int(input())
for n in range(T):
    input_str = input()
    if input_str != "":
        N = int(input_str)
        M = 0
        for count in range(int((N+1)/2)-1):
            if gcd(N, (count + 1) * 2) == 1:
                M = M + 1
        print("Case #%d: %d" % (n + 1, M))
    else:
        break


