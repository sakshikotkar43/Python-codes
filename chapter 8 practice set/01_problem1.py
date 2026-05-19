def greatest():
    a = int(input())
    b = int(input())
    c = int(input())

    if(a>b and a>c):
        return f"{a} is greatest"

    elif(b>a and b>c):
        return f"{b} is greatest"
    else:
        return f"{c} is greatest"

print(greatest())