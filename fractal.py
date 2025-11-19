import random
import os
import math

zoom = 1
resolution = 0.005
bounds = (-1.4, -0.4, 0, 0.5)
cmap = {False: "⋅", True: "⬤"}
center = ((bounds[0] + bounds[1]) / 2, (bounds[2] + bounds[3]) / 2)

resolution /= zoom
bounds = (center[0] - (bounds[1] - bounds[0]) / (2 * zoom),
		  center[0] + (bounds[1] - bounds[0]) / (2 * zoom), 
		  center[1] - (bounds[3] - bounds[2]) / (2 * zoom),
		  center[1] + (bounds[3] - bounds[2]) / (2 * zoom))

def mandelbrot(c):
	return lambda z: z ** 2 + c

def julia(c=0+0*1j):
	return lambda z: z ** 2 + c

def iterate(set_function, n, z=0):
	for _ in range(n):
		z = set_function(z)
	return z

def converges(c, set_function, iter=50, bound=2, conv='normal'):
	try:
		f, z = (set_function(c), 0) if callable(set_function(c)) else (set_function, c)
	except:
		f, z = set_function, c
	prev = 0
	for i in range(iter):
		z = f(z)
		if abs(z) > bound: # type: ignore
			return i if conv == 'normal' else i + 1 - math.log(math.log(abs(z))) / math.log(2)
		prev = z

	return iter

	# old version
	# try:
	# 	return abs(iterate(set_function(c), iter)) < bound # Mandelbrot
	# except:
	# 	return abs(iterate(set_function, iter, c)) < bound # Julia

def draw(set_function):
	# True or False
	# space = [[True if converges((x*resolution+bounds[0]) + (y*resolution+bounds[2])*1j, set_function, conv="normal") else False for x in range(int((bounds[1] - bounds[0]) / resolution))] for y in range(int((bounds[3] - bounds[2]) / resolution))]

	# Color gradient
	space = [[converges((x*resolution+bounds[0]) + (y*resolution+bounds[2])*1j, set_function, conv="fancy") for x in range(int((bounds[1] - bounds[0]) / resolution))] for y in range(int((bounds[3] - bounds[2]) / resolution))]

	graph(space)

def graph(space):
	os.system("clear")

	# True or False
	# print("\n".join("  ".join(cmap[point] for point in space[len(space) - line - 1]) for line in range(len(space))))

	# Color gradient
	max_iter = max(max(row) for row in space)

	def color(i):
		if i == max_iter:
			return f"\033[38;5;16m{cmap[True]}\033[0m"
		ansi = 17 + int((i / max_iter) * 200)
		return f"\033[38;5;{ansi}m{cmap[True]}\033[0m"

	print("\n".join("  ".join(color(point) for point in space[len(space) - line - 1]) for line in range(len(space))))

for a in range(1000):
	draw(julia(-0.835 + a/1000 - a/1000*1j))
# draw(julia(-0.835 - 0.2321*1j))
# draw(julia(-0.7269 + 0.1889j))
# draw(julia(-0.835 - 0.2321*1j))
# draw(mandelbrot)
