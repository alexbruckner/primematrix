#!/usr/bin/env python
import sys, os, time


from primes import generate_divisor_list,color_print
from matrix import Matrix


def traverse(matrix, map, level = 0, key_color = None):
	for key, value in map.items():
		x = matrix.get_x(key)

		if key_color:
			color = key_color
		else:
			color = matrix.reversed_colors[matrix.FORES[x % 7]];	
		
		m.add_color(x, level, 'X', color)

		new_level = level + 1
		try:
			traverse(matrix, value, new_level, color)
		except:
			pass



if __name__ == "__main__":
	integer = 0
	timeout = 1
	if len(sys.argv) > 1:
		integer = int(sys.argv[1]) 
	if len(sys.argv) > 2:
		timeout = int(sys.argv[2]) 

	divisor_list = generate_divisor_list(integer)

	if timeout > 0:
		for integer, divisors in enumerate(divisor_list):
			if integer < 2: continue;
			os.system('cls');
			
			print integer, divisors	
			print	
		
			m = Matrix(25,4)
			traverse(m, divisors)	
	
			m.display() 
			time.sleep(timeout)	
	else:
		divisors = divisor_list[integer]
		print integer, divisors	
		print	
		
		m = Matrix(25,4)
		traverse(m, divisors)	
	
		m.display() 
		

