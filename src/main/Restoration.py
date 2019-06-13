
import imageio
import numpy
import math
import cv2
import warnings


def fourier(image):
    """implementing fourier transform"""
    img = numpy.fft.fft2(image)
    img = numpy.fft.fftshift(img)
    temp = numpy.abs(img)
    imageio.imwrite(output + 'fourier_triangle.jpg', numpy.array(temp, dtype='uint8'))
    return img


def inverse_fourier(image):
    """implementing reverse fourier transform"""
    img = numpy.fft.ifft2(image)
    temp = numpy.abs(img)
    imageio.imwrite(output + 'inverse_fourier_triangle.jpg', numpy.array(temp, dtype='uint8'))


def deg_gen(image):
    """creating the degraded version of the image"""
    space = False
    sigma = 20
    var = sigma ** 2
    shape = image.shape
    deg = []
    for i in range(shape[0]):
        temp = []
        for j in range(0, shape[1]):
            nom = distance(i, j, shape)
            factor = (-1 * nom) / (2 * var)
            temp.append(math.exp(factor))
        deg.append(temp)
    deg = numpy.asarray(deg)
    imageio.imwrite(output + 'gaussian_degradation.jpg', numpy.array(deg * 255, dtype='uint8'))

    # in case that the specs are in space domain
    if space:
        deg = numpy.fft.fft2(deg)
        deg = numpy.fft.fftshift(deg)
        deg = numpy.abs(deg)
        deg = numpy.asarray(deg)
        imageio.imwrite(output + 'gaussian_degradation.jpg', numpy.array(deg * 255, dtype='uint8'))
    return deg


def distance(u, v, shape):
    row = (u - shape[0] / 2) ** 2
    col = (v - shape[1] / 2) ** 2
    return row + col


def degradation(image, deg):
    img = numpy.fft.fft2(image)
    img = numpy.fft.fftshift(img)
    ans = img * deg
    temp = numpy.fft.ifft2(ans)
    temp = numpy.abs(temp)
    temp = numpy.array(temp, dtype='uint8')
    imageio.imwrite(output + 'triangle_degraded.jpg', temp)
    return ans


def restoration(image, deg):
    """restore the original image from the degraded one"""
    res = []
    count = 0
    for i in range(0, image.shape[0]):
        temp = []
        for j in range(0, image.shape[1]):
            with warnings.catch_warnings():
                warnings.filterwarnings('error')
                try:
                    f = image[i][j] / deg[i][j]
                except Warning:
                    count += 1
                    f = image[i][j]
                temp.append(f)
        res.append(temp)
    res = numpy.asarray(res)
    res = numpy.fft.ifft2(res)
    res = numpy.abs(res)
    res = numpy.array(res, dtype='uint8')
    imageio.imwrite(output + 'triangle_restored.jpg', res)
    print(str(count) + ' out of total ' + str(image.shape[0] * image.shape[1]) + ' were divisions handled!')
    return True


def processing():
    """processing the digital images"""

    # reading the image
    image = cv2.imread(folder + 'triangle.jpg', 0)
    imageio.imwrite(output + 'triangle.jpg', image)

    # degrading and restoring the original image
    func = deg_gen(image)
    image_degraded = degradation(image, func)
    restoration(image_degraded, func)
    return


if __name__ == '__main__':
    """main function to start the program"""
    folder = ''
    output = './bin/'
    processing()
