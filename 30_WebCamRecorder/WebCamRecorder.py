import os
import cv2
import numpy as np
import datetime
import argparse

def create_output_file(save_path):
    today_folder = os.path.join(save_path, datetime.datetime.now().strftime("%Y%m%d"))

    print(today_folder)

    # 폴더가 없으면 생성
    if not os.path.exists(today_folder):
        os.makedirs(today_folder)

    # 녹화 시작 시간을 기준으로 파일 이름 생성
    start_time_str = start_time.strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(today_folder, f"recorded_video_{start_time_str}.avi")
    
    # 녹화 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (frame_width, frame_height))
    
    return out, output_file


def parse_args():
    parser = argparse.ArgumentParser(description="웹캠 녹화 프로그램")
    parser.add_argument("--webcam_index", type=int, default=0, help="사용할 웹캠의 인덱스 (기본값: 0)")
    parser.add_argument("--show_output", action="store_true", default=True, help="프레임을 화면에 표시할지 여부 (기본값: True)")
    parser.add_argument("--save_path", type=str, default=".", help="녹화 파일을 저장할 경로 (기본값: 현재 디렉토리)")
    parser.add_argument("--network_id", type=str, help="네트워크 드라이브 접근 ID")
    parser.add_argument("--network_pw", type=str, help="네트워크 드라이브 접근 PW")
    args = parser.parse_args()
    return args

# 명령행 인수 파싱
args = parse_args()

# 사용자가 help 옵션을 사용하면 도움말을 표시하고 프로그램 종료
if args.webcam_index is None and args.show_output is None:
    args.print_help()
    exit()

# 네트워크 드라이브에 연결
if args.network_id and args.network_pw:
    network_drive = os.path.join(args.save_path, "network_drive")
    os.system(f'net use {network_drive} {args.network_pw} /user:{args.network_id}')


# OpenCV 버전 확인
print("OpenCV Version:", cv2.__version__)

# 사용 가능한 웹캠의 수 확인
num_webcams = 10  # 임의로 설정한 최대 웹캠 수
for i in range(num_webcams):
    cap = cv2.VideoCapture(i)
    if not cap.isOpened():
        break
    print(f"Webcam {i}: {cap.get(3)}x{cap.get(4)}")
    cap.release()




# 웹캠 열기
cap = cv2.VideoCapture(args.webcam_index)

# 녹화 시작 시간 기록
start_time = datetime.datetime.now()

# 초기 녹화 파일 생성
out, current_output_file = create_output_file(network_drive if (args.network_id and args.network_pw) else args.save_path)

# 웹캠 정보 출력
print("Width:", cap.get(3))  # 프레임의 너비
print("Height:", cap.get(4))  # 프레임의 높이
print("Frames per Second:", cap.get(5))  # 초당 프레임 수
print("FourCC Code:", cap.get(6))  # 코덱 정보 (FourCC 코드)

# # 녹화 설정
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output_file = "recorded_video.avi"
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# out = cv2.VideoWriter(output_file, fourcc, 20.0, (frame_width, frame_height))

newVideo = True

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽혔는지 확인
    if not ret:
        continue

    # 현재 시간 계산 및 포맷 설정
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y %m %d %H:%M:%S")

    # 녹화 시간 및 현재 시간 출력
    elapsed_time = current_time - start_time
    # cv2.putText(frame, f"Recording: {elapsed_time}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, f"Real Time: {formatted_time}", (300, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1, cv2.LINE_AA)

    if args.show_output:
        cv2.imshow('WebCam Recording', frame)

    
    if current_time.minute == 0 and newVideo == False :
        newVideo = True
        out.release()  # 이전 녹화 파일 닫기
        out, current_output_file = create_output_file(network_drive if (args.network_id and args.network_pw) else args.save_path)  # 새로운 녹화 파일 생성
        start_time = current_time  # 새로운 녹화 시작 시간 갱신

    if current_time.minute > 0 :
        newVideo = False


    # 녹화 파일에 프레임 저장
    out.write(frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 네트워크 드라이브 접속 해제
if args.network_id and args.network_pw:
    os.system(f'net use {network_drive} /delete')

# 종료 시간 기록
end_time = datetime.datetime.now()

# 녹화 파일 및 웹캠 해제
out.release()
cap.release()
cv2.destroyAllWindows()
