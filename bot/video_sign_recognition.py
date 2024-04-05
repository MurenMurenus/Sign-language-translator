import torch
import cv2
import numpy as np
from init_model import get_trained_model
#import torch.nn.functional as TF

def video_sign_recognition(path: str) -> str:
    model = get_trained_model('saved.pt')
    classes = "abcdefghijklmnopqrstuvwhyz"

    cap = cv2.VideoCapture(path)

    num_frames = 1
    answer = ""
    previous_sign = ""

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if num_frames == 20:
            image = cv2.resize(frame, (200, 200))
            image = np.transpose(image, (2, 0, 1))
            model.eval()
            image = torch.tensor(image).float()
            with torch.no_grad():
                predict = model(image.unsqueeze(0))

            print(predict)
            #predicted_class = TF.softmax(predict)
            predicted_class = np.argmax(predict)

            num_class = predicted_class.item()
            if num_class < 27:
                sign = classes[predicted_class.item()]
            else:
                answer += str(num_class)

            if sign != previous_sign:
                answer = answer + sign
                previous_sign = sign

            num_frames = 1

        num_frames = num_frames + 1

    return answer

if __name__ == '__main__':
    result = video_sign_recognition('bot_data/photos/test_B.jpg')
    print(result)
