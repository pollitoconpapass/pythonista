# For buildin the container image using the Dockerfile
docker build -t sampleapp: latest .

# For running the container
docker run -p 5000:5000 sampleapp:latest # -> host port: container port