from PIL import Image


def getLSB(target):
    binary = str(bin(target))
    return binary[-1]


def binToAscii(bin):
    ret = ''
    length = len(bin) // 8
    for i in range(length):
        binary = bin[i*8:i*8 + 8]
        ret += chr(int(binary, 2))

    return ret


img = Image.open('Secret.png')
pixels = list(img.getdata())
mode = img.mode
ret = []

for i in range(10000):
    newPixel = list(pixels[i])
    ret.append(getLSB(newPixel[i % len(mode)]))

header, trailer = 2 * "11001100", 2 * "0101010100000000"
bin_str = ""

for b in ret:
    bin_str += b

tmp = bin_str[:bin_str.find(trailer)]
tmp = tmp.replace(header, '')

print(binToAscii(tmp))
