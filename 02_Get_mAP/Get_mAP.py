# csv 파일로 mAP 계산
import sys
import os
import time

# CSV 파일 경로 및 이름 받아서 List 형태로 반환
def CSVtoList(csv_file_name): 
    csvfp = open(csv_file_name, 'r')
    CSVLines = csvfp.readlines()
    Datalist = []
    for line in CSVLines:
        Data = line.split(',')
        tmp = []
        ii = 0
        for Data_ in Data:
            if ii == 0: # file name
                tmp = tmp + [Data_]
            elif ii == len(Data)-1: # '\n'
                break
            elif ii == 1: # Class
                tmp = tmp + [int(Data_)]
            elif ii > 1: # (Conf), x, y, w, h
                tmp = tmp + [float(Data_)]
            ii = ii + 1

        Datalist = Datalist + [tmp]
    csvfp.close()

    return Datalist

# List 데이터 출력, 보기 좋게
def PrintList(ListData): 
    for ld in ListData :
        print(ld)
    print(" ", end="\n")

# List 구성 데이터 중 파일 이름 부분만 모아서 고유한 값 생성
def GetUniqueFileName(ListData): 
    zipData_ = zip(*ListData)

    for Data in zipData_:
        FileNames = Data
        break

    FileNames = list(set(FileNames))

    return FileNames

# 두 리스트 내용 중 동일한 내용 값만 모아 반환
def GetSameData(DataList0, DataList1):
    Data = []

    for list0 in DataList0:
        for list1 in DataList1:
            if list0 == list1:
                Data = Data + [list0]
                break

    Data = sorted(Data)

    return(Data)

# 사각형 외접원 반지름 구하기
def GetCircleR(Rect):
    R = (Rect['w']/2)*(Rect['w']/2) + (Rect['h']/2)*(Rect['h']/2)
    return float(R)

# 두 사각형의 중심 거리 구하기
def GetRectDist(Rect0, Rect1):
    dist = (Rect0['x']-Rect1['x'])*(Rect0['x']-Rect1['x']) + (Rect0['y']-Rect1['y'])*(Rect0['y']-Rect1['y'])
    return float(dist)

# 사각 정보를 통해 교차 영역 구하기
def GetCrossArea(Rect0, Rect1):
    # print("\tGetCrossArea >> ")
    X = [Rect0['x'] - Rect0['w']/2, Rect0['x'] + Rect0['w']/2, Rect1['x'] - Rect1['w']/2, Rect1['x'] + Rect1['w']/2]
    Y = [Rect0['y'] - Rect0['h']/2, Rect0['y'] + Rect0['h']/2, Rect1['y'] - Rect1['h']/2, Rect1['y'] + Rect1['h']/2]

    X = sorted(X)
    Y = sorted(Y)

    return X, Y

# 사각형 넓이
def GetRectArea(Rect):
    # print("\t\tGetRectArea >> ", end='')
    # print(Rect['w'] * Rect['h'])
    return float(Rect['w'] * Rect['h'])

# 두 사각형의 IOU 구하기 : 교차영역 / (두 영역 넓이 - 교차 영역)
def GetIOU(Rect0, Rect1):
    # print("Get IOU >>")

    X, Y = GetCrossArea(Rect0, Rect1)

    CrossRect = {'w':abs(X[1]-X[2]), 'h':abs(Y[1]-Y[2])}

    CrossArea = GetRectArea(CrossRect)
    Rect0Area = GetRectArea(Rect0)
    Rect1Area = GetRectArea(Rect1)

    IOU = CrossArea / (Rect0Area + Rect1Area - CrossArea)
    return IOU

# 평탄화
def FlattingGraph(Pr, Rc):
    
    Flat_Pr = [float(0.0) for i in range(0, (len(Pr))*2)]
    Flat_Rc = [float(0.0) for i in range(0, (len(Rc))*2)]

    for ii in range(len(Rc)-1, 0, -1):
        Flat_Rc[2*ii] = Rc[len(Rc)-ii]
        Flat_Rc[2*ii+1] = Rc[len(Rc)-1-ii]

        maxPr = max(Pr[0:(len(Rc)-ii)])

        Flat_Pr[2*ii] = maxPr
        Flat_Pr[2*ii+1] = maxPr
    
    # print("Flat Rc >> ", end='')
    # print(Flat_Rc, end='\n\n')
    # print("Flat Pr >> ", end='')
    # print(Flat_Pr)

    return Flat_Pr, Flat_Rc

# AP 구하기
def GetAP(FlatPr, FlatRc):
    Area = 0
    for ii in range(1, len(FlatPr)-1):
        Area = Area + ((FlatPr[ii+1]+FlatPr[ii]) * (FlatRc[ii+1]-FlatRc[ii]))/2

    return Area

def ListSum(list):
    sum = 0
    for ii in list:
        sum = sum + ii
    return sum

def numListPrint(nGT, nTP, nFP, nFN):
    print(str(conf_) + " : ", end='')
    print("\t%3d"%ListSum(nGT), end='')
    print("\t%3d"%ListSum(nTP), end='')
    print("\t%3d"%ListSum(nFP), end='')
    print("\t%3d"%ListSum(nFN))

# Main
# 매개 변수로 폴더 이름 받기
if len(sys.argv) == 1: # 확장자 명, 모델 이름 입력 안했을 시
    print("py " + sys.argv[0] + " [Data Path] [Model] ... ")
elif len(sys.argv) == 2: # 모델 이름 입력 안했을 시 
    print("py " + sys.argv[0] + " " + sys.argv[1] + " [Model] ... ")
