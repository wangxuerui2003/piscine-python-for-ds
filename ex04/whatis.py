import sys

try:
	assert len(sys.argv) <= 2, "more than one argument is provided"
except AssertionError as e:
	print("AssertionError:", e)
	sys.exit()

if len(sys.argv) < 2:
	sys.exit()

try:
	num = int(sys.argv[1])
	print("I'm Even" if num % 2 == 0 else "I'm Odd")
except:
	print("AssertionError:", "argument is not an integer")

