
import rawpy
import numpy
import imageio


def save(file, name):
    temp = rawpy.imread(file)
    image = temp.postprocess()
    imageio.imsave(name, image)
    return


def subsample4(name, image):
    ans = []
    for i in range(0, n1, 4):
        temp = []
        for j in range(0, n2, 4):
            temp.append(image[i][j][:])
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imsave(name, ans)
    return ans


def subsample16(name, image):
    ans = []
    for i in range(0, n1, 16):
        temp = []
        for j in range(0, n2, 16):
            temp.append(image[i][j][:])
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imsave(name, ans)
    return ans


def interpolation4(name, image):
    ans = []
    for i in range(0, n1):
        temp = []
        x = round(i / 4)
        if x == n1 / 4:
            x = int(n1 / 4 - 1)
        for j in range(0, n2):
            y = round(j / 4)
            if y == n2 / 4:
                y = int(n2 / 4 - 1)
            temp.append(image[x][y][:])
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imsave(name, ans)
    return


def interpolation16(name, image):
    ans = []
    for i in range(0, n1):
        temp = []
        x = round(i / 16)
        if x == n1 / 16:
            x = int(n1 / 16 - 1)
        for j in range(0, n2):
            y = round(j / 16)
            if y == n2 / 16:
                y = int(n2 / 16 - 1)
            temp.append(image[x][y][:])
        ans.append(temp)
    ans = numpy.array(ans, dtype='uint8')
    imageio.imsave(name, ans)
    return


def run():
    while True:
        try:
            image = imageio.imread(triangle)
            temp = subsample4(output + 'triangles4.jpg', image)
            interpolation4(output + 'trianglei4.jpg', temp)
            temp = subsample16(output + 'triangles16.jpg', image)
            interpolation16(output + 'trianglei16.jpg', temp)
            break
        except FileNotFoundError:
            save(folder + 'triangle.raw', triangle)
    while True:
        try:
            image = imageio.imread(cat)
            temp = subsample4(output + 'cats4.jpg', image)
            interpolation4(output + 'cati4.jpg', temp)
            temp = subsample16(output + 'cats16.jpg', image)
            interpolation16(output + 'cati16.jpg', temp)
            break
        except FileNotFoundError:
            save(folder + 'cat.raw', cat)
    return


if __name__ == '__main__':
    folder = ''
    output = './bin/'
    triangle = output + 'triangle.jpg'
    cat = output + 'cat.jpg'
    n1 = 480
    n2 = 640
    run()
