import cv2
img=cv2.imread("butterfly.jpy")
cv2.imshow("display image",img)
grey_img=cv2.cvtColor(img,cv2.COLOR_RGB2GREY)
cv2.imshow("greyscale",grey_img)
cv2.waitkey(0)