elif len(sys.argv) >= 3: # 다 입력 했을 시
    gtCSV_name = sys.argv[1] + "_txt.csv"
    resCSV_name = sys.argv[1] + "\\" + sys.argv[2] + "_csv.csv"
    print("Ground Truth files : " + sys.argv[1] + "\\")
    print("   >>     nGT Data : ", end=' ')
    GT = CSVtoList(gtCSV_name)
    print(len(GT), end="\n")
    # print("   >>      GT Data   ", end='\n')
    # PrintList(GT)

    print("Model Output files : " + sys.argv[1] + "\\" + sys.argv[2] + "\\")
    print("   >> nResult Data : ", end=' ')
    Res = CSVtoList(resCSV_name)
    print(len(Res), end="\n\n")
    # print("   >>  Result Data   ", end='\n')
    # PrintList(Res)

    FileNames = GetSameData(GetUniqueFileName(GT), GetUniqueFileName(Res))
    # print(FileNames)
    ImgInfo = {'w':1280, 'h':720}
    Confidence = [x / 10 for x in list(range(0, 11))]
    Class = list(range(0, 5))

    tic = time.time()

    ClassAP = [float(0.0) for i in range(0, len(Class))]
    for class_ in Class:
        print("Class >> " + str(class_))
    # class_ = 1
    
        # print("\tConf.\tPrec.\tRecall")
        # print("\tnGT\tnTP\tnFP\tnFN")
        Precision = [float(0.0) for i in range(0, len(Confidence))]
        Recall = [float(0.0) for i in range(0, len(Confidence))]
        for confIdx in range(0, len(Confidence)):
            conf_ = Confidence[confIdx]
        # conf_ = 0.9
            file_nGT = [int(0) for i in range(0, len(FileNames))]
            file_nTP = [int(0) for i in range(0, len(FileNames))]
            file_nFP = [int(0) for i in range(0, len(FileNames))]
            file_nFN = [int(0) for i in range(0, len(FileNames))]
            for fidx in range(0, len(FileNames)):
                print("\tConfidence >> " + str(conf_) + " : " + str(fidx+1) + " / " + str(len(FileNames)), end='       \r')
                # print("Class >> " + str(class_) + " : " + 
                #     str(confIdx*(len(FileNames)-1) + fidx) + " / " + 
                #     str((len(Confidence)-1)*(len(FileNames)-1)), end='\r')
            # fidx = 0
                filename_ = FileNames[fidx]
                for gt_ in GT:
                    if (gt_[0] == filename_) and (gt_[1] == class_):
                        file_nGT[fidx] = file_nGT[fidx] + 1 # 해당 클래스의 GT 개수 구하기
                        gtRect = {'x':gt_[2] * ImgInfo['w'], 'w':gt_[4] * ImgInfo['w'], 'y':gt_[3] * ImgInfo['h'], 'h':gt_[5] * ImgInfo['h']}
                        gtR = GetCircleR(gtRect)
                        for res_ in Res:
                            if res_[2] > conf_:
                                if (res_[0] == filename_) and (res_[1] == class_):
                                    file_nFP[fidx] = file_nFP[fidx] + 1 # 해당 클래스의 결과 수 구하기
                                    resRect = {'x':res_[3] * ImgInfo['w'], 'w':res_[5] * ImgInfo['w'], 'y':res_[4] * ImgInfo['h'], 'h':res_[6] * ImgInfo['h']}

                                    gtresDist = GetRectDist(gtRect, resRect)

                                    if(gtR > gtresDist):
                                        IOU = GetIOU(gtRect, resRect)
                                        if(IOU >= 0.5):
                                            file_nTP[fidx] = file_nTP[fidx] + 1 # 정 검출 결과

                if(file_nGT[fidx] > 0):
                    file_nFP[fidx] = int(file_nFP[fidx] / file_nGT[fidx]) - file_nTP[fidx] # 정답 수 만큼 반복했으므로 정답수로 나누고, 정검출 수 빼면, 오검출

                    file_nFN[fidx] = file_nGT[fidx] - file_nTP[fidx] # 정답 수 중 정검출 된 거 빼면 미검출
                else:
                    file_nFP[fidx] = 0
                    file_nTP[fidx] = 0

            if(conf_ == 1.0):
                Precision[confIdx] = 1.0
                Recall[confIdx] = 0.0
            else:
                Precision[confIdx] = float(ListSum(file_nTP)) / float(ListSum(file_nTP) + ListSum(file_nFP) + 0.000001)
                Recall[confIdx] = float(ListSum(file_nTP)) / float(ListSum(file_nGT) + 0.000001)

            # numListPrint(file_nGT, file_nTP, file_nFP, file_nFN)
            
            # print('', end='\t')
            # print(conf_, end='\t')
            # # print("\n\t\tPrecision >> ", end='')
            # print('%.3f' %Precision[confIdx], end='\t')
            # # print("\t\t   Recall >> ", end='')
            # print('%.3f' %Recall[confIdx])

        Flat_Pr, Flat_Rc = FlattingGraph(Precision, Recall)
        ClassAP[class_] = GetAP(Flat_Pr, Flat_Rc)
        print("\n\tAP >> %.3f" %ClassAP[class_])

    print("\nmAP >> %.3f" %(ListSum([ClassAP[1], ClassAP[2], ClassAP[4]])/3))
    
    toc = time.time()
    print("Proc. Time >> ", end='')
    print("%.3f" %(toc-tic))