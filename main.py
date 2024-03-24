import cv2
import dlib
from argparse import ArgumentParser
from imutils import face_utils, resize

parser = ArgumentParser()
parser.add_argument(
    "-p",
    "--predictor",
    type=str,
    default="shape_predictor_68_face_landmarks.dat",
    required=False,
    help="Path to the dlib shape predictor",
)
parser.add_argument(
    "-w", "--width", type=int, default=600, required=False, help="Output image width"
)
parser.add_argument(
    "-n", "--name", type=str, default="image", required=False, help="Output window name"
)
parser.add_argument(
    "-c", "--camera", type=int, default=0, required=False, help="Input device (camera) id"
)
args = parser.parse_args()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args.predictor)

vs = cv2.VideoCapture(args.camera)

while True:
    _, image = vs.read()
    image = resize(image, width=args.width)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1)
    for i, rect in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        x, y, w, h = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        for x, y in shape:
            cv2.circle(image, (x, y), 3, (0, 255, 0), -1)

    cv2.imshow(args.name, image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
vs.release()
