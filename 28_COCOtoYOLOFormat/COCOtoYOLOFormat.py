import os
import json
import shutil

LABEL_PATH = "라벨링데이터\\TL_1.금실1\\"
IMAGE_PATH = "원천데이터\\TS_1.금실1\\"

SAVE_PATH = "YOLOData\\"

FROM_LABEL_EXT = ".json"
TO_LABEL_EXT = ".txt"

IMAGE_EXT = ".jpg"

LABEL_DIC ={'잎':0, '줄기':1, '화방':2, '과실':3}

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

lLabel = os.listdir(LABEL_PATH)
lImage = os.listdir(IMAGE_PATH)

lLabelName =  [lName.replace(FROM_LABEL_EXT, "") for lName in lLabel]
lImageName =  [lName.replace(IMAGE_EXT, "") for lName in lImage]

for iName in lImageName:
    lFileName = list(set([iName]).intersection(set(lLabelName)))
    
    if len(lFileName) == 1:
        lYoloData = []
        fName = lFileName[0]
        print(fName)

        with open(LABEL_PATH + fName + FROM_LABEL_EXT, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # print(data)

        images = data['images']
        image_id = images['image_id']
    
        imgW = float(images['width'])
        imgH = float(images['height'])

        annotations = data['annotations']

        for annotation in annotations:
            if(annotation['image_id'] != image_id):
                continue

            bbox = annotation['bbox']
            category_id = annotation['category_id']

            for category in data['categories']:
                if category['id'] == category_id:
                    desired_name = category['name']
                    break

            print('\tcategory:', LABEL_DIC[desired_name], ' bbox:', bbox)
            
            w = bbox[2] / imgW
            h = bbox[3] / imgH
            
            x = (bbox[0] / imgW) + w / 2
            y = (bbox[1] / imgH) + h / 2
            
            lYoloData.append({'category': LABEL_DIC[desired_name], 'x': x, 'y': y, 'w': w, 'h': h})

        output_file_path = SAVE_PATH + fName + TO_LABEL_EXT
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for item in lYoloData:
                output_file.write(f"{item['category']} {item['x']:.4f} {item['y']:.4f} {item['w']:.4f} {item['h']:.4f}\n")


        shutil.copy(IMAGE_PATH + fName + IMAGE_EXT, SAVE_PATH + fName + IMAGE_EXT)

