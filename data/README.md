# Important!

## Datasets:
1) Sign_language_dataset
2) MNIST sign language dataset https://www.kaggle.com/datasets/datamunge/sign-language-mnist?resource=download
3) https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset

## ## To get the final dataset for training:
1. Download Sign language dataset by [link](https://drive.google.com/file/d/1ONW7ImAmRkMDOEAY-wQu_A5y3HI4NqBg/view?usp=sharing)
2. Download MNIST dataset and ASL dataset
3. Scatter images from MNIST dataset to sign_language_dataset by running csv_to_img.py (because MNIST is in csv format)
4. Scatter images from asl_alphabet_train to sign_language_dataset by running asl_add.py
5. Change the size of all images to 200 by 200 format by running resize_img.py
6. Split sign_language_dataset into train, val and test by running script.py
7. Change the paths in the configs conf/data/sign_train.yaml and /conf/data/sign_test.yaml to the resulting train, val and test