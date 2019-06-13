
import cv2
import numpy
import matplotlib.pyplot
import matplotlib.ticker


def data_plot(x, y, col, name):
    """DataScience plotting function"""
    matplotlib.pyplot.plot(x, y, color=col, label=name)
    matplotlib.pyplot.xlim(x[0], x[-1])
    matplotlib.pyplot.ylim(x[0], x[-1])
    matplotlib.pyplot.xticks([0, 64, 128, 192, 255])
    matplotlib.pyplot.yticks([0, 64, 128, 192, 255])
    matplotlib.pyplot.ylabel('Output Gray-Level (s)')
    matplotlib.pyplot.xlabel('Input Gray-Level (r)')
    matplotlib.pyplot.legend()
    return


def hist_plot(x, y, col, name):
    """histogram plotting function"""
    matplotlib.pyplot.bar(x, y, color=col, label=name)
    matplotlib.pyplot.xlim(x[0], x[-1])
    matplotlib.pyplot.xticks([0, 64, 128, 192, 255])
    matplotlib.pyplot.ylabel('Pixels')
    matplotlib.pyplot.xlabel('Gray-Level')
    matplotlib.pyplot.legend()
    return


def cdf_plot(x, y, col, name):
    """cumulative distribution plotting function"""
    matplotlib.pyplot.plot(x, y, color=col, label=name)
    matplotlib.pyplot.xlim(x[0], x[len(x) - 1])
    matplotlib.pyplot.xticks([0, 64, 128, 192, 255])
    matplotlib.pyplot.ylabel('CDF')
    matplotlib.pyplot.xlabel('Gray-Level')
    matplotlib.pyplot.legend()
    return


def image_process(img):
    """applying the Gamma transformation to the image"""
    pic = glt(img, gamma=0.4)
    pic = numpy.array(pic, dtype='uint8')
    cv2.imwrite(output + 'cat_red.jpg', pic)
    pic = glt(image, gamma=2.5)
    pic = numpy.array(pic, dtype='uint8')
    cv2.imwrite(output + 'cat_blue.jpg', pic)
    return


def histogram_process(img):
    """obtaining the histogram of the images"""
    x = r_input
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    h = []
    for i in range(0, 256):
        h.append(hist[i][0])
    label = 'Original Histogram'
    hist_plot(x, h, 'purple', label)
    matplotlib.pyplot.savefig(output + 'original_histogram.jpg')
    matplotlib.pyplot.close()
    eq_img = cv2.equalizeHist(img)
    cv2.imwrite(output + 'equalized_cat.jpg', eq_img)
    eq_hist = cv2.calcHist([eq_img], [0], None, [256], [0, 256])
    eq_h = []
    for i in range(0, 256):
        eq_h.append(eq_hist[i][0])
    label = 'Equalized Histogram'
    hist_plot(x, eq_h, 'purple', label)
    matplotlib.pyplot.savefig(output + 'equalized_histogram.jpg')
    matplotlib.pyplot.close()
    func = hist.cumsum()
    func = 255 * func / func[-1]
    label = 'Transfer Function'
    data_plot(x, func, 'navy', label)
    matplotlib.pyplot.savefig(output + 'function.jpg')
    matplotlib.pyplot.close()
    return


def transform(gamma):
    """defining the transformation based on the value of Gamma"""
    r = r_input
    c = const(gamma)
    ans = [c * (x ** gamma) for x in r]
    return ans


def const(gamma):
    """constant value of the factor in transformation"""
    r = r_input
    ans = numpy.power(r[len(r) - 1], 1 - gamma)
    return ans


def glt_figure():
    """figures for Gamma transformation"""
    r = r_input
    # first Gamma function
    gamma = 0.4
    s = transform(gamma)
    label = '$\\gamma$ = ' + str(gamma)
    data_plot(r, s, 'red', label)
    # second Gamma function
    gamma = 2.5
    s = transform(gamma)
    label = '$\\gamma$ = ' + str(gamma)
    data_plot(r, s, 'blue', label)
    matplotlib.pyplot.savefig(output + 'Power_Law_GLTs.jpg')
    matplotlib.pyplot.close()
    return


def glt(img, gamma):
    """Gamma transformation on the image"""
    c = const(gamma)
    ans = []
    for i in range(0, len(img)):
        temp = []
        for j in range(0, len(img[0])):
            s = round(c * (img[i][j] ** gamma))
            if s == 256:
                s = 255
            temp.append(s)
        ans.append(temp)
    return ans


if __name__ == '__main__':
    """main function to run the program"""
    folder = ''
    output = './bin/'
    r_input = range(0, 256)
    glt_figure()
    cat = folder + 'cat.jpg'
    image = cv2.imread(cat, 0)
    image_process(image)
    histogram_process(image)
