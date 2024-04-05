import torch
from efficientnet_pytorch import EfficientNet


def get_trained_model(path: str) -> EfficientNet:
    model = EfficientNet.from_pretrained('efficientnet-b0', num_classes=29)
    model.load_state_dict(torch.load(path))

    return model
