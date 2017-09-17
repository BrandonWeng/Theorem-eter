import cv2
import numpy as np

defNum = 1;
theoremNum = 1;

def defColor(pixel):
    #[172 248 255]
    return ((pixel[0] >= 165 and pixel[0] <= 175) and (pixel[1] >= 245 and pixel[1] <= 250) and \
    (pixel[2] >= 253 and pixel[2] <= 258))

def theoremColor(pixel):
    #[214 194 196]
    return ((pixel[0] >= 212 and pixel[0] <= 217) and (pixel[1] >= 192 and pixel[1] <= 196) and \
    (pixel[2] >= 194 and pixel[2] <= 199))

def whitePixel(pixel):
    return np.all(pixel >= 245);

# def saveImg(fileName, startHeight, endHeight, pageImg):
#     cropImg = pageImg[startHeight:endHeight , 0:pageImgWidth];
#     cv2.imshow("test",cropImg);
#     cv2.waitKey(0);

def extractPage(imgName):
    global defNum;
    global theoremNum;

    pageImg = cv2.imread(imgName);
    pageImg = cv2.resize(pageImg, (1200, 1500))
    pageImgHeight, pageImgWidth, ch = pageImg.shape;
    defExtract = theoremExtract = False;
    defStart = theoremStart = 0;
    mid = int(pageImgWidth / 2);

    for i in range(pageImgHeight):
        if(defColor(pageImg[i][mid]) and not defExtract):
            defStart = i;
            defExtract = True;

        if(theoremColor(pageImg[i][mid]) and not theoremExtract):
            theoremStart = i;
            theoremExtract = True;

        if(defExtract and whitePixel(pageImg[i][mid])):
            defExtract = False;
            cropImg = pageImg[defStart:i -1 , 0:pageImgWidth];
            cv2.imwrite("definitions/definition" + str(defNum) + ".jpg" ,cropImg);
            defNum += 1;

        if(theoremExtract and whitePixel(pageImg[i][mid])):
            theoremExtract = False;
            cropImg = pageImg[theoremStart:i -1 , 0:pageImgWidth];
            cv2.imwrite("theorems/theorem" + str(theoremNum) + ".jpg",cropImg);
            theoremNum += 1;

def extractBook(path, startPage, endPage):
    for pageNum in range(startPage, endPage):
        extractPage(path + str(pageNum) + ".jpg");

def cropDefinitions(path, numDef):
    for i in range (1, numDef):
        print("image" + str(i));
        imgName = path + "definition" + str(i) + ".jpg";
        print(imgName);
        defImg = cv2.imread(imgName);
        defImgHeight, defImgWidth, ch = defImg.shape;
        start = 0;
        end = 0;

        for k in range (defImgWidth):
            if(defColor(defImg[0][k])):
                start = k;
                break;

        for k in range(defImgWidth - 1, -1, -1):
            if(defColor(defImg[0][k])):
                end = k;
                break;

        headImg = defImg[0:defImgHeight , 0:start];
        cv2.imwrite("definitions/defHead" + str(i) + ".jpg",headImg);
        bodyImg = defImg[0:defImgHeight , start:end];
        cv2.imwrite("definitions/defBody" + str(i) + ".jpg",bodyImg);

def cropTheorems(path, numTheorems):
    for i in range (1, numTheorems):
        print("image" + str(i));
        imgName = path + "theorem" + str(i) + ".jpg";
        print(imgName);
        theoremImg = cv2.imread(imgName);
        theoremImgHeight, theoremImgWidth, ch = theoremImg.shape;
        start = 0;
        end = 0;

        for k in range (theoremImgWidth):
            if(theoremColor(theoremImg[0][k])):
                start = k;
                break;

        for k in range(theoremImgWidth - 1, -1, -1):
            if(theoremColor(theoremImg[0][k])):
                end = k;
                break;

        headImg = theoremImg[0:theoremImgHeight , 0:start];
        cv2.imwrite("theorems/theoremHead" + str(i) + ".jpg",headImg);
        bodyImg = theoremImg[0:theoremImgHeight , start:end];
        cv2.imwrite("theorems/theoremBody" + str(i) + ".jpg",bodyImg);

cropTheorems("theorems/" ,96);
# extractBook("linAlgJpg/linear_algebra_course_notes_v3-", 11, 218);
