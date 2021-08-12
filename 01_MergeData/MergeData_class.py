# 폴더 내 부의 txt 파일 병합
import sys
import os

# 매개 변수로 폴더 이름 받기
if len(sys.argv) == 1: # 확장자 명, 파일 경로 입력 안했을 시
    print("py " + sys.argv[0] + " [Data File Extention(=.txt, .csv)] [PickClass (=0, 1, 2, ...)] [Data File Path 0] [Data File Path 1] ... ")
elif len(sys.argv) == 2: # 파일 경로 입력 안했을 시
    print("py " + sys.argv[0] + " " + sys.argv[1] + " [PickClass (=0, 1, 2, 3, 4)] [Data File Path 0] [Data File Path 1] ... ")
elif len(sys.argv) == 3: # 파일 경로 입력 안했을 시
    print("py " + sys.argv[0] + " " + sys.argv[1] + " " + sys.argv[2] + " [Data File Path 0] [Data File Path 1] ... ")
elif len(sys.argv) >= 4: # 다 입력 했을 시
    # print("Data Extention : " + sys.argv[1])
    DataExten = sys.argv[1]
    if(DataExten == ".txt"):
        SplitChr = ' '
    elif(DataExten == ".csv"):
        SplitChr = ','

    PickClass = sys.argv[2]
        
    if(DataExten[0] != '.'):
        print("Data Extention : " + sys.argv[1])
        print("is wrong format")
        print("Data file extention format is .xxx")
        print("py " + sys.argv[0] + " .xxx" + " [Data File Path 0] [Data File Path 1] ... ")
    else :
        for Argidx in range(3, len(sys.argv)):
            NowPath = sys.argv[Argidx] + "/"
            print(NowPath)
            if os.path.isdir(sys.argv[Argidx]): # 폴더 존재 유무 확인. 존재 하면 실행.
                print("Exist this Path")
                
                CSVFile = open(sys.argv[Argidx] + "_" + PickClass + "_" + DataExten[1:] + ".csv", 'w')

                FileList = os.listdir(NowPath) # 해당 경로 파일 목록 읽기
                for Fileidx in range(0, len(FileList)):
                    if(FileList[Fileidx][-4:] == DataExten):
                        FileName = FileList[Fileidx][:-4] # 파일 이름과 확장자 분할
                        # print(FileName + DataExten)

                        file = open(NowPath + FileName + DataExten, 'r')
                        lines = file.readlines()
                        for line in lines:
                            line = line.split(SplitChr)
                            if(line[1] == PickClass):
                                # print([FileName] + line)
                                CSVFile.write(FileName)
                                for data in line:
                                    CSVFile.write(',')
                                    CSVFile.write(data.strip("\n"))
                                CSVFile.write(",\n")


                        file.close()

                    print(str(Fileidx+1) + "/" + str(len(FileList)), end='\r')

                CSVFile.close()
                print("\nThis Path Done.\n")




            else :
                print("Not exist this Path")
