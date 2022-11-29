# https://yuki67.github.io/post/perlin_noise/
from math import floor
from itertools import product
import numpy as np
import matplotlib.pyplot as plt

def lerp(a, b, t):
    return a + (b - a) * t

class Perlin():
    slopes = 2 * np.random.random((256, 2)) - 1
    rand_index = np.zeros(512, dtype=np.int8)
    for i, rand in enumerate(np.random.permutation(256)):
      rand_index[i] = rand
      rand_index[i + 256] = rand

    @staticmethod
    def hash(i, j):
        return Perlin.rand_index[Perlin.rand_index[i] + j]

    @staticmethod
    def fade(x):
        return 6 * x**5 - 15 * x ** 4 + 10 * x**3

    @staticmethod
    def weight(ix, iy, dx, dy):
        ix %= 256
        iy %= 256
        ax, ay = Perlin.slopes[Perlin.hash(ix, iy)]
        return ax * dx + ay * dy

    @staticmethod
    def noise(x, y):
        ix = floor(x)
        iy = floor(y)
        dx = x - floor(x)
        dy = y - floor(y)

        w00 = Perlin.weight(ix,     iy,   dx  , dy)
        w10 = Perlin.weight(ix+1,   iy, dx-1,   dy)
        w01 = Perlin.weight(ix,   iy+1,   dx, dy-1)
        w11 = Perlin.weight(ix+1, iy+1, dx-1, dy-1)

        wx = Perlin.fade(dx)
        wy = Perlin.fade(dy)

        
        y0 = lerp(w00, w10, wx)
        y1 = lerp(w01, w11, wx)
        return (lerp(y0, y1, wy) - 1) / 2 