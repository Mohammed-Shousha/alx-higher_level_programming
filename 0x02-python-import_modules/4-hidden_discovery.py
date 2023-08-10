#!/usr/bin/python3

def discover(module):
	names = dir(module)
	for name in names:
		if name[:2] != '__':
			print(name)

if __name__ == '__main__':
	import hidden_4
	discover(hidden_4)

