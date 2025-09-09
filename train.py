import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
# from swanlab.integration.ultralytics import add_swanlab_callback


if __name__ == '__main__':
    model = YOLO('./ours-obb.yaml') 
    # ./configs/ours.yaml

    model.train(data='./data/hrsc.yaml', # ./data/OSC.yaml / ./data/hrsc.yaml
                cache=False,
                imgsz=640,
                epochs=400,
                batch=16,
                workers=4,
                device='0',
                # resume=True, # 断点续训,YOLO初始化时选择last.pt,
                # pretrained=False, 
                # amp=False, # close amp
                project='runs/train',
                name='exp',
                )