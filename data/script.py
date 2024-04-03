import os
import torch
from torch.utils.data import random_split
from torchvision import datasets


def main():
    DATA_DIR = 'sign_language_dataset'
    dataset = datasets.ImageFolder(DATA_DIR)

    proportions = [.6, .2, .2]
    lengths = [int(p * len(dataset)) for p in proportions]
    lengths[-1] = len(dataset) - sum(lengths[:-1])
    train_data, test_data, val_data = torch.utils.data.random_split(dataset, lengths)

    print(len(train_data))
    print(len(test_data))
    print(len(val_data))
    # torch.save(train_data, f'{DATA_DIR}_train.pt')
    # torch.save(test_data, f'{DATA_DIR}_test.pt')
    # torch.save(val_data, f'{DATA_DIR}_val.pt')
    # with open(f'{DATA_DIR}_train.pkl', 'wb') as train_data_file:
    #     pickle.dump(train_data, train_data_file)
    # with open(f'{DATA_DIR}_test.pkl', 'wb') as test_data_file:
    #     pickle.dump(test_data, test_data_file)
    # with open(f'{DATA_DIR}_val.pkl', 'wb') as val_data_file:
    #     pickle.dump(val_data, val_data_file)

    iterr = 0
    for item in train_data:
        img, cls = item
        class_name = dataset.classes[cls]
        if iterr % 1000 == 0:
            print("Train:", iterr)

        if not os.path.exists(f'{DATA_DIR}_train/{class_name}'):
            os.makedirs(f'{DATA_DIR}_train/{class_name}')
        img.save(f'{DATA_DIR}_train/{class_name}/{class_name}{iterr}.jpg')
        iterr += 1

    iterr = 0
    for item in test_data:
        img, cls = item
        class_name = dataset.classes[cls]
        if iterr % 1000 == 0:
            print("Test:", iterr)

        if not os.path.exists(f'{DATA_DIR}_test/{class_name}'):
            os.makedirs(f'{DATA_DIR}_test/{class_name}')
        img.save(f'{DATA_DIR}_test/{class_name}/{class_name}{iterr}.jpg')
        iterr += 1

    iterr = 0
    for item in val_data:
        img, cls = item
        class_name = dataset.classes[cls]
        if iterr % 1000 == 0:
            print("Val:", iterr)

        if not os.path.exists(f'{DATA_DIR}_val/{class_name}'):
            os.makedirs(f'{DATA_DIR}_val/{class_name}')
        img.save(f'{DATA_DIR}_val/{class_name}/{class_name}{iterr}.jpg')
        iterr += 1


if __name__ == '__main__':
    main()
