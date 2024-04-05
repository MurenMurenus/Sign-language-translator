from efficientnet_pytorch import EfficientNet


def get_efficientnet_model(num_classes: int = 29):
    model = EfficientNet.from_pretrained('efficientnet-b0', num_classes=num_classes)
    return model
