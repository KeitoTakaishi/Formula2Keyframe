import os


def import_file_data(path):
    _ = ""
    with open(path) as f:
        _ = f.read()

    return _


if __name__ == "__main__":
    pos_x = "\"" + import_file_data("./out/out_posx.txt") + "\""
    pos_y = "\"" + import_file_data("./out/out_posy.txt") + "\""
    rot_z = "\"" + import_file_data("./out/out_rotz.txt") + "\""

    raw = ""
    with open('./template.txt') as f:
        for line in f:
            raw += line
            if ("translation_x" in line):
                raw += line+pos_x
            elif ("translation_y" in line):
                raw += line+pos_y
            elif ("rotation_3d_z" in line):
                raw += line+rot_z

    print(raw)
