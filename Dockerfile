FROM python:3.12-alpine

# Keeps Python from buffering stdout and stderr for immediate logging
ENV PYTHONUNBUFFERED=1

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Add a non-root user for security
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install dependencies if requirements.txt exists, with robust error handling
RUN if [ -f requirements.txt ]; then \
		pip install --user --no-cache-dir -r requirements.txt; \
	else \
		echo "Warning: requirements.txt not found. Skipping dependency installation."; \
	fi

RUN alias norminette="python -m flake8"
# Copy application code into the container
COPY . .

# Ensure the appuser has the necessary permissions
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Set a default command to run a Python application (replace "app" with your entry module/script)
CMD ["sleep", "infinity"]
