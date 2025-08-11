T = int(input())

for Tc in range(1,T+1):
    money = int(input())
    s1, s2, s3, s4, s5, s6, s7, s8 =  0, 0, 0, 0, 0, 0, 0, 0 
    while money >= 50000:
        s1 +=1
        money -= 50000
    while money >= 10000:
        s2 +=1
        money -= 10000
    while money >=5000:
        s3 +=1
        money -= 5000
    while money >=1000:
        s4 +=1
        money -= 1000
    while money >=500:
        s5 +=1
        money -= 500
    while money >= 100:
        s6 +=1
        money -= 100
    while money >= 50:
        s7+=1
        money -= 50
    while money >= 10:
        s8+=1
        money -= 10
    print(f'#{Tc}')
    print(s1, s2, s3, s4, s5, s6, s7, s8)