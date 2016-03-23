numbers = []

def add_while_end(i, num, plus):
	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + plus
		print "numbers now: ", numbers
		print "At the bottom i is %d" % i

add_while_end(5, 50, 10)


print "The numbers: "

for num in numbers:
    print num
