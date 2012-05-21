from colorama import init, Fore, Back, Style
from primes import get_prime_list
init(autoreset=True)

colors = {'red': Fore.RED, 'white': Fore.WHITE, 'magenta':Fore.MAGENTA, 'cyan': Fore.CYAN, 'blue': Fore.BLUE, 'green': Fore.GREEN, 'yellow': Fore.YELLOW}
style = Back.BLACK + Style.BRIGHT

class Matrix(object):
    FORES = [colors['red'], colors['white'], colors['magenta'], colors['cyan'], colors['blue'], colors['green'], colors['yellow']]
    reversed_colors = dict((v,k) for k, v in colors.iteritems())
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.content = ['{blue}O{white}'] * self.size
	self.label_y = range(height)
	self.label_x = get_prime_list(self.size)

    def set_point(self, x, y, value):
        self.check_bounds(x, y)
        self.content[y * self.width + x] = value
    def set_color(self, x, y, value, color):
	self.set_point(x, y, '{%s}%s{%s}' % (color, value, 'white')) 
    def add_color(self, x, y, value, color):
	self.set_point(x, y, '%s{%s}%s{%s}' % (self.get_point(x, y).replace('{blue}O{white}',''), color, value, 'white'))
    def get_point(self, x, y):
        self.check_bounds(x, y)
        return self.content[y * self.width + x]
    def __str__(self):
        return str(self.content)
    def check_bounds(self, x, y):
        if x >= self.width or y >= self.height:
            raise Exception('out of bounds')
    def display(self):
        l = []
        rows = self.height
	   
	for i in xrange(self.size - 1, -1, -1):
            l.insert(0, self.content[i])
            if i % self.width == 0:
		rows -= 1
		s = str(l)
		for key, value in colors.items():
 			s = s.replace('{%s}' % key, colors[key] + style)
          	print Fore.GREEN+'{0:02}'.format(self.label_y[rows])+Fore.WHITE, s.replace('\'','').replace(',','  '),
                l = []
                print
	print
	print '   ',
	for i, prime in enumerate(self.label_x):
		if i >= self.width: break
		print '%s%s ' % (self.FORES[i%7], '{0:02}'.format(prime)),	
    def get_x(self, prime):
	    return [i for i,x in enumerate(self.label_x) if x == prime][0]
	


if __name__ == "__main__":
	m = Matrix(5, 4)
	m.set_color(4, 3, 1, 'red')
	m.set_color(0, 0, 2, 'green')
	m.display() 

