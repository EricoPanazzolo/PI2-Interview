FROM python:3.11-slim

WORKDIR /app

# Copy the project files
COPY . /app/

# Expose the server ports
EXPOSE 8081
EXPOSE 8082

# Run default server (Buganizer)
CMD ["python", "-u", "-m", "apps.buganizer.main"]
