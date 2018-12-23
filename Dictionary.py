from itertools import permutations
from urllib.request import urlopen as ureq
my_url='https://drive.google.com/file/d/170ja5hf4EMSeY9etVx7A5gDgiOQ_PIME/view?usp=sharing'
client=ureq(my_url)
dump= client.read()
client.close()
i=0
Final=[]
pe_list=[]
items=input()
z=len(items)
for L in range(1,z+1):
	perms = [''.join(p) for p in permutations(items,L)]
	pe_list=pe_list+perms
	L=L+1
#print(set(perms).intersection(dump))

for p in pe_list:
	for T in dump:
		if(p==T):
			print(T)