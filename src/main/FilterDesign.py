
import cv2
import imageio
import numpy
import matplotlib.pyplot
import matplotlib.ticker


def plot_hist(x, y, col, name):
    """histogram plotting function"""
    matplotlib.pyplot.bar(x, y, color=col, label=name)
    matplotlib.pyplot.xlim(x[0] - 10, x[-1] + 10)
    matplotlib.pyplot.xticks([0, 64, 128, 192, 255])
    matplotlib.pyplot.ylabel('Pixels')
    matplotlib.pyplot.xlabel('Gray-Level')
    matplotlib.pyplot.legend()
    return


def histogram(img, title):
    """calculating the histogram"""
    x = r_input
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    h = []
    for i in range(0, 256):
        h.append(hist[i][0])
    plot_hist(x, h, 'purple', title)
    return


def image_creation():
    """creating the digital images of the pattern"""
    im1 = []
    for x in range(0, 512):
        temp = []
        for y in range(0, 255):
            temp.append(0)
        temp.append(67)
        temp.append(133)
        for y in range(257, 512):
            temp.append(200)
        im1.append(temp)
    im1 = numpy.array(im1, dtype='uint8')
    histogram(im1, 'Image 1')
    matplotlib.pyplot.savefig(output + 'image1_histogram.jpg')
    matplotlib.pyplot.close()
    im2 = []
    flag1 = True
    flag2 = True
    for x in range(0, 512):
        temp = []
        if x % 8 == 0:
            flag1 = not flag1
        for y in range(0, 512):
            if y % 8 == 0:
                flag2 = not flag2
            if (flag1 and flag2) or (not flag1 and not flag2):
                temp.append(0)
            elif (flag1 and not flag2) or (not flag1 and flag2):
                temp.append(200)
        im2.append(temp)
    im2 = numpy.array(im2, dtype='uint8')
    histogram(im2, 'Image 2')
    matplotlib.pyplot.savefig(output + 'image2_histogram.jpg')
    matplotlib.pyplot.close()
    return


def filter_average(img, name):
    """applying the average filter to the image"""
    ans = []
    for i in range(0, len(img)):
        temp = []
        for j in range(0, len(img[i])):
            node = average(img, i, j)
            temp.append(node)
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(output + name, ans)
    return


def filter_median(img, name):
    """applying the median filter to the image"""
    ans = []
    for i in range(0, len(img)):
        temp = []
        for j in range(0, len(img[i])):
            node = median(img, i, j)
            temp.append(node)
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imwrite(output + name, ans)
    return


def average(img, i, j):
    """calculating the average of the pixels"""
    ans = 0.00
    for m in range(i - 5, i + 6):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - 5, j + 5):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            ans += img[m][n] / 121
    return ans


def median(img, i, j):
    """calculating the median of the pixels"""
    temp = []
    for m in range(i - 5, i + 6):
        if m < 0:
            m = 0
        elif m > len(img) - 1:
            m = len(img) - 1
        for n in range(j - 5, j + 5):
            if n < 0:
                n = 0
            elif n > len(img[0]) - 1:
                n = len(img[0]) - 1
            temp.append(img[m][n])
    temp.sort()
    return temp[60]


def processing():
    """digital processing of the image to get the histogram and equalized versions"""
    cat = folder + 'cat.jpg'
    triangle = folder + 'triangle.jpg'
    # first original image, CAT
    label = 'Original Cat Image'
    image = cv2.imread(cat, 0)
    histogram(image, label)
    matplotlib.pyplot.savefig(output + 'histogram_cat_original.jpg')
    matplotlib.pyplot.close()
    # average filtered image, CAT
    label = 'Average Filtered Cat Image'
    filter_average(image, 'cat_averaged.jpg')
    processed_image = cv2.imread(output + 'cat_averaged.jpg', 0)
    histogram(processed_image, label)
    matplotlib.pyplot.savefig(output + 'histogram_cat_averaged.jpg')
    matplotlib.pyplot.close()
    # median filtered image, CAT
    label = 'Median Filtered Cat Image'
    filter_median(image, 'cat_median.jpg')
    processed_image = cv2.imread(output + 'cat_median.jpg', 0)
    histogram(processed_image, label)
    matplotlib.pyplot.savefig(output + 'histogram_cat_median.jpg')
    matplotlib.pyplot.close()
    # second original image, TRIANGLE
    label = 'Original Triangle Image'
    image = cv2.imread(triangle, 0)
    histogram(image, label)
    matplotlib.pyplot.savefig(output + 'histogram_triangle_original.jpg')
    matplotlib.pyplot.close()
    # average filtered image
    label = 'Average Filtered Triangle Image'
    filter_average(image, 'triangle_averaged.jpg')
    processed_image = cv2.imread(output + 'triangle_averaged.jpg', 0)
    histogram(processed_image, label)
    matplotlib.pyplot.savefig(output + 'histogram_triangle_averaged.jpg')
    matplotlib.pyplot.close()
    # median filtered image
    label = 'Median Filtered Triangle Image'
    filter_median(image, 'triangle_median.jpg')
    processed_image = cv2.imread(output + 'triangle_median.jpg', 0)
    histogram(processed_image, label)
    matplotlib.pyplot.savefig(output + 'histogram_triangle_median.jpg')
    matplotlib.pyplot.close()
    return


if __name__ == '__main__':
    """main function to run the program"""
    r_input = range(0, 256)
    folder = ''
    output = './bin/'
    processing()
    image_creation()
