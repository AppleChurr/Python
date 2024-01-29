# E2Box_9axis

## 개요
- `E2Box_9axis.py`는 9축 센서 데이터를 시리얼 포트를 통해 읽어와서 실시간으로 그래프로 표시하는 파이썬 스크립트입니다.

## 기능
- 롤(Roll), 피치(Pitch), 요(Yaw), X/Y/Z 축 가속도계 데이터를 실시간으로 그래프로 표시합니다.
- matplotlib을 사용하여 데이터를 시각화합니다.
- NumPy를 활용하여 데이터 처리를 수행합니다.

## 사용 방법
- 스크립트를 실행하기 전에 시리얼 포트와 연결된 9축 센서 장치가 필요합니다.
- `serial_port`와 `baud_rate`는 센서와 연결된 시리얼 포트 설정에 맞게 조정해야 합니다.
- 스크립트 실행 시 센서 데이터에 따라 그래프가 실시간으로 업데이트됩니다.

## 주의사항
- 시리얼 포트 설정이 올바르지 않으면 데이터를 읽지 못할 수 있습니다.
- matplotlib 및 NumPy 라이브러리가 필요합니다.