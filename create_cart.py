import cv2
img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
text_to_show='i like coding'
cv2.putText(img,text_to_show,
            (20,220),
            frontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale=1,
            color=(0,0,255)
            )
cv2.imshow("output",img)
cv2.waitkey(0)