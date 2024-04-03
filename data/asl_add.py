import os
from torchvision import datasets

DATA_DIR_OUT = 'sign_language_dataset'
DATA_DIR_IN = 'asl_alphabet_train'

dataset = datasets.ImageFolder(DATA_DIR_IN)
iterr = 0
for item in dataset:
    if iterr % 1000 == 0:
        print("Dataset:", iterr)
    img, cls = item
    class_name = dataset.classes[cls]
    if not os.path.exists(f'{DATA_DIR_OUT}/{class_name}'):
        os.makedirs(f'{DATA_DIR_OUT}/{class_name}')
    img.save(f'{DATA_DIR_OUT}/{class_name}/{class_name}{iterr}_kaggle.jpg')
    iterr += 1
