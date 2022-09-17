from PIL import Image
import pytesseract
import cv2
import os



def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    if width is None:
        if height is None:
            return image

        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    if height is None:

        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        dim = (width, height)

    # return the resized image
    return cv2.resize(image, dim, interpolation = inter)


# image = 'pexels.jpg'
# img = cv2.imread(image)
# img = image_resize(img, width=18000, height=12000)
# # save the image
# cv2.imwrite('resizedbymaster.jpg', img)


# open a folder raw and resize each image create a new folder called raw_resized and save each image with its name after resizing

def resize_images():
    dirName = input('Enter the folder name: ')
    newDirname = f'{dirName}_resized'
    if not os.path.exists(newDirname):
        os.mkdir(newDirname)
    for filename in os.listdir(dirName):
        img = cv2.imread(f'{dirName}/{filename}')
        if img is not None:
            img = image_resize(img, width=3000, height=5000)
            cv2.imwrite(f'{newDirname}/{filename}', img)
            print(f'{filename} resized successfully')



if __name__ == '__main__':
    resize_images()


# for image in os.listdir('raw'):
#     img = cv2.imread(f'raw/{image}')
#     img = image_resize(img, width=1000, height=600)
#     # save the image
#     cv2.imwrite(f'raw_resized/{image}', img)


# Code From here: https://www.youtube.com/watch?v=kxHp5ng6Rgw
