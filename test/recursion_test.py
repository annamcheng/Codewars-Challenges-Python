def mel(n, m):
    if n == 1:
        return m
    else:
        return m + mel(n-1, m)

n = 4
m = 5

print(mel(n, m))

x = 1234
def digit_num(x):
    if x < 10:
        return 1
    else:
        return 1+digit_num(x//10)
            #  1+ digit_num(123)
                # 1 + digit_num(12)
                    # 1 + digit_num(1)


def reverse(x):
    if x < 10:
        return x
    else:
        return (x%10)*(10**(digit_num(x)-1)) + reverse(x//10)
                # 4   * (10**3) + reverse(123)           # 4000 + 321 = 4321
                #        3 * (10**2) + reverse(12)       # 300 + 21 = 321
                #             2 * (10**1) + reverse(1)   # 20 + 1 = 21
print(reverse(x))

print()