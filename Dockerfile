FROM python:3.10-bullseye

RUN wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
RUN bzip2 -d shape_predictor_68_face_landmarks.dat.bz2

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y --no-install-recommends

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

ENTRYPOINT ["python3.10", "main.py"]