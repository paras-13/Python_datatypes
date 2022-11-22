#Pattern programming with strings in python
'''
Demo Eg:-
P        N
  Y    O
    TH
'''
# Code -->

stri='PYTHON'
column=6
a,s=0,5
for i in range(column-3):
	for j in range(column):
		if j==a or j==s:
			print(stri[j],end=' ')
		else:
			print(' ',end=' ')
	a,s=a+1,s-1
	print()