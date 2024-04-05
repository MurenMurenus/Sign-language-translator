import torch
import cv2
import numpy as np
from init_model import get_trained_model


def video_sign_recognition(path: str) -> str:
    model = get_trained_model('saved.pt')
    classes = "abcdefghijklmnopqrstuvwhyz*? "
    confidence = 0.92
    check_freq = 15
    cap = cv2.VideoCapture(path)

    num_frames = 1
    answer = ""
    previous_sign = ""
    sign = ""

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if num_frames == check_freq:
            max_side = max(frame.shape[0:2])
            old_image_height, old_image_width, channels = frame.shape
            color = (255, 255, 255)

            padded = np.full((max_side, max_side, channels), color, dtype=np.uint8)

            # copy img image into center of result image
            padded[0:old_image_height,
            0:old_image_width] = frame

            image = cv2.resize(padded, (200, 200))
            image = np.transpose(image, (2, 0, 1))
            model.eval()
            image = torch.tensor(image).float()
            with torch.no_grad():
                predict = model(image.unsqueeze(0))

            predicted_class = torch.nn.functional.softmax(predict, dim=-1).max(1)

            if predicted_class.values[0] < confidence:
                continue
            num_class = predicted_class.indices[0]
            sign = classes[num_class]

            if sign != previous_sign:
                if sign == '*':
                    if len(answer) > 1:
                        answer = answer[0:-2]
                elif sign == '?':
                    previous_sign = sign
                    continue
                else:
                    answer += sign
                previous_sign = sign

            num_frames = 1

        num_frames = num_frames + 1

    return answer

