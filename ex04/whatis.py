import sys

assert len(sys.argv) <= 2, "more than one argument is provided"

if len(sys.argv) < 2:
	sys.exit()

try:
	num = int(sys.argv[1])
	print("I'm Even" if num % 2 == 0 else "I'm Odd")
except:
	assert False, "argument is not an integer"

