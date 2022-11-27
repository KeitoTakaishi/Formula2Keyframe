import os
import re
import numpy as np
from matplotlib import pyplot
import math
import utils.easing as easing
import utils.utils as utils

import argparse


def two_mix(x, max_frame):
    threshold = max_frame/2.0
    y = []
    for i in range(max_frame+1):
        if i <= threshold:
            x = i/threshold
            _y = 1.0 - pow(1.0 - x, 3.0)
            y.append(_y * 3.0)
        else:
            x = (i-threshold)/threshold
            #y.append(pow(1.0 - (i-threshold)/threshold, 3.0))
            _y = (1.0 - np.sqrt(1 - pow(x - 1, 2)))
            _y = _y - 1.0
            y.append(_y * 3.0)
    return y


def repeat_easing(x, freq: float, amp, offsets, ease_type):
    
    _x = np.where(x == 1.0, 1.0, x*freq - np.floor(x*freq))
    #_x = x*freq - np.floor(x*freq)
    #_x = np.fmod(_x + offsets, 1.0) 
    print(_x)
    

    if ease_type == 'easeOutSine':
        y = easing.easeOutSine(_x, amp)
    elif ease_type == 'easeOutCubic':
        y = easing.easeOutCubic(_x, amp)
    elif ease_type == 'easeInCirc':
        y = easing.easeInCirc(_x, amp)
    elif ease_type == 'easeOutQuart':
        y = easing.easeOutQuart(_x, amp)
    elif ease_type == 'easeOutExpo':
        y = easing.easeOutExpo(_x, amp)
    else:
        return
    return y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_path")
    parser.add_argument("--amp", default=3.0, type=float)
    parser.add_argument("--max_frames", default=60, type=float)
    parser.add_argument("--freq", default=5.0, type=float)
    parser.add_argument("--offset", default=0.0, type=float)
    parser.add_argument("--preview", action='store_true')
    parser.add_argument("--easing", default='easeOutCubic')


    args = parser.parse_args()

    # ----------------------------------------------------------------------------
    # path = './motion_preset.txt'
    # values = read(path)
    # values = mul(values, 2.0)
    # values = invert(values)

    out_path = args.out_path
    max_frame = args.max_frames
    freq = args.freq
    amp = args.amp
    offset = args.offset
    ease_type = args.easing
    # ----------------------------------------------------------------------------
    x = np.linspace(0, max_frame, max_frame+1)

    nx = x / (max_frame)
    print(nx)
    offsets = np.ones(x.shape) * offset
    

    y = repeat_easing(nx, freq, amp, offsets, ease_type)

    #y = two_mix(x, max_frame)
    utils.write(out_path, y)

    if args.preview:
        pyplot.plot(nx, y)
        pyplot.show()
