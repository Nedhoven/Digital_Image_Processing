
import cv2
import imageio
import numpy
import scipy.ndimage.filters as ned


def frequency(img, name):
    """implementing shifted Fourier transform for images"""
    ans = numpy.fft.fft2(img)
    ans = numpy.fft.fftshift(ans)
    ans = 20 * numpy.log(numpy.abs(ans))
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(name, ans)
    return ans


def padding(img, name):
    """padding to have the final image as the same size as the input"""
    ans = []
    flag1 = False
    for i in range(-1, len(img) + 1):
        flag2 = False
        if flag1:
            break
        if i == len(img):
            i = 0
            flag1 = True
        temp = []
        for j in range(-1, len(img[0]) + 1):
            if flag2:
                break
            if j == len(img[0]):
                j = 0
                flag2 = True
            temp.append(img[i][j])
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(name, ans)
    return ans


def filter_sharpen(img, name):
    """sharpening the image by subtracting the derivative from the original"""
    ans = []
    for i in range(1, len(img) - 1):
        temp = []
        for j in range(1, len(img[0]) - 1):
            node = sharpen(img, i, j)
            temp.append(node)
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(name, ans)
    return ans


def filter_derivative(img, name):
    """implementation of SciPy library, ndImage, filters, laplace"""
    ans = []
    for i in range(1, len(img) - 1):
        temp = []
        for j in range(1, len(img[0]) - 1):
            node = derivative(img, i, j)
            temp.append(node)
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(name, ans)
    return ans


def sharpen(img, i, j):
    """implementing the mask for sharpening"""
    pixel = 0.00
    for m in range(i - 1, i + 2):
        for n in range(j - 1, j + 2):
            if i == m and j == n:
                temp = 9 * img[m][n]
            else:
                temp = -1 * img[m][n]
            pixel += temp
    return pixel


def derivative(img, i, j):
    """implementing the mask for derivation"""
    pixel = 0.00
    for m in range(i - 1, i + 2):
        for n in range(j - 1, j + 2):
            if i == m and j == n:
                temp = -8 * img[m][n]
            else:
                temp = img[m][n]
            pixel += temp
    return pixel


def processing():
    """processing the digital images"""
    # original image, cat
    cat = folder + 'cat.jpg'
    image = cv2.imread(cat, 0)
    frequency(image, output + 'cat_frequency.jpg')
    image_padded = padding(image, output + 'cat_padded.jpg')
    filter_derivative(image_padded, output + 'cat_derivative.jpg')
    # overwrite for the quality
    image_derivative = ned.laplace(image)
    imageio.imwrite(output + 'cat_derivative.jpg', image_derivative)
    image_sharpened = image - image_derivative
    imageio.imwrite(output + 'cat_sharpened.jpg', image_sharpened)

    # original image, triangle
    triangle = folder + 'triangle.jpg'
    image = cv2.imread(triangle, 0)
    frequency(image, output + 'triangle_frequency.jpg')
    image_padded = padding(image, output + 'triangle_padded.jpg')
    filter_derivative(image_padded, output + 'triangle_derivative.jpg')
    # overwrite for the quality
    image_derivative = ned.laplace(image)
    imageio.imwrite(output + 'triangle_derivative.jpg', image_derivative)
    image_sharpened = image - image_derivative
    imageio.imwrite(output + 'triangle_sharpened.jpg', image_sharpened)
    return


if __name__ == '__main__':
    """main function to start the program"""
    folder = ''
    output = './bin/'
    processing()
