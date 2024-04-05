import torch
import cv2
import numpy as np
from init_model import get_trained_model


def photo_sign_recognition(path: str) -> str:
    model = get_trained_model('saved.pt')
    classes = "abcdefghijklmnopqrstuvwhyz*? "

    image = cv2.imread(path)
    image = cv2.resize(image, (200, 200))
    image = np.transpose(image, (2, 0, 1))

    model.eval()
    image = torch.tensor(image).float()
    with torch.no_grad():
        predict = model(image.unsqueeze(0))
    predicted_class = torch.nn.functional.softmax(predict, dim=-1).max(1)

    # predicted_class = np.argmax(predict)
    print(predicted_class)

    if predicted_class.values[0] < 0.5:
        return "Cannot recognize: I'm not sure about the result, try again"

    num_class = predicted_class.indices[0]
    sign = classes[num_class]

    if sign == '*':
        return 'delete'
    elif sign == '?':
        return 'nothing'
    elif sign == ' ':
        return 'space'
    return sign


if __name__ == '__main__':
    result = photo_sign_recognition('bot_data/photos/test_B.jpg')
    print(result)
