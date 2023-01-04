def printnumber(n):
    for n in range(n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)

printnumber(1000)