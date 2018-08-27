"""
Created on Fri Aug 24 13:15:57 2018
Author:Aravind Rajeev
"""

from itertools import combinations_with_replacement
inp = input()
string=""
comb=[]
for i in range(0,len(inp)-1):
  if(inp[i] != " "):
      string+=inp[i]
num=int(inp[i+1])  
comb=list(combinations_with_replacement(string,num))
comb=[list(item) for item in comb]
for i in range(0,len(comb)):
    for k in range(0,num):
        for j in range(1,num):
            if(comb[i][j-1]>comb[i][j]):
                temp=comb[i][j-1]
                comb[i][j-1]=comb[i][j]
                comb[i][j]=temp     
comb.sort()
for j in range (0,len(comb)):
    for i in range (0,num):
        print(comb[j][i],sep='',end='')
        
    print() 