from datetime import datetime 
from typing import List
import torch

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Data ingestion constants
ARTIFACTS_DIR: str = "artifacts"
FOLDER_NAME = "Data"
GD_ZIP_FILE_PATH = "https://drive.google.com/file/d/1lrZNdDcrlHWY6Te2sl-3d5aQ3HaoB1Ke/view?usp=sharing"
ZIP_FILE_NAME = 'Xray_dataset.zip'
DATA_INGESTION_DATA_DIR = "data"

# data transfomation constants
CLASS_LABEL1: str = "NORMAL"
CLASS_LABEL2: str = "PNEUMONIA"
BRIGHTNESS: int = 0.10
CONTRAST: int = 0.1
SATURATION: int = 0.10
HUE: int = 0.1
RESIZE: int = 224
CENTERCROP: int = 224
RANDOMROTATION: int = 10
NORMALIZE_LIST_1: List[int] = [0.485, 0.456, 0.406]
NORMALIZE_LIST_2: List[int] = [0.229, 0.224, 0.225]
TRAIN_TRANSFORMS_KEY: str = "xray_train_transforms"
TRAIN_TRANSFORMS_FILE: str = "train_transforms.pkl"
TEST_TRANSFORMS_FILE: str = "test_transforms.pkl"
BATCH_SIZE: int = 2
SHUFFLE: bool = False
PIN_MEMORY: bool = True


# model trainer constants
TRAINED_MODEL_DIR: str = "trained_model"
TRAINED_MODEL_MNAME: str = "model.pt"
DEVICE: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
STEP_SIZE: int = 6
GAMMA: int = 0.5
EPOCH: int = 1

BENTOML_MODEL_NAME: str = "xray_model"

BENTOML_SERVICE_NAME: str = "xray_service"

BENTOML_ECR_URI: str = "xray_bento_image"

PREDICTION_LABEL: dict = {"0": CLASS_LABEL1, 1: CLASS_LABEL2}