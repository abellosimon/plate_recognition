from ultralytics import YOLO

#Load model 
license_model = YOLO("yolov8n.yaml") # build a new model 

#Use the model 
results = license_model.train(data="data.yaml", epochs=11) # train the model