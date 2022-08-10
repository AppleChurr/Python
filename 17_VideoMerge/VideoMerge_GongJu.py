from moviepy.editor import *


VideoPATH = "\\\\192.168.0.253\\Shared2_CCTV_AI\\[20211130] 공주 ITS 데이터 (11월 17일 24시간)\\# 영상_데이터\\"
DestPATH = "\\\\192.168.0.253\\Shared2_CCTV_AI\\[20211130] 공주 ITS 데이터 (11월 17일 24시간)\\# 영상_데이터_2H\\"
DatePATH = "\\2021\\11\\17\\"

SitePATH = [
            "01. 강북교차로_cam1 [FHD]", "01. 강북교차로_cam2 [FHD]", "01. 강북교차로_cam3 [FHD]", "01. 강북교차로_cam4 [FHD]", 
            "02. 생명과학고교차로_cam1 [FHD]", "02. 생명과학고교차로_cam2 [FHD]", "02. 생명과학고교차로_cam3 [FHD]", "02. 생명과학고교차로_cam4 [FHD]", 
            "03. 옥룡교차로_cam1 [FHD]", "03. 옥룡교차로_cam2 [FHD]", "03. 옥룡교차로_cam3 [FHD]",
            "04. 중동교차로_cam1 [FHD]", "04. 중동교차로_cam2 [FHD]", "04. 중동교차로_cam3 [FHD]", "04. 중동교차로_cam4 [FHD]",
            "05. 신월초사거리_cam1 [FHD]", "05. 신월초사거리_cam2 [FHD]", "05. 신월초사거리_cam3 [FHD]", "05. 신월초사거리_cam4 [FHD]", 
            "06. 연수원길 사거리_cam1 [D1]", "06. 연수원길 사거리_cam2 [D1]", "06. 연수원길 사거리_cam3 [D1]", "06. 연수원길 사거리_cam4 [D1]", 
            # "01. 전막교차로 (교차로) [FHD]", "02. 강북교차로 (교차로) [FHD]", "03. 공주IC (교차로) [FHD]", "04. 공주보 동측 삼거리 (교차로) [FHD]", 
            # "05. 송선교차로 (교차로) [FHD]", "06. 옥룡교차로 (교차로) [FHD]", "07. 금학교차로 (교차로) [FHD]", "08. 초대교회앞 삼거리 (교차로) [FHD]", 
            # "01. 전막교차로 [FHD]", "02. 강북교차로 [FHD]", "03. 공주IC [FHD]", "04. 공주보 동측 삼거리 [FHD]", 
            # "05. 송선교차로 [FHD]", "06. 옥룡교차로 [FHD]", "07. 금학교차로 [FHD]", "08. 초대교회앞 삼거리 [FHD]"
            ]

TargetFiles = [["20211117_070000-072959.mkv", "20211117_073000-075959.mkv", "20211117_080000-082959.mkv", "20211117_083000-085959.mkv"], 
            ["20211117_110000-112959.mkv", "20211117_113000-115959.mkv", "20211117_120000-122959.mkv", "20211117_123000-125959.mkv"],
            ["20211117_170000-172959.mkv", "20211117_173000-175959.mkv", "20211117_180000-182959.mkv", "20211117_183000-185959.mkv"]]

FileTitle = ["20211117_070000-085959", "20211117_110000-125959", "20211117_170000-185959"]

for Site_ in SitePATH:
    FullPATH = VideoPATH + Site_ + DatePATH

    if not(os.path.isdir(FullPATH)):
        print("[ERROR] Invalid site : " + Site_)
        continue

    for tIdx in range(0, len(FileTitle)):
        VideoList = TargetFiles[tIdx]
        Video2H = VideoFileClip(FullPATH + VideoList[0], audio=False)

        for vIdx in range(1, len(VideoList)):
            Video30M = VideoFileClip(FullPATH + VideoList[vIdx], audio=False)
            Video2H = concatenate_videoclips([Video2H, Video30M])

        Video2H.write_videofile(DestPATH + Site_ + "_" + FileTitle[tIdx] + ".mp4")

        Video30M.close()
        Video2H.close()

# Video24H = VideoFileClip("22번 내각.mp4", audio=False)
# Video30M = VideoFileClip("23번 내각.mp4", audio=False)

# Video24H = concatenate_videoclips([Video24H, Video30M])
# Video24H.write_videofile("Video24H.mp4")