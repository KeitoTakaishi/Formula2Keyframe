# https://easings.net/
import numpy as np
import math


def easeOutSine(x, amp):
    y = np.sin((x * math.pi) / 2) * amp
    return y


def easeOutCubic(x, amp):
    y = np.sin((x * math.pi) / 2) * amp
    return y


def easeInCirc(x, amp):
    #y = 1 - np.sqrt(1 - math.pow(x, 2))
    y = np.sqrt(1 - np.power(x - 1, 2)) * amp
    return y
