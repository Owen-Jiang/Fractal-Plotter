import random
import os

resolution = 0.01
bounds = (-1, 1, -1, 1)
cmap = {False: " ", True: "■"}

def mandelbrot(c):
	return lambda z: z ** 2 + c

def julia(c=0+0*1j):
	return lambda z: z ** 2 + c

def iterate(set_function, n, z=0):
	for _ in range(n):
		z = set_function(z)
	return z

def converges(c, set_function, iter=9, bound=10 ** 0.15):
	try:
		return abs(iterate(set_function(c), iter)) < bound # Mandelbrot
	except:
		return abs(iterate(set_function, iter, c)) < bound # Julia

def draw(set_function):
	space = [[True if converges((x*resolution+bounds[0]) + (y*resolution+bounds[2])*1j, set_function) else False for x in range(int((bounds[1] - bounds[0]) / resolution))] for y in range(int((bounds[3] - bounds[2]) / resolution))]
	graph(space)

def graph(space):
	os.system("clear")
	print("\n".join("  ".join(cmap[point] for point in space[len(space) - line - 1]) for line in range(len(space))))

draw(julia(-0.835 - 0.2321*1j))
draw(julia(-0.7269 + 0.1889j))
draw(julia(1 - (1 + 5 ** 0.5) / 2))
draw(mandelbrot)