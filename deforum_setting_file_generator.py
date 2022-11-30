import os
import argparse


def import_file_data(path):
    _ = ""
    with open(path) as f:
        _ = f.read()

    return _


def generate_setting_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template',
                        required=True, type=str)
    parser.add_argument('-o', '--out_path',
                        type=str, default='./out.txt')
    parser.add_argument('-a', '--attributes',
                        required=True, nargs="*", type=str)
    parser.add_argument('-k', '--keyframe_data',
                        required=True, nargs="*", type=str)

    args = parser.parse_args()
    keyframe_data = []

    for k in args.keyframe_data:
        keyframe_data.append("\"" + import_file_data(k) + "\n")

    raw = ""
    with open(args.template) as f:
        for line in f:
            is_keyframe_data = False
            for i, attr in enumerate(args.attributes):
                if (attr in line):
                    raw += line.replace("\n", "") + \
                        keyframe_data[i].replace("\n", "") + "\"" + ","
                    is_keyframe_data = True
            if is_keyframe_data == False:
                raw += line
    generate_setting_file(args.out_path, raw)
