

from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model = YOLO('yolov8n.pt')

results = model.train(data='coco128.yaml', epochs=3)

results = model.val()

results = model('https://ultralytics.com/images/bus.jpg')

success = model.export(format='onnx')