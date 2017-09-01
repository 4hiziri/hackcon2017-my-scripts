def to_string(list):
    ret = ""
    for c in list:
        ret += c

    return ret


def decode(cipher, dec):
    ret = ''

    for c in cipher:
        if c in dec.keys():
            ret += dec[c]
        else:
            ret += c

    return ret


def mkhist(sentense):
    hist = {}
    for i in range(ord('A'), ord('Z') + 1):
        hist[chr(i)] = 0

    for c in sentense:
        if c in hist.keys():
            hist[c] += 1

    return hist
