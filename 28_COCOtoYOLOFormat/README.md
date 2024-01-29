
# COCOtoYOLOFormat

## 개요
- `COCOtoYOLOFormat.py`는 COCO 데이터셋 형식의 이미지 및 라벨 데이터를 YOLO 형식으로 변환하는 스크립트입니다.

## 기능
- JSON 형식의 COCO 라벨 파일을 읽어 YOLO 형식의 `.txt` 파일로 변환합니다.
- 이미지 파일을 YOLO 데이터셋에 맞게 복사합니다.
- 변환된 데이터는 지정된 경로에 저장됩니다.

## 사용 방법
- 원본 COCO 데이터셋이 있는 디렉토리에서 스크립트를 실행합니다. 스크립트는 자동으로 이미지와 라벨을 YOLO 형식으로 변환하여 저장합니다.

## 주의사항
- 올바른 변환을 위해 원본 COCO 데이터셋의 구조와 형식을 정확히 이해할 필요가 있습니다.