from pathlib import Path
from typing import List

import cv2
import numpy as np
import mediapipe as mp
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets
from torchvision import transforms


class SignDataset(Dataset):
    def __init__(self, paths: List[Path], transform=None):
        self.paths = paths
        self.transform = transform # если есть аугментации

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        labels = sorted(set(str(x).split('/')[-2] for x in paths))
        self.one_hot_encoding = {label: i for i, label in enumerate(labels)}

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        image = cv2.imread(str(self.paths[idx]))
        label = str(self.paths[idx]).split('/')[-2]
        with self.mp_hands.Hands(
                static_image_mode=True,
                max_num_hands=2,
                min_detection_confidence=0.2) as hands:
            results = hands.process(cv2.flip(image, 1))
            if results.multi_hand_landmarks:
                annotated_image = cv2.flip(image.copy(), 1)
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        annotated_image,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style())
                image = cv2.flip(annotated_image, 1)

        image = cv2.resize(image, (200, 200))
        image = np.transpose(image, (2, 0, 1))

        return torch.tensor(image).float(), torch.tensor(self.one_hot_encoding[label])


def get_sign_dataloader(
        path_train, path_val, batch_size, shuffle=True, num_workers=1,
    ):
    transform = transforms.Compose([
        transforms.RandomRotation(10, fill=0),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.5)
    ])

    train_dataset = SignDataset(paths=[*Path(path_train).rglob('*.jpg')], transform=transform)
    val_dataset = SignDataset(paths=[*Path(path_val).rglob('*.jpg')])
    # print("STARTED")
    # train_dataset = pickle.load(open(path_train, "rb"))
    # val_dataset = pickle.load(open(path_val, "rb"))
    # print("Number of training samples: ", len(train_dataset))
    # print("Number of validation samples: ", len(val_dataset))


    loader_args = {
        'batch_size': batch_size,
        'shuffle': shuffle,
        'num_workers': num_workers
    }
    return DataLoader(train_dataset, **loader_args), DataLoader(val_dataset, **loader_args)


def get_sign_test_dataloader(
        path_test, batch_size, num_workers=1,
    ):
    test_dataset = SignDataset(paths=[*Path(path_test).rglob('*.jpg')])
    # test_dataset = pickle.load(open(path_test, "rb"))
    # print("Number of test samples: ", len(test_dataset))

    loader_args = {
        'batch_size': batch_size,
        'shuffle': False,
        'num_workers': num_workers
    }
    return DataLoader(test_dataset, **loader_args)
