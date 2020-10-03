import cv2
import pandas as pd
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
cv2.namedWindow('image')
img = cv2.imread('flo2.jpg')
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index)
clicked = False
while(1):
    cv2.imshow("image",img)
    cv2.setMouseCallback('image', draw_function)
    if (clicked):
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        cv2.putText(img, text,(50,50),cv2.FONT_HERSHEY_TRIPLEX,0.8,(255,255,255),2)
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    #Break if user hits 'esc' key
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()