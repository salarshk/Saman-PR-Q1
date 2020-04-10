import numpy
import random
N=1000000
n1=26
m1=2
n2=52
m2=4
d1=np.zeros([N,1])
d2=np.zeros([N,1])
for i in range(N):
    p1=0
    a = [j+1 for j in range(n1)]
    random.shuffle(a)
    for k in range(1,n1):
        a_temp=a[k-1]
        if (a[k]>n1/m1 and a_temp>n1/m1) or (a[k]<=n1/m1 and a_temp<=n1/m1):
            p1=p1+1
            
    d1[i]=p1
    p2=0
    b = [j+1 for j in range(n2)]
    random.shuffle(b)
    for k in range(1,n2):
        b_temp=b[k-1]
        if (b[k]>((m2-1)*n2/m2) and b_temp>((m2-1)*n2/m2)) or (b[k]<=n2/m2 and b_temp<=n2/m2) or (((m2-2)*n2/m2)<b[k]<=((m2-1)*n2/m2) and ((m2-2)*n2/m2)<b_temp<=((m2-1)*n2/m2)) or (((m2-3)*n2/m2)<b[k]<=((m2-2)*n2/m2) and ((m2-3)*n2/m2)<b_temp<=((m2-2)*n2/m2)):
            p2=p2+1
            
    d2[i]=p2
print("the mean of P when N = 26 and M = 2 is:")    
print(np.mean(d1))    
print("the Standard Deviation of P for N = 26 and M = 2 is:")
print(np.std(d1))
print("the conditional probability that P > 12 given that it's P > 6 when N = 26 and M = 2 is:")
pr1=sum(d1>12)/sum(d1>6)
print(pr1)
print("the mean of P when N = 52 and M = 4 is:")    
print(np.mean(d2))    
print("the Standard Deviation of P for N = 52 and M = 4 is:")
print(np.std(d2))
print("the conditional probability that P > 12 given that it's P > 6 when N = 52 and M = 4 is:")
pr2=sum(d2>12)/sum(d2>6)
print(pr2)