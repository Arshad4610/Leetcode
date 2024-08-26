n=int(input())
s=input().strip()
m=0
res=''
for i in range(len(s)):
    for j in range(i,n):
        p=s[i:j+1]
        if(p==p[::-1]):
            if len(p)>m:
                m=len(p)
                res=p
print(m)
print(res)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
OUTPUT:
  Sample Input
    5
    abbba
  Your Output
    5
    abbba
