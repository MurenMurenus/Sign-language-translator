import torchvision


def get_mobilenet_model(num_classes: int = 29):
    model = torchvision.models.mobilenet_v3_small(weights=torchvision.models.mobilenet.MobileNet_V3_Small_Weights)
    model.classifier[-1].out_features = num_classes
    return model
