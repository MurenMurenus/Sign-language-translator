import os

import cv2

def main():
    DATA_DIR = 'sign_language_dataset'
    #iter = 1

    for dirpath, _, filenames in os.walk(DATA_DIR):

        #print("Iteraration: ", iter)
        #iter += 1

        for img_name in filenames:
            img_path = os.path.join(dirpath, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (200, 200))
            cv2.imwrite(img_path, img)

if __name__ == '__main__':
    main()

