n,k=map(int,input().split())
aList=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n):
        # 拼一下数啊
        s1=str(i)+str(j)
        s2=str(j)+str(i)
        if int(s1) % k==0:
            print(s1)
            c+=1
        if  int(s2)%k==0:
            print(s2)
            c+=1

print(c)
     
        
        
        
