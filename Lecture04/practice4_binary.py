x = 250000
epsilon = 0.01
step = epsilon**2
num_guesses = 0
low= 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
	print ('low =', low, 'high =', high, 'ans =',ans)
	num_guesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans

	ans = (high + low)/2.0

print ("num_guesses =", num_guesses)

print (ans, 'is close to square root of ', x)

