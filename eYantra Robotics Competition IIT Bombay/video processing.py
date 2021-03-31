
import cv2 as cv
import imageio


def partA():
    vidcap = cv.VideoCapture('RoseBloom.mp4')

    def Frame_at_6(sec):
        vidcap.set(cv.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = vidcap.read()
        if hasFrames:
            cv.imwrite("frame_as_6.jpg" + str(count) + ".jpg", image)
        return hasFrames

    sec = 0
    frameRate = 6
    count = 0
    success = Frame_at_6(sec)
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = Frame_at_6(sec)


def partB():
    im = imageio.imread("frame_as_6.jpg1.jpg")
    im[:, :, 0] = 0
    im[:, :, 1] = 0
    cv.imwrite("frame_as_6_red.jpg", im)


partA()
partB()
