
from ultralytics import YOLO






def main():
    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from YAML
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights

    # Train the model
    results = model.train(data="garbage.yaml", epochs=100, imgsz=640, device=0)

    metrics = model.val()  # evaluate model performance on the validation set



def export():
    model = YOLO("yolov8n.yaml").load("best.pt")  # build from YAML and transfer weights
    results = model(
        "D:\\AndroidProject\\det_garbage_yolo\\test\\images\\85450f8f-802a-429e-811b-31de1382cfad.jpg")  # predict on an image
    path = model.export(format="onnx")  # export the model to ONNX format


if __name__ == '__main__':

    export()