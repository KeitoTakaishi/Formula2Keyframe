import argparse
import math
import os

parser = argparse.ArgumentParser()

parser.add_argument('--f', default="math.sin(t)")
parser.add_argument('--max', default=120)
parser.add_argument('--out', default='./motion.txt')
args = parser.parse_args()

base_formula = args.f
max_frame = args.max
out_path = args.out
print(out_path)


if not os.path.exists(out_path):
    # os.remove(out_path)
    print('test')
    f = open(out_path, 'w')
    f.close()


with open(out_path, mode='a') as f:
    for i in range(max_frame+1):
        #y = eval(formula)
        # pow(1.0,1.0)
        y = math.sin(i)
        s = "{}:{},".format(i, y)
        f.write(s)
