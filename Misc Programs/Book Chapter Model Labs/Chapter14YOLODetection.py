# Raghav Sriram

import pandas as pd
import os
import numpy as np
import shutil
import ast
from sklearn import model_selection
from tqdm import tqdm
import wandb
from sklearn.model_selection import GroupKFold
from IPython.display import Image, clear_output  # to display images
from os import listdir
from os.path import isfile
from glob import glob
import yaml
# clear_output()

TRAIN_LABELS_PATH = './vinbigdata/labels/train'
VAL_LABELS_PATH = './vinbigdata/labels/val'
TRAIN_IMAGES_PATH = './vinbigdata/images/train' #12000
VAL_IMAGES_PATH = './vinbigdata/images/val' #3000
External_DIR = '../input/vinbigdata-512-image-dataset/vinbigdata/train' # 15000
os.makedirs(TRAIN_LABELS_PATH, exist_ok = True)
os.makedirs(VAL_LABELS_PATH, exist_ok = True)
os.makedirs(TRAIN_IMAGES_PATH, exist_ok = True)
os.makedirs(VAL_IMAGES_PATH, exist_ok = True)
size = 51

df = pd.read_csv('../input/vinbigdata-512-image-dataset/vinbigdata/train.csv')
df.head()
df = df[df.class_id!=14].reset_index(drop = True)

df['x_min'] = df.apply(lambda row: (row.x_min)/row.width, axis = 1)*float(size)
df['y_min'] = df.apply(lambda row: (row.y_min)/row.height, axis = 1)*float(size)
df['x_max'] = df.apply(lambda row: (row.x_max)/row.width, axis =1)*float(size)
df['y_max'] = df.apply(lambda row: (row.y_max)/row.height, axis =1)*float(size)

df['x_mid'] = df.apply(lambda row: (row.x_max+row.x_min)/2, axis =1)
df['y_mid'] = df.apply(lambda row: (row.y_max+row.y_min)/2, axis =1)

df['w'] = df.apply(lambda row: (row.x_max-row.x_min), axis =1)
df['h'] = df.apply(lambda row: (row.y_max-row.y_min), axis =1)

df['x_mid'] /= float(size)
df['y_mid'] /= float(size)

df['w'] /= float(size)
df['h'] /= float(size)

# <class> <x_center> <y_center> <width> <height>
def preproccess_data(df, labels_path, images_path):
    for column, row in tqdm(df.iterrows(), total=len(df)):
        attributes = row[['class_id','x_mid','y_mid','w','h']].values
        attributes = np.array(attributes)
        np.savetxt(os.path.join(labels_path, f"{row['image_id']}.txt"),
                   [attributes], fmt = ['%d', '%f', '%f', '%f', '%f'])
        shutil.copy(os.path.join('/kaggle/input/vinbigdata-512-image-dataset/vinbigdata/train', f"{row['image_id']}.png"),images_path)

preproccess_data(df, TRAIN_LABELS_PATH, TRAIN_IMAGES_PATH)
preproccess_data(val_df, VAL_LABELS_PATH, VAL_IMAGES_PATH)

classes = [ 'Aortic enlargement',
            'Atelectasis',
            'Calcification',
            'Cardiomegaly',
            'Consolidation',
            'ILD',
            'Infiltration',
            'Lung Opacity',
            'Nodule/Mass',
            'Other lesion',
            'Pleural effusion',
            'Pleural thickening',
            'Pneumothorax',
            'Pulmonary fibrosis']

data = dict(
    train =  '../vinbigdata/images/train',
    val   =  '../vinbigdata/images/val',
    nc    = 14,
    names = classes
    )

with open('./yolov5/vinbigdata.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

f = open('./yolov5/vinbigdata.yaml', 'r')
print('\nyaml:')
print(f.read())

# b39dd18eed49a73a53fccd7b684ea7ecaed75b08
wandb.login()
test_dir = f'/kaggle/input/vinbigdata-{size}-image-dataset/vinbigdata/test'
weights_dir = './runs/train/vin3/weights/best.pt'
os.listdir('./runs/train/vin3/weights')