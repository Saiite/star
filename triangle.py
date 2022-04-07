#coding:utf-8
n= int(input ("veillez saisir le nombre de ligne :"))

x=2*(n>1)

for i in range(1,8*n,2):
            print(str('*'*[i,8*n-i-x][i+x>n*6 or i//n//2%2 ]).center(6*n))
           
