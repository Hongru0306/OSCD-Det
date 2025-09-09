import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('./runs/train/exp5/weights/best.pt') # best.pt
    metrics = model.val(data='./data/hrsc.yaml',
              split='test', # split可以选择train、val、test 根据自己的数据集情况来选择.
              imgsz=640,
              batch=16,
              # iou=0.7,
              # rect=False,
            #   save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )
    
    print('map:', metrics.box.map)  # mAP50-95
    print('map50:', metrics.box.map50)  # mAP50
    print('map75:', metrics.box.map75)  # mAP75
    # print(metrics.box.maps)
    print('mp:', metrics.box.mp)
    print('mr:', metrics.box.mr)