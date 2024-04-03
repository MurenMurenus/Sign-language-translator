# Важно!

## Datasets:
1) Sign_language_dataset
2) MNIST sign language dataset https://www.kaggle.com/datasets/datamunge/sign-language-mnist?resource=download
3) https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset

## Для получения итогового датасета под обчуение:
1. Скачать Sign language dataset по [ссылке](https://drive.google.com/file/d/1ONW7ImAmRkMDOEAY-wQu_A5y3HI4NqBg/view?usp=sharing)
2. Скачать MNIST датасет и ASL датасет
3. Раскидать изображения из MNIST датасета в sign_language_dataset, запустив csv_to_img.py (тк MNIST существует в формате csv)
4. Раскидать изображения из asl_alphabet_train в sign_language_dataset, запустив asl_add.py
5. Разделить sign_language_dataset на train, val и test, запустив script.py
5. Изменить пути в конфигах conf/data/sign_train.yaml и /conf/data/sign_test.yaml до получившихся train, val и test