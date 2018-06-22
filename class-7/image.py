import cv2
# reading image
#   image name, image faetures
# 1 -> color 0-> black and white -1 transparency
# 1 -> IMREAD_COLOR 0-> IMREAD_BGR2GRAY -1 -> IMREAD_UNCHANGE_COLOR
img1 = cv2.imread("image.jpeg",1)
img0 = cv2.imread("image.jpeg",0)
# checking rows and cols
print img1.shape
print img0.shape

# to show image
# parameters
    # windowName
    # data
cv2.imshow("windowname",img1)
cv2.imshow("Gray",img0)
cv2.imshow("Trans",img_1)

# save black and white (GRAY) image
cv2.imwrite()

#to hold upper window
cv2.waitKey(0)