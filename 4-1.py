fibs=[0,1]
num=input()
while True:
    fibs.append(fibs[-2]+fibs[-1])
    if fibs[-1]>num:
        fibs.pop(-1)
        break

total=0
for x in fibs :
    if x%2==0:
        total+=x
print total