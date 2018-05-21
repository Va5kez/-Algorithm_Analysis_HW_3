import random

final = [None]*20

def hashing(array):
    size = len(array)
    f = 0
    while f < size:
        hash(array[f], size)
        f+=1
    return final

def hash(element, size):
    a = random.randint(1, size*4)
    b = random.randint(1, size*4)
    c = next_prime(size*2)
    pos = (a*element + b) % c
    if pos < len(final):
        if final[pos] is None:
            final[pos] = element
        else:
            hash(element, size)
    else:
        hash(element, size)

def next_prime(number):
    while True:
		number += 1
		if number < 2:
			continue
		if number == 2:
			break
		if number % 2 == 0:
			continue
		flag = False
		i = 3
		while (i * i) <= number:
			if number % i == 0:
				flag = True
				break
			i += 2
		if not flag:
			break
    return number
