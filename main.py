import os
import re
import numpy as np
from matplotlib import pyplot as plt
import math
import utils.easing as easing
import utils.noise as noise
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


def repeat_easing(x, args):
    if args.ease_loop:
        _x = x*args.freq - np.floor(x*args.freq)
    else:
        _x = np.where(x == 1.0, 1.0, x*freq - np.floor(x*freq))
    #_x = np.fmod(_x + offsets, 1.0)
    if args.easing == 'easeOutSine':
        y = easing.easeOutSine(_x, args.amp)
    elif args.easing == 'easeOutCubic':
        y = easing.easeOutCubic(_x, args.amp)
    elif args.easing == 'easeInCirc':
        y = easing.easeInCirc(_x, args.amp)
    elif args.easing == 'easeOutQuart':
        y = easing.easeOutQuart(_x, args.amp)
    elif args.easing == 'easeOutExpo':
        y = easing.easeOutExpo(_x, args.amp)
    elif args.easing == 'easeInQuint':
        y = easing.easeInQuint(_x, args.amp)
    else:
        pass
    return y


def noise2keyframe(x, args):
    sample_num = len(x)
    noise_values = np.zeros((sample_num))

    for i in range(args.noise_loop):
        w = pow(2, (i+1))
        values = np.array([[noise.Perlin.noise(x, y)
                            for x in np.linspace(0, w, 1)]
                           for y in np.linspace(0, w, sample_num)])
        values = values.squeeze() + 0.5
        #noise_values = noise_values + values
        noise_values = values
    noise_values = (noise_values / args.noise_loop)*20.0*args.amp

    return noise_values


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_path")
    parser.add_argument("--formula_type", default='noise',
                        choices=["easing", "noise"])
    parser.add_argument("--max_frames", default=120, type=int)
    parser.add_argument("--amp", default=3.0, type=float)
    parser.add_argument("--easing", default='easeOutCubic')
    parser.add_argument("--freq", default=5.0, type=float)
    parser.add_argument("--min_value", default=0.0, type=float)
    parser.add_argument("--offset", default=0.0, type=float)
    parser.add_argument("--noise_loop", default=4, type=int)
    parser.add_argument("--ease_loop", action='store_true')
    parser.add_argument("--preview", action='store_true')

    args = parser.parse_args()
    out_path = args.out_path
    max_frame = args.max_frames
    formula_type = args.formula_type

    # noise
    # easing
    ease_type = args.easing
    freq = args.freq
    amp = args.amp
    min_value = args.min_value
    offset = args.offset

    # ----------------------------------------------------------------------------
    x = np.linspace(0, max_frame, max_frame+1)
    nx = x / (max_frame)
    keyframe_values = np.zeros(max_frame+1)

    if formula_type == "easing":
        keyframe_values = repeat_easing(nx, args)
    elif formula_type == "noise":
        keyframe_values = noise2keyframe(nx, args)

    keyframe_values = [utils.map_value(
        y_, 0.0, amp, min_value, amp) for y_ in keyframe_values]
    keyframe_values = np.round(keyframe_values, 3)
    utils.write(out_path, keyframe_values)

    if args.preview:
        plt.plot(nx, keyframe_values)
        plt.show()
