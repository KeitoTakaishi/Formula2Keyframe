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
    y = np.sqrt(1 - np.power(x - 1, 2)) * amp
    return y


def easeOutQuart(x, amp):
    y = 1 - np.power(1 - x, 4) * amp
    return y


def easeOutExpo(x, amp):
    y = np.where(x == 1.0, 1.0, 1 - np.power(2.0, -10.0 * x)) * amp
    return y
