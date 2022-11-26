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


def repat_easing(x, n, amp):
    _x = x*n - np.floor(x*n)
    y = easing.easeInCirc(_x, amp)
    return y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_path")
    parser.add_argument("--amp", default=3.0)
    parser.add_argument("--max_frames", default=120)
    parser.add_argument("--freq", default=5.0)
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
    # ----------------------------------------------------------------------------
    x = np.linspace(0, max_frame, max_frame+1)
    nx = x / max_frame
    y = repat_easing(nx, freq, amp)

    #y = two_mix(x, max_frame)
    utils.write(out_path, y)

    pyplot.plot(nx, y)
    pyplot.show()
