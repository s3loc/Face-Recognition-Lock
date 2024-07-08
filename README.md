# Face-Recognition-Lock


Project Name: Face Recognition Lock

Description:
Face Recognition Lock is a Python script that uses computer vision to recognize and authenticate users based on their face. It captures webcam video, detects hand signals to initiate face capture, saves and compares the detected face with a known face, and locks/unlocks the screen based on face recognition results.

Usage Instructions:

    Requirements:
        Python must be installed on your system.
        Install required libraries: cv2, numpy.
        Ensure your computer has a working webcam.

    Implementation:
        Copy the provided Python code into a file (e.g., face_recognition_lock.py).
        Install necessary libraries using pip:

        bash

    pip install opencv-python numpy

Execution:

    Run the script in a terminal or command prompt:

    bash

        python face_recognition_lock.py

        The webcam feed will start, and it will wait for a hand gesture to initiate face capture.

    Face Capture and Authentication:
        Hand Gesture Detection:
            Move your hand to trigger the script to capture your face.
        Face Detection and Comparison:
            Once a hand gesture is detected, the script captures your face and compares it with a previously saved face.
            If the face matches, it recognizes and displays a message indicating the recognized face.
            If the face does not match, it saves the new face and updates the known face.

    Screen Locking:
        The script continuously monitors the webcam feed for the recognized face.
        If the recognized face is detected continuously for a specified timeout period (default 5 seconds), it unlocks the screen.
        If the recognized face is not detected within the timeout period, it locks the screen for security.

    Exiting the Program:
        Press 'q' on your keyboard to exit the program and close the webcam feed.

Legal Disclaimer:
This script is for educational and personal use only. It accesses webcam data and utilizes face recognition techniques for authentication. The developer is not responsible for any misuse or potential issues resulting from the use of this script. Use at your own risk.

#-----------------------------------------------------------
Proje Adı: Yüz Tanıma Kilit

Açıklama:
Yüz Tanıma Kilit, kullanıcıların yüzleri üzerinden tanınmasını sağlayan ve bilgisayar görüntüleme tekniklerini kullanan bir Python scriptidir. Web kamerası videoyu yakalar, el sinyallerini algılayarak yüz yakalama işlemini başlatır, yakalanan yüzü kaydeder ve bilinen bir yüzle karşılaştırır. Yüz tanıma sonuçlarına göre ekranı kilitleyip açar.

Kullanım Talimatları:

    Gereksinimler:
        Bilgisayarınızda Python yüklü olmalıdır.
        Gerekli kütüphaneleri kurun: cv2, numpy.
        Bilgisayarınızda çalışan bir web kamerası olmalıdır.

    Uygulama:
        Sağlanan Python kodunu bir dosyaya kopyalayın (örneğin, face_recognition_lock.py).
        Gerekli kütüphaneleri pip kullanarak yükleyin:

        bash

    pip install opencv-python numpy

Çalıştırma:

    Terminal veya komut istemcisinde script'i çalıştırın:

    bash

        python face_recognition_lock.py

        Web kamerası beslemesi başlayacak ve el işareti bekleyecektir.

    Yüz Yakalama ve Doğrulama:
        El İşareti Algılama:
            El hareketinizi kullanarak script'i yüz yakalamaya başlatın.
        Yüz Algılama ve Karşılaştırma:
            El işareti algılandıktan sonra script yüzünüzü yakalar ve daha önce kaydedilmiş bir yüzle karşılaştırır.
            Eğer yüz eşleşirse, tanınan yüzü gösteren bir mesajı görüntüler.
            Eğer yüz eşleşmezse, yeni yüzü kaydeder ve bilinen yüzü günceller.

    Ekran Kilitleme:
        Script, web kamerası beslemesini sürekli olarak tanınan yüz için izler.
        Belirtilen zaman aşımı süresi boyunca (varsayılan 5 saniye) sürekli olarak tanınan yüz algılandığında ekranı kilidini açar.
        Tanınan yüz belirtilen zaman aşımı süresi içinde algılanmazsa, güvenlik için ekranı kilitler.

    Programdan Çıkış:
        Programı sonlandırmak ve web kamerası beslemesini kapatmak için klavyenizde 'q' tuşuna basın.

Yasal Sorumluluk Reddi:
Bu script eğitim ve kişisel kullanım içindir. Web kamerası verisine erişir ve yüz tanıma tekniklerini kullanarak kimlik doğrulama yapar. Geliştirici, bu script'in kullanımından kaynaklanabilecek herhangi bir yanlış kullanım veya olası sorunlardan sorumlu değildir. Kullanımı kendi sorumluluğunuzdadır.

