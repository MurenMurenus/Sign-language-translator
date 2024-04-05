import torch
import cv2
import numpy as np
from init_model import get_trained_model


def video_sign_recognition(path: str) -> str:
    model = get_trained_model('saved.pt')
    classes = "abcdefghijklmnopqrstuvwhyz*? "
    confidence = 0.82
    check_freq = 30
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
            image = cv2.resize(frame, (200, 200))
            image = np.transpose(image, (2, 0, 1))
            model.eval()
            image = torch.tensor(image).float()
            with torch.no_grad():
                predict = model(image.unsqueeze(0))

            predicted_class = torch.nn.functional.softmax(predict, dim=-1).max(1)

            # predicted_class = np.argmax(predict)
            # print(predicted_class)

            if predicted_class.values[0] < confidence:
                continue
            num_class = predicted_class.indices[0]
            # num_class = predicted_class.item()
            # if num_class < 26:
            sign = classes[num_class]
            # else:
            #     answer += str(num_class)

            if sign != previous_sign:
                if sign == '*':
                    if len(answer) > 1:
                        answer = answer[0:-2]
                elif sign == '?':
                    continue
                else:
                    answer += sign
                previous_sign = sign

            num_frames = 1

        num_frames = num_frames + 1

    return answer

