# takes list of nums and operators, no parentheses
def eval(c):
    a = []
    # E
    for j in range(len(c)):
        if j == 0:
            a.append(c[j])
        elif c[j-1] == "**" or c[j-1] == "^":
            pass
        elif c[j] == "**" or c[j] == "^":
             new = float(a.pop(-1)) ** float(c[j+1])
             a.append(new)
        else:
            a.append(c[j])
    # M
    b = []
    for j in range(len(a)):
        if j == 0:
            b.append(a[j])
        elif a[j-1] == "*" or a[j-1] == "/":
            pass
        elif a[j] == "*":
             new = float(b.pop(-1)) * float(a[j+1])
             b.append(new)
        elif a[j] == "/":
             new = float(b.pop(-1)) / float(a[j+1])
             b.append(new)
        else:
            b.append(a[j])
    # A
    d = []
    for j in range(len(b)):
        if j == 0:
            d.append(b[j])
        elif b[j-1] == "+" or b[j-1] == "-":
            pass
        elif b[j] == "+":
             new = float(d.pop(-1)) + float(b[j+1])
             d.append(new)
        elif b[j] == "-":
             new = float(d.pop(-1)) - float(b[j+1])
             d.append(new)
        else:
            d.append(b[j])
    return float(d[0])

def calc(i):
    clean = ""
    for j in range(len(i)):
        ch = i[j]
        # exponents
        if ch == "*":
            if j != (len(i) - 1) and i[j+1] == "*":
                clean += (" ** ")
            elif j != 0 and i[j-1] == "*":
                pass
            else:
                clean += " * "
        elif ch in "()-+/^":
            clean += (" " + ch + " ")
        else:
            clean+= ch
    c = clean.split()
    # P
    if "(" in c:
        ans,stack = [],[]
        for j in range(len(c)):
            if c[j] == "(":
                stack.append(j)
                ans.append(c[j])
            elif c[j] == ")":
                start = stack.pop(-1)
                # last index
                last = len(ans) - 1 - ans[::-1].index("(")
                ans = ans[:last]
                ans.append(eval(c[start+1:j]))
            else:
                ans.append(c[j])
        print(eval(ans))
    else:
        print(eval(c))

def run():
    while True:
        print("Enter input or quit to quit: ")
        i = input().strip().lower()
        if i == "quit":
            break
        else:
            calc(i)

run()
