import torch
import cv2
import numpy as np
from init_model import get_trained_model


def photo_sign_recognition(path: str) -> str:
    model = get_trained_model('saved.pt')
    classes = "abcdefghijklmnopqrstuvwhyz*? "

    frame = cv2.imread(path)
    max_side = max(frame.shape[0:2])
    old_image_height, old_image_width, channels = frame.shape
    color = (255, 255, 255)

    padded = np.full((max_side, max_side, channels), color, dtype=np.uint8)

    # copy img image into center of result image
    padded[0:old_image_height,
    0:old_image_width] = frame

    image = cv2.resize(padded, (200, 200))
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
