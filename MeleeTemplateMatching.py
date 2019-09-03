import cv2
import numpy as np

#Opens main image
img_bgr = cv2.imread('melee.png')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

#Open Template
def opentemplate(filename):
  template = cv2.imread(filename,0)
  w, h = template.shape[::-1]
  return template

templates = ["jigglypuff.png", "fox.png"]
colors = [(0,255,255), (235, 64, 52)]
for index, template in enumerate(templates):
  print(index, template)
  #Opens template
  template = cv2.imread(template,0)
  w, h = template.shape[::-1]
  #Matches template to image
  res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
  threshold = 0.8
  loc = np.where(res >= threshold)
  #Draws rectangles on image
  for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1] + h), colors[index], 2)

#Display  
cv2.imshow('Detected',img_bgr)
cv2.waitKey()