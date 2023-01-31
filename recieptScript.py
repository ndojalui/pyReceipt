import cv2
import pytesseract
import numbers

userDic = {"august": 0, "luigi":0,"kyle":0,"christain":0,"josh":0}
path_to_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

img = cv2.imread(r'C:\\Users\\augus\\OneDrive\\Desktop\\PythonScript\\testImage.png',cv2.IMREAD_GRAYSCALE)
ret, img = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
text = pytesseract.image_to_string(img)
text = str(text)
print(text)
print("____________________________________________")
text = text.splitlines()
print(text[6])
for item in text:
    if "TOTAL:" in item:
        print("Found it: " + item)
        x= str(item).split(" ")
        fPrice = x[-1]
        print("Total: " + fPrice)

for i in userDic:
    userDic[i]=float(fPrice)/5

while(True):
    print("Everyone Owes")
    for i in userDic:
        print(i + " "+ str(userDic[i]))

    print("Enter name and much they owe for the personal item, split by a space, 'stop' to stop entering data")
    userItem = input(": ")
    if userItem == "stop":
        break
    userItem = userItem.split(" ")
    
    if(userItem[0]=="august"):
        userDic["august"] += float(userItem[1])*(4/5)
        for i in userDic:
            if i != "august":
                userDic[i] -=float(userItem[1])*(1/5)
    elif(userItem[0]=="luigi"):
        userDic["luigi"] += float(userItem[1])*(4/5)
        for i in userDic:
            if i != "luigi":
                userDic[i] -=float(userItem[1])*(1/5)
    elif(userItem[0]=="kyle"):
        userDic["kyle"] += float(userItem[1])*(4/5)
        for i in userDic:
            if i != "kyle":
                userDic[i] -=float(userItem[1])*(1/5)
    elif(userItem[0]=="christain"):
        userDic["christain"] += float(userItem[1])*(4/5)
        for i in userDic:
            if i != "christain":
                userDic[i] -=float(userItem[1])*(1/5)
    elif(userItem[0]=="josh"):
        userDic["christain"] += float(userItem[1])*(4/5)
        for i in userDic:
            if i != "christain":
                userDic[i] -=float(userItem[1])*(1/5)
