# 용도

## 00_FileCopy
    GT 데이터를 여러개로 나누거나 임의로 선별하여 그룹화함

## 01_MergeData
    여러개로 나뉘어져 있는 GT 혹은 Output 데이터를 병합

## 02_Get_mAP
    mAP 계산용 프로그램

## 03_IDXmaker
    동일한 경로 상의 영상 파일에 대한 .idx 파일 생성 >> 몇몇 영상에서 안되는 문제 확인

### 0.9.1
    - .avi, .mkv도 사용 가능

### 0.9.0
    - 해당 .exe 파일과 동일한 경로에 .mp4 동영상을 넣고 실행시키면, IDX 파일을 생성
    - 해당 경로상에 여러개의 동영상을 넣어서 실행하면, 여러개의 IDX 파일이 바로 생성
    - 해당 .exe파일을 .mp4 동영상이 있는 폴더로 옮겨서 사용하셔도 가능

## 04_SimEquation
### => 오토켈리브레이션으로 인해 사용 X
    Data.csv에 있는 길이 데이터를 통해 다수의 연립방정식을 풀어 해를 구함
    
## 05_CountTXTtoCSV
    txt 파일에 단순 카운팅 자료를 종합하여 CSV로 옮김

## 06_CountingOnVideo
### => 미완성
    영상 재생과 동시에 카운팅 하는 프로그램

## 07_AvgGTRectSize
### 0.1.0
    데이터 셋 전체 차량의 너비, 높이 데이터 종합
### 0.2.0
    너비/높이 데이터 추가

## 08_BackgroundSubtractor
    배경 제거 알고리즘 예제

## 09_Video2GIF
    Video to GIF 예제

## 10_CrossroadCounting
    SignUS에서 나온 회전류 Log 데이터를 단위 시간별로 끊어서 저장

## 11_VDSDataRandomSampling
### => 미완성

## 12_GetROIMask
### => 미완성

## 13_VideoSampling
### => 미완성

## 14_PNGtoJPG
    폴더 내부 PNG 파일을 전부 JPG로 변경

## 15_MakeLPRData
### => 미완성

## 16_ClassModify
    YOLO 정답 파일인 txt 파일에서 클래스를 수정하는 스크립트

## 17_VideoMerge
    두 개 이상의 영상을 하나로 이어 붙이는 스크립트

## 18_COCOSplitter
    필요한 클래스의 데이터로만 이루어지도록 분할

## 19_DataSetOrganization
    데이터셋 라벨링 되어있는 .txt 문서를 Windows COCO 형식으로 전환

## 20_LPRClassChanger
    SetLPR로 만들어진 데이터 클래스를 유니코드 값이 아닌 네임즈로 세팅되어있는 값으로 변환

## 21_ImageSizeChanger
    이미지의 크기를 정해진 크기로 변경하여 저장 1280x720

## 22_FalseNegativeLPImage
    폴더 내 이미지 중 번호판 미검지 이미지만 골라내서 다른 폴더로 이동시키는 스크립트

## 23_LogAnalysis
    IntelligentVDS의 전체 로그와 최근 24시간 로그를 통계적으로 비교할 수 있도록 Plot 표출

## 24_CameraExtrinsicCalibration

## 25_ToKITTIDataFormat

## 26_AVIAnalyser
    화성 번호인식 결과를 이용한 데이터 분석

## 27_BusLinkChecker
    버스 링크/노드 좌표 체크

## 28_COCOtoYOLOFormat
    AI허브의 딸기 데이터를 Sign Yolo 형식으로 변환

## 29_ImageBlur
    폴더 내에 있는 이미지 블러 (라벨링 된 데이터 용)

## 30_WebCamRecorder
    웹캠 녹화용


## 99_ArgVarTest
    프로그램 실행 시 매개변수 Arg, Var 예제

## 99_ExMatplotlib
    Matplotlib 예제

## 99_RemoveBackGround
    Unet을 이용한 배경 제거 예제

# exe 만들기
    pyinstaller -w -F pythonFileName.py
    -w : 콘솔 표시 안함 (디폴트 : 콘솔 표시)
    -F : 단일 exe 파일로 변환 (디폴트 : 1개 폴더로 구성)
    -n NAME.exe :프로그램 이름을 NAME으로 지정
