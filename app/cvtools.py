import cv2 as cv
import os
class CvTools:
    def __init__(self):
        self.face_detector = cv.CascadeClassifier('app/cascade/haarcascade_frontalface_default.xml')
    def add_dataset(self, nama, img):
        # try:
        path_dataset = f"app/dataset/{nama}/"
        nama_file = str(len(os.listdir("app/dataset/uki/"))) if len(os.listdir("app/dataset/uki/")) <= 10 else 10

        # img = cv.imread(img)
        img = cv.imdecode(img, cv.IMREAD_COLOR)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.imwrite(str(os.path.join(path_dataset, nama_file)) + ".jpg", gray[y:y+h, x:x+w])
        print(str(os.path.join(path_dataset, nama_file)) + ".jpg")
        # img.save(os.path.join(path_dataset, f"{nama}-{nama_file}.jpg"))
        return True
        # except:
        #     return False