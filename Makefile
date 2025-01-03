# Variables
IMAGE_NAME = python_image
CONTAINER_NAME = python_container

# Default target
all: build run

# Build the Docker image
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .
	@if [ $$? -ne 0 ]; then \
		echo "Docker build failed"; \
		exit 1; \
	fi
	@echo "Docker build successful"

# Run the Docker container and enter it interactively
run:
	@echo "Starting Docker container in detached mode..."
	@container_id=$$(docker run -d -v "$$(pwd):/app" --name $(CONTAINER_NAME) $(IMAGE_NAME)); \
	if [ $$? -ne 0 ]; then \
		echo "Docker container failed to start"; \
		exit 1; \
	fi
	@echo "Docker container started successfully: $$container_id"

	@echo "Entering the Docker container interactively..."
	docker exec -it $$container_id /bin/sh
	@if [ $$? -ne 0 ]; then \
		echo "Failed to enter Docker container"; \
		docker stop $$container_id; \
		exit 1; \
	fi
	@echo "Entered Docker container successfully"

	@echo "Stopping the Docker container..."
	docker stop $$container_id

# Stop and remove all containers
clean:
	@echo "Stopping and removing containers..."
	@if [ "$(shell docker ps -a -q -f name=$(CONTAINER_NAME))" ]; then \
		docker stop $(shell docker ps -a -q -f name=$(CONTAINER_NAME)); \
		docker rm $(shell docker ps -a -q -f name=$(CONTAINER_NAME)); \
	fi

# Stop and remove all containers and remove all images
fclean: clean
	@echo "Removing Docker images..."
	@if [ "$(shell docker images -q $(IMAGE_NAME))" ]; then \
		docker rmi -f $(shell docker images -q $(IMAGE_NAME)); \
	fi

# Phony targets to avoid conflicts with files of the same name
.PHONY: all build run clean fclean