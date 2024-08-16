# Get Started



## Train model
1. dataset file: garbage.yaml
2. change train.py main func
```python
if __name__ == '__main__':
    train()
```
3. train
```bash
python3 train.py
```

## export model to onnx
1. change ultralytics/cfg/default.yaml model config
   model: D:\\AndroidProject\\rk3588_ultralytics_yolov8\\best.pt
2. change train.py main func and add export func to main
```bash
if __name__ == '__main__':
    export()
```

## convert model to rknn 
1. Configure RKNN-Toolkit2 Environment on PC
```bash
p# Create Projects folder
mkdir Projects
cd Projects
# Download RKNN-Toolkit2 repository
git clone https://github.com/airockchip/rknn-toolkit2.git 
# Download RKNN Model Zoo repository
git clone https://github.com/airockchip/rknn_model_zoo.git
# Navigate to the rknn-toolkit2 directory
cd Projects/rknn-toolkit2/rknn-toolkit2
# Choose the appropriate requirements file according to your python version
pip install -r packages/requirements_cp310-x.x.x.txt -i https://mirror.baidu.com/pypi/simple
# Choose the appropriate wheel package file according to your python version and processor architecture:
pip install packages/rknn_toolkit2-x.x.x+708089d1-cp310-cp310-linux_x86_64.whl
```
2. Verify if the installation is successful
```bash
$ python3
>>> from rknn.api import RKNN
```
3. convert onnx to rknn
```bash
cd rknn_model_zoo/examples/yolov8/python
python3 convert.py best.onnx rk3588
```

4. Run the yolov8 example program
```bash
cd rknn_model_zoo/examples/yolov8/python
sudo python3 yolov8.py --model_path best.rknn --img_save
```


# ref: 
1. rknn model example: https://github.com/airockchip/rknn_model_zoo
2. toolkit package: https://github.com/airockchip/rknn-toolkit2
3. rknn install: https://docs.radxa.com/en/rock5/rock5c/app-development/rknn_install
4. convert and deploy: https://docs.radxa.com/en/rock5/rock5c/app-development/rknn_install







