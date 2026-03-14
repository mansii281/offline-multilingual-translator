import cv2
import mediapipe as mp
import math
from transformers import pipeline

print("Loading translation model...")

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="eng_Latn"
)

print("Model ready\n")

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.8
)

cap = cv2.VideoCapture(0)

word = ""
letter = ""

def dist(a,b):
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

def finger_state(hand):

    fingers = []

    # thumb
    fingers.append(1 if hand.landmark[4].x > hand.landmark[3].x else 0)

    # index
    fingers.append(1 if hand.landmark[8].y < hand.landmark[6].y else 0)

    # middle
    fingers.append(1 if hand.landmark[12].y < hand.landmark[10].y else 0)

    # ring
    fingers.append(1 if hand.landmark[16].y < hand.landmark[14].y else 0)

    # pinky
    fingers.append(1 if hand.landmark[20].y < hand.landmark[18].y else 0)

    return fingers

print("Gesture Mode Started")
print("SPACE → capture letter")
print("ENTER → finish word\n")

while True:

    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)
    letter = ""

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

            fingers = finger_state(hand)

            thumb = hand.landmark[4]
            index = hand.landmark[8]
            middle = hand.landmark[12]
            ring = hand.landmark[16]
            pinky = hand.landmark[20]

            # A
            if fingers == [1,0,0,0,0]:
                letter="A"

            # B
            elif fingers == [0,1,1,1,1]:
                letter="B"

            # C
            elif dist(thumb,index)>0.1 and fingers[1:]==[1,1,1,1]:
                letter="C"

            # D
            elif fingers == [0,1,0,0,0]:
                letter="D"

            # E
            elif fingers == [0,0,0,0,0] and dist(thumb,index)<0.08:
                letter="E"

            # F
            elif dist(thumb,index)<0.05 and fingers[2:]==[1,1,1]:
                letter="F"

            # G
            elif fingers == [1,1,0,0,0]:
                letter="G"

            # H
            elif fingers == [0,1,1,0,0]:
                letter="H"

            # I
            elif fingers == [0,0,0,0,1]:
                letter="I"

            # K
            elif fingers == [1,1,1,0,0]:
                letter="K"

            # L
            elif fingers == [1,1,0,0,0]:
                letter="L"

            # M
            elif fingers == [0,0,0,0,0] and dist(thumb,ring)<0.05:
                letter="M"

            # N
            elif fingers == [0,0,0,0,0] and dist(thumb,middle)<0.05:
                letter="N"

            # O
            elif dist(thumb,index)<0.04 and fingers[1:]==[0,0,0,0]:
                letter="O"

            # P
            elif fingers == [1,1,1,0,0] and index.y>middle.y:
                letter="P"

            # Q
            elif fingers == [1,1,0,0,0] and index.y>thumb.y:
                letter="Q"

            # R
            elif fingers == [0,1,1,0,0] and dist(index,middle)<0.03:
                letter="R"

            # S
            elif fingers == [0,0,0,0,0] and dist(thumb,pinky)>0.1:
                letter="S"

            # T
            elif fingers == [0,0,0,0,0] and dist(thumb,index)>0.1:
                letter="T"

            # U
            elif fingers == [0,1,1,0,0] and dist(index,middle)>0.05:
                letter="U"

            # V
            elif fingers == [0,1,1,0,0] and dist(index,middle)>0.08:
                letter="V"

            # W
            elif fingers == [0,1,1,1,0]:
                letter="W"

            # X
            elif fingers == [0,1,0,0,0] and dist(index,thumb)>0.08:
                letter="X"

            # Y
            elif fingers == [1,0,0,0,1]:
                letter="Y"

    cv2.putText(frame,"Detected: "+letter,(30,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.putText(frame,"Word: "+word,(30,80),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("ASL Translator",frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 13:
        break

    if key == 32:

        if letter!="":
            word+=letter
            print("Captured:",letter)

        while cv2.waitKey(1)&0xFF==32:
            pass

cap.release()
cv2.destroyAllWindows()

print("\nDetected word:",word)

languages = {
"1":("hin_Deva","Hindi"),
"2":("spa_Latn","Spanish"),
"3":("arb_Arab","Arabic"),
"4":("fra_Latn","French"),
"5":("deu_Latn","German"),
"6":("ita_Latn","Italian"),
"7":("zho_Hans","Chinese"),
"8":("jpn_Jpan","Japanese"),
"9":("kor_Hang","Korean")
}

print("\nSelect language:\n")

for k,v in languages.items():
    print(k,v[1])

choice=input("Enter number: ")

target=languages.get(choice)

translated=translator(
word,
tgt_lang=target[0],
num_beams=3,
early_stopping=True
)

print("\nTranslated ("+target[1]+"):")
print(translated[0]["translation_text"])