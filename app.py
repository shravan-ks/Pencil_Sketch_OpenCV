import osd
import cv2
import glob

image_path = input("Enter Image Path of Image: with Extension >>")
print(image_path)

for f in glob.glob(image_path):
    filename = 'Pencil Sketch ' + (os.path.split(f)[-1])


image = cv2.imread(image_path)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImageInv = 255 - grayImage

grayImageInv = cv2.GaussianBlur(grayImageInv, (71, 71), 0)

output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.namedWindow(filename, cv2.WINDOW_NORMAL)
cv2.resizeWindow(filename, 5400, 3600)


cv2.imshow("image", image)
cv2.imshow(filename, output)
cv2.imwrite(filename , output)
cv2.waitKey(0)