import cv2

def crop_and_save_video(input_path, output_path, start_x, start_y, width, height):
    # 동영상을 읽어옴
    video_capture = cv2.VideoCapture(input_path)

    # 동영상의 속성을 가져옴
    frame_width = int(video_capture.get(3))  # 프레임 너비
    frame_height = int(video_capture.get(4)) # 프레임 높이
    fps = video_capture.get(5)               # 초당 프레임 수

    # 출력 동영상을 저장할 객체 생성
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        # 동영상에서 한 프레임을 읽어옴
        ret, frame = video_capture.read()

        # 더 이상 프레임이 없으면 종료
        if not ret:
            break

        # 입력된 좌표와 크기로 프레임을 크롭
        cropped_frame = frame[start_y:start_y+height, start_x:start_x+width]

        # 크롭된 프레임을 출력 동영상에 추가
        out.write(cropped_frame)

    # 사용한 객체들을 해제
    video_capture.release()
    out.release()

# 입력 동영상 경로 및 출력 동영상 경로 설정
input_video_path = '1.avi'
output_video_path = '1_crop.avi'

# 크롭할 영역의 좌표와 크기 설정
crop_start_x = 0
crop_start_y = 0
crop_width = 400
crop_height = 4200

# 동영상 크롭 및 저장 함수 호출
crop_and_save_video(input_video_path, output_video_path, crop_start_x, crop_start_y, crop_width, crop_height)
