import sys
from colorama import init, Fore, Back, Style
def get_prime_list(max_number):
    #create some constants
    max_plus_1 = max_number + 1
    max_plus_1_div_2 = max_plus_1 / 2;

    #create list of integers
    integers = []
    for position in xrange(max_plus_1):
        integers.append(position)

    #set non-prime integers to divisor tuples
    for factor in xrange(2, max_plus_1_div_2):
        next_position = factor + factor
        while next_position < max_plus_1:
            integers[next_position] = 0
            next_position += factor

    return_list = []
    for prime in integers:
	    if prime != 0:
		    return_list.append(prime)

    return return_list[1:]
    

def generate_divisor_list(max_number):
    #create some constants
    max_plus_1 = max_number + 1
    max_plus_1_div_2 = max_plus_1 / 2;

    #create list of integers
    integers = []
    for position in xrange(max_plus_1):
        integers.append(position)

    #set non-prime integers to divisor tuples
    for factor in xrange(2, max_plus_1_div_2):
        next_position = factor + factor
        while next_position < max_plus_1:
            integers[next_position] = (integers[factor], integers[next_position / factor])
            next_position += factor

    #add the divisors up to represent them as powers in a map
    for position in xrange(max_plus_1):
	position_integers = to_map(integers[position])
	for key, value in position_integers.items():
			if value == 1: continue
			position_integers[key] = integers[value]
	integers[position] = position_integers
	    


    return integers

def to_list(tuples):
    as_list = []
    _to_list(tuples, as_list)
    return as_list

def _to_list(tuples, as_list=[]):
    try:
        for elem in tuples:
            _to_list(elem, as_list)
        return as_list
    except TypeError:
        as_list.append(tuples)

def to_map(tuples):
    as_map = {}
    as_list = to_list(tuples)
    for elem in as_list:
        if as_map.get(elem):
            as_map[elem] = as_map[elem] + 1
        else:
            as_map[elem] = 1
    return as_map



def decorate(item):
	return str(item).replace('{','{' + Fore.GREEN + Back.BLACK + Style.BRIGHT).replace(':',Fore.WHITE + Back.BLACK + Style.BRIGHT+':').replace(', ', ', ' + Fore.GREEN + Back.BLACK + Style.BRIGHT)

def color_print(integer):
	init(autoreset=True)
	for i, item in enumerate(generate_divisor_list(integer)):
		normal_prefix = Fore.WHITE + Back.BLACK + Style.BRIGHT
		prime_prefix = Fore.RED + Back.BLACK + Style.BRIGHT
		div24_prefix = Fore.MAGENTA + Back.BLACK + Style.BRIGHT
		div6_prefix = Fore.YELLOW + Back.BLACK + Style.BRIGHT

		prefix = normal_prefix
	
		if i > 1:
			if len(item.items()) == 1 and item.items()[0][1] == 1:
				prefix = prime_prefix	
			if i % 6 == 0:
				prefix = div6_prefix
			if i % 24 == 0:
				prefix = div24_prefix


		divisors_prefix = Fore.BLUE + Back.BLACK + Style.BRIGHT
 
		print prefix + '%s' % i, decorate(item), divisors_prefix + '%s' % item.keys()



if __name__ == "__main__":
	integer = 0
	if len(sys.argv) > 1:
		integer = int(sys.argv[1]) 
	color_print(integer)



