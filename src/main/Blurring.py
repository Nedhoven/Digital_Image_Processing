
import imageio
import numpy


def main_image():
    """creating the original binary image"""
    ans = []
    for i in range(0, 240):
        temp = [10 for _ in range(0, 240)]
        if 15 <= i <= 224:
            temp[20:27] = [240 for _ in range(0, 7)]
            temp[44:51] = [240 for _ in range(0, 7)]
            temp[68:75] = [240 for _ in range(0, 7)]
            temp[92:99] = [240 for _ in range(0, 7)]
            temp[116:123] = [240 for _ in range(0, 7)]
            temp[140:147] = [240 for _ in range(0, 7)]
            temp[164:171] = [240 for _ in range(0, 7)]
            temp[188:195] = [240 for _ in range(0, 7)]
            temp[212:219] = [240 for _ in range(0, 7)]
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(output + "binary.jpg", ans)
    return ans


def arithmetic_mean(img, i, j, size):
    """arithmetic mean filter of size x size"""
    pixel = 0.00
    factor = 1 / (size * size)
    s = int(size / 2)
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            pixel += img[m][n]
    pixel *= factor
    return pixel


def geometric_mean(img, i, j, size):
    """geometric mean filter of size x size"""
    pixel = 1.00
    factor = 1 / (size * size)
    s = int(size / 2)
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            pixel *= img[m][n]
    pixel = pixel ** factor
    return pixel


def harmonic_mean(img, i, j, size):
    """harmonic mean filter of size x size"""
    pixel = 0.00
    factor = size * size
    s = int(size / 2)
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            pixel += (1 / img[m][n])
    pixel = factor / pixel
    return pixel


def contraharmonic_mean(img, i, j, size, q):
    """contraharmonic mean filter of size x size and order of q"""
    dom = 0.00
    nom = 0.00
    s = int(size / 2)
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            dom += float(img[m][n]) ** (q + 1)
            nom += float(img[m][n]) ** q
    pixel = dom / nom
    return pixel


def median_filter(img, i, j, size):
    """median filter of size x size"""
    s = int(size / 2)
    point = int(size * size / 2)
    temp = []
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            temp.append(img[m][n])
    temp.sort()
    pixel = temp[point]
    return pixel


def max_filter(img, i, j, size):
    """maximum filter of size x size"""
    point = size * size - 1
    s = int(size / 2)
    temp = []
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            temp.append(img[m][n])
    temp.sort()
    pixel = temp[point]
    return pixel


def min_filter(img, i, j, size):
    """minimum filter of size x size"""
    point = 0
    s = int(size / 2)
    temp = []
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            temp.append(img[m][n])
    temp.sort()
    pixel = temp[point]
    return pixel


def midpoint_filter(img, i, j, size):
    """midpoint filter of size x size"""
    s = int(size / 2)
    point = size * size - 1
    pixel = 0.000
    temp = []
    for m in range(i - s, i + s + 1):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - s, j + s + 1):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            temp.append(img[m][n])
    temp.sort()
    pixel += temp[point] + temp[0]
    pixel /= 2
    return pixel


def filtering(img):
    """applying the filters to the image"""
    size1 = 3
    size2 = 7
    size3 = 9

    # arithmetic mean filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = arithmetic_mean(img, i, j, size1)
            node2 = arithmetic_mean(img, i, j, size2)
            node3 = arithmetic_mean(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "arithmetic_mean_3.jpg", ans1)
    imageio.imwrite(output + "arithmetic_mean_7.jpg", ans2)
    imageio.imwrite(output + "arithmetic_mean_9.jpg", ans3)

    # geometric mean filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = geometric_mean(img, i, j, size1)
            node2 = geometric_mean(img, i, j, size2)
            node3 = geometric_mean(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "geometric_mean_3.jpg", ans1)
    imageio.imwrite(output + "geometric_mean_7.jpg", ans2)
    imageio.imwrite(output + "geometric_mean_9.jpg", ans3)

    # harmonic mean filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = harmonic_mean(img, i, j, size1)
            node2 = harmonic_mean(img, i, j, size2)
            node3 = harmonic_mean(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "harmonic_mean_3.jpg", ans1)
    imageio.imwrite(output + "harmonic_mean_7.jpg", ans2)
    imageio.imwrite(output + "harmonic_mean_9.jpg", ans3)

    # contraharmonic mean filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = contraharmonic_mean(img, i, j, size1, 1)
            node2 = contraharmonic_mean(img, i, j, size2, 1)
            node3 = contraharmonic_mean(img, i, j, size3, 1)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "contraharmonic_mean_(1)_3.jpg", ans1)
    imageio.imwrite(output + "contraharmonic_mean_(1)_7.jpg", ans2)
    imageio.imwrite(output + "contraharmonic_mean_(1)_9.jpg", ans3)
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = contraharmonic_mean(img, i, j, size1, -1)
            node2 = contraharmonic_mean(img, i, j, size2, -1)
            node3 = contraharmonic_mean(img, i, j, size3, -1)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "contraharmonic_mean_(-1)_3.jpg", ans1)
    imageio.imwrite(output + "contraharmonic_mean_(-1)_7.jpg", ans2)
    imageio.imwrite(output + "contraharmonic_mean_(-1)_9.jpg", ans3)

    # median filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = median_filter(img, i, j, size1)
            node2 = median_filter(img, i, j, size2)
            node3 = median_filter(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "median_filter_3.jpg", ans1)
    imageio.imwrite(output + "median_filter_7.jpg", ans2)
    imageio.imwrite(output + "median_filter_9.jpg", ans3)

    # max filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = max_filter(img, i, j, size1)
            node2 = max_filter(img, i, j, size2)
            node3 = max_filter(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "max_filter_3.jpg", ans1)
    imageio.imwrite(output + "max_filter_7.jpg", ans2)
    imageio.imwrite(output + "max_filter_9.jpg", ans3)

    # min filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = min_filter(img, i, j, size1)
            node2 = min_filter(img, i, j, size2)
            node3 = min_filter(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "min_filter_3.jpg", ans1)
    imageio.imwrite(output + "min_filter_7.jpg", ans2)
    imageio.imwrite(output + "min_filter_9.jpg", ans3)

    # midpoint filtering
    ans1 = []
    ans2 = []
    ans3 = []
    for i in range(0, len(img)):
        temp1 = []
        temp2 = []
        temp3 = []
        for j in range(0, len(img[i])):
            node1 = midpoint_filter(img, i, j, size1)
            node2 = midpoint_filter(img, i, j, size2)
            node3 = midpoint_filter(img, i, j, size3)
            temp1.append(node1)
            temp2.append(node2)
            temp3.append(node3)
        ans1.append(temp1)
        ans2.append(temp2)
        ans3.append(temp3)
    ans1 = numpy.array(ans1, dtype='uint8')
    ans2 = numpy.array(ans2, dtype='uint8')
    ans3 = numpy.array(ans3, dtype='uint8')
    imageio.imwrite(output + "midpoint_filter_3.jpg", ans1)
    imageio.imwrite(output + "midpoint_filter_7.jpg", ans2)
    imageio.imwrite(output + "midpoint_filter_9.jpg", ans3)
    return


def processing():
    """processing the digital images"""
    image = main_image()
    filtering(image)
    return


if __name__ == '__main__':
    """main function to start the program"""
    output = './bin/'
    processing()
