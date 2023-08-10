#!/usr/bin/python3

def add_args(argv):
	total = 0

	for i in range(1, len(argv)):
		total += int(argv[i])

	return total

if __name__ == '__main__':
	from sys import argv
	print(add_args(argv))
