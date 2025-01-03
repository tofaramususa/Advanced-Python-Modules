#!/bin/sh

# Build the Docker image
docker build -t python_image .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Docker build failed"
    exit 1
fi
echo "Docker build successful"

# Start the Docker container in detached mode with volume binding
container_id=$(docker run -d -v "$(pwd):/app" python_image)

# Check if the container started successfully
if [ $? -ne 0 ]; then
    echo "Docker container failed to start"
    exit 1
fi
echo "Docker container started successfully: $container_id"

# Enter the running container interactively
docker exec -it "$container_id" /bin/sh

# Check if entering the container was successful
if [ $? -ne 0 ]; then
    echo "Failed to enter Docker container"
    # Stop the container if entering fails
    docker stop "$container_id"
    exit 1
fi
echo "Entered Docker container successfully"

# Optional: Cleanup if needed
# Uncomment the following line to stop the container after exiting the shell
docker stop "$container_id"
