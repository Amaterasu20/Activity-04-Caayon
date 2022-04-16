import cv2
filePath = 'klsmyt.jpg'
imgFlag = int(1)
img = cv2.imread(filePath,imgFlag)
cv2.imshow("Classmate and Tropa",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
