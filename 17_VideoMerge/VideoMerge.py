from moviepy.editor import *


VideoPATH = "D:\\20_Data\\[20220113] 화성 26번 개소 영상\\"
DestPATH = "D:\\20_Data\\[20220113] 화성 26번 개소 영상\\"

TargetFiles = [
            #["[20220113][124000]_video_125000.avi", "[20220113][125000]_video_130000.avi", "[20220113][130000]_video_131000.avi", 
            #"[20220113][131000]_video_132000.avi", "[20220113][132000]_video_133000.avi", "[20220113][133000]_video_134000.avi",], 
            [ "[20220113][134000]_video_135000.avi", "[20220113][135000]_video_140000.avi", "[20220113][140000]_video_141000.avi", 
            "[20220113][141000]_video_142000.avi", "[20220113][142000]_video_143000.avi", "[20220113][143000]_video_144000.avi"]
            ]

DestFiles = [#"[20220113][124000_134000]", 
            "[20220113][134000_144000]"]

dIdx = 0

for Targets_ in TargetFiles:

    Video1H = VideoFileClip(VideoPATH + Targets_[0], audio=False)

    for vIdx in range(1, len(Targets_)):
        Video10M = VideoFileClip(VideoPATH + Targets_[vIdx], audio=False)
        Video1H = concatenate_videoclips([Video1H, Video10M])

    Video1H.write_videofile(DestPATH + DestFiles[dIdx] + ".mp4")

    Video10M.close()
    Video1H.close()

    dIdx = dIdx + 1