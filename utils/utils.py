def read(path):
    raw_data = None
    values = []

    with open(path) as f:
        raw_data = f.read()

    elements = raw_data.split(',')
    for e in elements:
        v = e.split(':')[-1].replace('(', '')
        v = v.replace(')', '')
        values.append(float(v))
    return values


def write(path, values):
    max_frames = len(values)
    with open(path, mode='w') as f:
        for i in range(max_frames):
            s = "{}:({}),".format(i, values[i])
            f.write(s)


def mul(values, a):
    _values = []
    for v in values:
        _value = a * v
        _values.append(_value)
    return _values


def invert(values):
    inv_values = []
    for v in values:
        inv_value = -1.0 * v
        inv_values.append(inv_value)
    return inv_values
