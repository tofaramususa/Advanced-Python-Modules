# Variables
IMAGE_NAME = python_modules
CONTAINER_NAME = python_modules_container

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
	@CONTAINER_ID=$$(docker run -d -v "$$(pwd):/app" --name $(CONTAINER_NAME) $(IMAGE_NAME)); \
	if [ -z "$$CONTAINER_ID" ]; then \
		echo "Docker container failed to start"; \
		exit 1; \
	fi; \
	echo "Docker container started successfully: $$CONTAINER_ID"; \
	echo "Entering the Docker container interactively..."; \
	if ! docker exec -it $$CONTAINER_ID /bin/sh; then \
		echo "Failed to enter Docker container"; \
		docker stop $$CONTAINER_ID; \
		exit 1; \
	fi; \
	echo "Entered Docker container successfully"; \
	echo "Stopping the Docker container..."; \
	docker stop $$CONTAINER_ID

shell: docker exec -it $$CONTAINER_ID /bin/sh
# Stop and remove all containers
clean:
	@echo "Stopping and removing containers..."
	@docker ps -a -q -f name=$(CONTAINER_NAME) | xargs -r docker stop
	@docker ps -a -q -f name=$(CONTAINER_NAME) | xargs -r docker rm

# Stop and remove all containers and remove all images
fclean: clean
	@echo "Removing Docker images..."
	@docker images -q $(IMAGE_NAME) | xargs -r docker rmi -f

re: fclean all

# Phony targets to avoid conflicts with files of the same name
.PHONY: all build run clean fclean re