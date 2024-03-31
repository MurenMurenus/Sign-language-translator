import torch
from torchvision import datasets


def main():
    DATA_DIR = 'sign_language_dataset'
    dataset = datasets.ImageFolder(DATA_DIR)

    train_size = int(0.6 * len(dataset))
    test_size = int(0.2 * len(dataset))
    val_size = int(0.2 * len(dataset))

    train_data, test_data, val_data = torch.utils.data.random_split(dataset, [train_size, test_size, val_size])

    print(len(train_data))
    print(len(test_data))
    print(len(val_data))
    torch.save(train_data, f'{DATA_DIR}_train.pt')
    torch.save(test_data, f'{DATA_DIR}_test.pt')
    torch.save(val_data, f'{DATA_DIR}_val.pt')


if __name__ == '__main__':
    main()
