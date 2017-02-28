def remove_dups_noneclone(L1, L2):
	for e1 in L1:
		print(e1)
		if e1 in L2:
			L1.remove(e1)

def remove_dups(L1, L2):
	for e1 in L1[:]: #extra colon makes it use an copy of L1, not the "removed" one
		print(e1)
		if e1 in L2:
			L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)