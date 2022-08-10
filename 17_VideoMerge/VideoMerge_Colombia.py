from moviepy.editor import *

VideoPATH = "\\\\192.168.0.253\\Shared2_CCTV_AI\\[20211124] 콜롬비아 2차\\영상_2차년도\\"
SavePATH = "D:\\02_Python\\17_VideoMerge\\콜롬비아 2차\\"

if not(os.path.isdir(SavePATH)):
    os.makedirs(os.path.join(SavePATH))

# 1시간 영상
# 43번

# 33번 주간 불연속

Video = [
        # ["1. VDS-027(30)\\27-1\\", "[20211123][090000]_video.mp4", "[20211123][093000]_video.mp4", "01. VDS-027(30)-1-D-090000.mp4"], 
        # ["1. VDS-027(30)\\27-1\\", "[20211123][230000]_video.mp4", "[20211123][233000]_video.mp4", "01. VDS-027(30)-1-N-230000.mp4"], 
        # ["1. VDS-027(30)\\27-2\\", "[20211124][143000]_video.mp4", "[20211124][150000]_video.mp4", "01. VDS-027(30)-2-D-143000.mp4"],
        # ["1. VDS-027(30)\\27-2\\", "[20211124][203000]_video.mp4", "[20211124][210000]_video.mp4", "01. VDS-027(30)-2-N-203000.mp4"],
        # ["2. VDS-031(35)\\", "[20211125][093000]_video.mp4", "[20211125][100000]_video.mp4", "02. VDS-031(35)-N-193000.mp4"],
        # ["5. VDS-035(40)\\", "[20211124][023000]_video.mp4", "[20211124][030000]_video.mp4", "05. VDS-035(40)-D-123000.mp4"],
        # ["6. VDS-034(39)\\34-1\\", "[20211129][183000]_video.mp4", "[20211129][190000]_video.mp4", "06. VDS-034(39)-1-N-183000.mp4"],
        # ["6. VDS-034(39)\\34-1\\", "[20211129][210000]_video.mp4", "[20211129][213000]_video.mp4", "06. VDS-034(39)-1-D-090000.mp4"],
        # ["6. VDS-034(39)\\34-2\\", "[20211128][203000]_video.mp4", "[20211128][210000]_video.mp4", "06. VDS-034(39)-2-D-083000.mp4"],
        # ["8. VDS-029(32)\\29-1\\", "[20211123][080000]_video.mp4", "[20211123][083000]_video.mp4", "08. VDS-029(32)-1-N-200000.mp4"],
        # ["8. VDS-029(32)\\29-1\\", "[20211124][010000]_video.mp4", "[20211124][013000]_video.mp4", "08. VDS-029(32)-1-D-130000.mp4"],
        # ["8. VDS-029(32)\\29-2\\", "[20211124][170000]_video.mp4", "[20211124][173000]_video.mp4", "08. VDS-029(32)-2-N-190000.mp4"],
        # ["8. VDS-029(32)\\29-2\\", "[20211125][000000]_video.mp4", "[20211125][003000]_video.mp4", "08. VDS-029(32)-2-D-140000.mp4"],
        # ["9. VDS-036(41)\\36-1\\", "[20211129][200000]_video.mp4", "[20211129][203000]_video.mp4", "09. VDS-036(41)-1-D-100000.mp4"],
        # ["9. VDS-036(41)\\36-1\\", "[20211130][100000]_video.mp4", "[20211130][103000]_video.mp4", "09. VDS-036(41)-1-N-200000.mp4"],
        # ["9. VDS-036(41)\\36-2\\", "[20211205][153000]_video.mp4", "[20211205][160000]_video.mp4", "09. VDS-036(41)-2-N-000000.mp4"],
        # ["9. VDS-036(41)\\36-2\\", "[20211206][000000]_video.mp4", "[20211206][003000]_video.mp4", "09. VDS-036(41)-2-D-120000.mp4"],
        # ["12. VDS-033(38)\\1번\\", "[20211123][100000]_video.mp4", "[20211123][103000]_video.mp4", "12. VDS-033(38)-1-N-220000.mp4"],
        # ["12. VDS-033(38)\\2번\\", "[20211127][013000]_video.mp4", "[20211127][020000]_video.mp4", "12. VDS-033(38)-2-D-133000.mp4"],
        # ["12. VDS-033(38)\\2번\\", "[20211127][083000]_video.mp4", "[20211127][090000]_video.mp4", "12. VDS-033(38)-2-N-203000.mp4"],
        # ["14. VDS-044(56)\\", "[20211129][010000]_video.mp4", "[20211129][013000]_video.mp4", "14. VDS-044(56)-D-130000.mp4"],
        # ["14. VDS-044(56)\\", "[20211129][103000]_video.mp4", "[20211129][110000]_video.mp4", "14. VDS-044(56)-N-223000.mp4"],
        # ["32. V-V032(36)\\32-1\\", "[20211129][223000]_video.mp4", "[20211129][230000]_video.mp4", "32. V-V032(36)-1-D-103000.mp4"],
        # ["32. V-V032(36)\\32-1\\", "[20211130][123000]_video.mp4", "[20211130][130000]_video.mp4", "32. V-V032(36)-1-N-203000.mp4"],
        # ["32. V-V032(36)\\32-2\\", "[20211202][213000]_video.mp4", "[20211202][220000]_video.mp4", "32. V-V032(36)-2-D-100000.mp4"],
        # ["32. V-V032(36)\\32-3\\", "[20211202][220000]_video.mp4", "[20211202][223000]_video.mp4", "32. V-V032(36)-3-D-100000.mp4"],
        # ["39. V-V039(48)\\39-1\\", "[20211208][053000]_video.mp4", "[20211208][060000]_video.mp4", "39. V-V039(48)-1-D-053000.mp4"],
        # ["39. V-V039(48)\\39-2\\", "[20211208][230000]_video.mp4",                                   "39. V-V039(48)-2-D-140000.mp4"],
        # ["41. V-V041(50)\\VDS41-1\\", "[20211203][223000]_video.mp4", "[20211203][230000]_video.mp4", "41. V-V041(50)-1-D-130000.mp4"],
        # ["41. V-V041(50)\\VDS41-1\\", "[20211204][090000]_video.mp4", "[20211204][093000]_video.mp4", "41. V-V041(50)-1-N-233000.mp4"],
        # ["41. V-V041(50)\\VDS41-2\\", "[20211130][010000]_video.mp4", "[20211130][013000]_video.mp4", "41. V-V041(50)-2-D-130000.mp4"],
        # ["41. V-V041(50)\\VDS41-2\\", "[20211130][110000]_video.mp4", "[20211130][113000]_video.mp4", "41. V-V041(50)-2-N-230000.mp4"],
        # ["7. VDS-040(49)\\40-3\\", "[20211205][150000]_video.mp4", "[20211205][153000]_video.mp4", "07. VDS-040(49)-3-D-150000.mp4"],
        # ["23. V-V023(23)\\1\\", "[20211204][003000]_video.mp4", "[20211204][010000]_video.mp4", "23. V-V023(23)-1-D-130000.mp4"],
        # ["23. V-V023(23)\\2\\", "[20211204][003000]_video.mp4", "[20211204][010000]_video.mp4", "23. V-V023(23)-2-D-130000.mp4"],
        # ["23. V-V023(23)\\3\\", "[20211209][230000]_video.mp4", "[20211209][233000]_video.mp4", "23. V-V023(23)-3-D-110000.mp4"],
        # ["23. V-V023(23)\\4\\", "[20211209][230000]_video.mp4", "[20211209][233000]_video.mp4", "23. V-V023(23)-4-D-110000.mp4"],
        # ["37. V-V037(42)\\1\\", "[20211211][023000]_video.mp4", "[20211211][030000]_video.mp4", "37. V-V037(42)-1-D-143000.mp4"],
        # ["37. V-V037(42)\\2\\", "[20211211][023000]_video.mp4", "[20211211][030000]_video.mp4", "37. V-V037(42)-2-D-143000.mp4"],
        # ["38. V-V038(43)\\1\\", "[20211209][090000]_video.mp4", "[20211209][093000]_video.mp4", "38. V-V038(43)-1-D-090000.mp4"],
        # ["38. V-V038(43)\\2\\", "[20211209][090000]_video.mp4", "[20211209][093000]_video.mp4", "38. V-V038(43)-2-D-090000.mp4"],
        # ["12. VDS-033(38)\\1번\\", "[20211123][020000]_video.mp4", "[20211123][203000]_video.mp4", "12. VDS-033(38)-1-D-140000.mp4"],
        # ["2. VDS-031(35)\\", "[20211125][053000]_video.mp4", "[20211125][060000]_video.mp4", "02. VDS-031(35)-D-153000.mp4"],
        ]


for Video_ in Video:
    if len(Video_) == 3:
        CamVideoPATH = VideoPATH + Video_[0]
        PrevVideo = VideoFileClip(CamVideoPATH + Video_[1], audio=False)
        PrevVideo.write_videofile(SavePATH + Video_[2])
    elif len(Video_) == 4:
        CamVideoPATH = VideoPATH + Video_[0]

        PrevVideo = VideoFileClip(CamVideoPATH + Video_[1], audio=False)
        print(CamVideoPATH + Video_[2], end=" <<+>> ")
        NextVideo = VideoFileClip(CamVideoPATH + Video_[2], audio=False)
        print(CamVideoPATH + Video_[2])

        MergeVedeo = concatenate_videoclips([PrevVideo, NextVideo])
        MergeVedeo.write_videofile(SavePATH + Video_[3])