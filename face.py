#referencias
#https://omes-va.com/face-recognition-python/

from tkinter import Image
import cv2
import face_recognition


#--comparacion de imagen--

# se obtiene la imagen
image = cv2.imread("./images/rostro.jpg")

# se detecta el rostro en la imagen
face_loc = face_recognition.face_locations(image)[0]

# Guarda el mapa del rostro en la imagen
face_image_encodings = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]
#print("face_image_encodings: ", face_image_encodings)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame, 1) # efecto espejo

    # detecta el rostro en el frame
    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        for face_location in face_locations:

            #Guarda el mapa del rostro detectado en el frame
            face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_loc])[0]

            #comparacion con el rostro conocido y el desconocido
            result = face_recognition.compare_faces([face_image_encodings], face_frame_encodings)
            print(result)

            if result[0] == True:
                text = "conocido"
                color = (125, 220, 0)
            else:
                text = "Desconocido"
                color = (50, 50, 255)
            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
            cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows