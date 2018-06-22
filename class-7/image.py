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

#to draw a line in the image
#   image data,start point , end point, color, line width
cv2.line(img1,(0,0),(150,100),(0,0,255),4)

# cv2.rectangle() -> two ppint of hp , color, line width
# cv2.circle() -> center,radius,color,line width

# Putting text on image 
# font = cv2.FONT_HERSEY_SIMPLEX 
# cv2.putTEXT(img1,"NEKO",(10,10),font,3,(100,23,200))
# data ,text ,starting point, font type, size, color

cv2.imshow("windowname",img1)
cv2.imshow("Gray",img0)
cv2.imshow("Trans",img_1)

# save black and white (GRAY) image
cv2.imwrite("new_name.jpeg",img1)

#to hold upper window
cv2.waitKey(0)