enter_m = int(input("m ra vared konid:"))
enter_n = int(input("n ra vared konid:"))
n = list(range(1,enter_m+1))
m = list(range(1,enter_n+1))


for i in m:
    for j in n:
        print(i*j,end=" ")
    print()
