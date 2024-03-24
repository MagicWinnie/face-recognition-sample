# Face Recognition Sample

A sample face recognition app using python, opencv, and dlib. Hosted on Docker Hub.

## Run Docker
1. `docker pull magicwinnie/face-recognition-sample:latest`
2. `xhost +local:docker`
3. `docker run --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY face-recognition-sample`
