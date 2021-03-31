import cv2
import numpy as np
# import os
# import sys
import csv
import imageio


def partA():
    im = cv2.imread(r"bird.jpg")
    im2 = cv2.imread(r"cat.jpg")
    im3 = cv2.imread(r"flowers.jpg")
    im4 = cv2.imread(r"horse.jpg")

    # for image 1:
    dim = im.shape
    height = dim[0]
    width = dim[1]
    channel = dim[2]
    # for image 2
    dim2 = im2.shape
    height2 = dim2[0]
    width2 = dim2[1]
    channel2 = dim2[2]
    # for image 3 :
    dim3 = im3.shape
    height3 = dim3[0]
    width3 = dim3[1]
    channel3 = dim3[2]
    # for image 4 :
    dim4 = im4.shape
    height4 = dim4[0]
    width4 = dim4[1]
    channel4 = dim4[2]
    # for image 1:
    aa = im[:, :, 0]
    ab = im[:, :, 1]
    ac = im[:, :, 2]
    # for image 2 :
    aa2 = im2[:, :, 0]
    ab2 = im2[:, :, 1]
    ac2 = im2[:, :, 2]
    # for image 3 :
    aa3 = im3[:, :, 0]
    ab3 = im3[:, :, 1]
    ac3 = im3[:, :, 2]
    # for image 4 :
    aa4 = im4[:, :, 0]
    ab4 = im4[:, :, 1]
    ac4 = im4[:, :, 2]
    # for image 1 :
    t = aa.shape
    M = t[0]
    N = t[1]
    center, loc = M / 2, N / 2
    intensityR, intensityG, intensityB = aa[213, 320], ab[213, 320], ac[213, 320]
    # for image 2 :
    t2 = aa2.shape
    M2 = t2[0]
    N2 = t2[1]
    center2, loc2 = M2 / 2, N2 / 2
    intensity2R, intensity2G, intensity2B = aa2[195, 320], ab2[195, 320], ac2[195, 320]
    # for image 3 :
    t3 = aa3.shape
    M3 = t3[0]
    N3 = t3[1]
    center3, loc3 = M3 / 2, N3 / 2
    intensity3R, intensity3G, intensity3B = aa3[141, 320], ab3[141, 320], ac3[141, 320]
    # for image 4 :
    t4 = aa4.shape
    M4 = t4[0]
    N4 = t4[1]
    center4, loc4 = M4 / 2, N4 / 2
    intensity4R, intensity4G, intensity4B = aa4[202, 320], ab4[202, 320], ac4[202, 320]
    dict_data = [['bird.jpg', 'cat.jpg', 'flowers.jpg', 'horse.jpg'],
                 [height, height2, height3, height4],
                 [width, width2, width3, width4],
                 [channel, channel2, channel3, channel4],
                 [intensityB, intensity2B, intensity3B, intensity4B],
                 [intensityG, intensity2G, intensity3G, intensity4G],
                 [intensityR, intensity2R, intensity3R, intensity4R]]
    dict_data = np.array(dict_data)
    dict_data2 = np.transpose(dict_data)
    print(dict_data2)
    with open('ststs.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in range(0, dict_data2.shape[0]):
            myList = []
            myList.append(dict_data2[row])
            for al in myList:
                writer.writerow(al)
    csvfile.close()


def partB():
    im = cv2.imread(r"cat.jpg")
    im[:, :, 0] = 0
    im[:, :, 1] = 0
    red = cv2.imwrite("cat_red.jpg", im)
    # red.save("cat_red.jpg")

    pass


def partC():
    im = cv2.imread(r"flowers.jpg")
    bgra = cv2.cvtColor(im, cv2.COLOR_BGR2BGRA)
    alpha = np.full_like(im[..., 0], 128)
    print(alpha)
    bgra = cv2.merge((im, alpha))
    cv2.imwrite('flowers_alpha.png', bgra)


def partD():
    im = imageio.imread(r"horse.jpg")
    aa = im[:, :, 0]
    ab = im[:, :, 1]
    ac = im[:, :, 2]
    I = ((0.3 * aa) + (0.59 * ab) + (0.11 * ac))
    cv2.imwrite("horse_gray.jpg", I)


partB()
partC()
partD()
