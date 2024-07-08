import cv2
import os
import ctypes
import numpy as np
import time

# El ve yüz için cascade sınıflandırıcıları
palm_cascade = cv2.CascadeClassifier('C:\\Users\\vural\\PycharmProjects\\faceshow2\\.idea\\palm.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ekran kilidini açmak için Windows API'sini kullan
def lock_screen():
    ctypes.windll.user32.LockWorkStation()

# Yeni bir yüz kaydet
def save_face(face_roi):
    face_path = os.path.join('faces', 'user_face.jpg')
    cv2.imwrite(face_path, face_roi)
    print('Yeni yüz kaydedildi!')
    return face_path

# Kaydedilen yüzü yükle ve tanı
def load_known_face():
    face_path = os.path.join('faces', 'user_face.jpg')
    if os.path.exists(face_path):
        known_face = cv2.imread(face_path, cv2.IMREAD_GRAYSCALE)
        return known_face
    return None

# Yüzlerin karşılaştırılması
def is_same_face(face1, face2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(face1, None)
    kp2, des2 = orb.detectAndCompute(face2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    if len(matches) > 10:  # Eşik değeri, gerektiğinde ayarlanabilir
        return True
    return False

# Webcam'den video akışı yakala
cap = cv2.VideoCapture(0)

while True:
    # Kullanıcının el işareti yapmasını bekleyin
    hand_detected = False
    while not hand_detected:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        palms = palm_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (px, py, pw, ph) in palms:
            if pw > 100 and ph > 100:  # Algılanan avucun yeterince büyük olduğundan emin ol
                hand_detected = True
                print("El işareti algılandı.")
                break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # El işareti algılandıktan sonra yüz kaydetme döngüsü
    like_detected = False
    known_face = load_known_face()
    while not like_detected:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            if known_face is not None:
                if is_same_face(face_roi, known_face):
                    cv2.putText(frame, 'Kaydedilen Yüz!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                else:
                    cv2.putText(frame, 'Farkli Yüz!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            else:
                save_face(face_roi)
                known_face = face_roi
                like_detected = True
                break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Zaman aşımı ayarları
    timeout_duration = 5  # 5 saniye
    last_seen_time = time.time()

    # Yüz tanıma döngüsü
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        face_recognized = False

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            if known_face is not None and is_same_face(face_roi, known_face):
                face_recognized = True
                last_seen_time = time.time()
                cv2.putText(frame, 'Kaydedilen Yüz!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                break

        if face_recognized:
            print("Kaydedilen yüz algılandı. Ekran kilidi açıldı.")
        else:
            # Kaydedilen yüz son görülme zamanını kontrol et
            if time.time() - last_seen_time > timeout_duration:
                print("Kaydedilen yüz algılanmadı. Ekran kilidi kapatılıyor.")
                lock_screen()
                break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
