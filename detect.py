import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('your_weight') # select your model.pt path
    model.predict(source='data_path',  # /CV/xhr_dataset/Visdrone/VisDrone2019-DET-test-dev/images
                  imgsz=640,
                  project='runs/detect',
                  save=True,
                  conf=0.25,
                  save_txt=False, # save results as .txt file
                  # save_crop=True, # save cropped images with results
                )