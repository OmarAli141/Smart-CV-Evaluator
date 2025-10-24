# Docker Deployment Guide for Smart CV Evaluator

This guide explains how to deploy the Smart CV Evaluator application using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose (usually comes with Docker Desktop)
- Ollama running locally (for AI model inference)

## Quick Start

### 1. Build and Run with Docker Compose (Recommended)

```bash
# Build and start the application
docker-compose up --build

# Run in detached mode (background)
docker-compose up -d --build
```

The application will be available at: `http://localhost:8501`

### 2. Build and Run with Docker Commands

```bash
# Build the Docker image
docker build -t smart-cv-evaluator .

# Run the container
docker run -p 8501:8501 smart-cv-evaluator
```

## Configuration

### Environment Variables

You can customize the application using environment variables:

```bash
# Custom port
docker run -p 8080:8080 -e STREAMLIT_SERVER_PORT=8080 smart-cv-evaluator

# Custom address
docker run -p 8501:8501 -e STREAMLIT_SERVER_ADDRESS=0.0.0.0 smart-cv-evaluator
```

### Volume Mounts

For persistent storage of uploads and temporary files:

```bash
docker run -p 8501:8501 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/temp:/app/temp \
  smart-cv-evaluator
```

## Ollama Integration

### Option 1: Local Ollama (Recommended)
Keep Ollama running on your host machine. The Docker container will connect to `host.docker.internal:11434` (on Windows/Mac) or `localhost:11434` (on Linux).

### Option 2: Ollama in Docker
Uncomment the Ollama service in `docker-compose.yml` to run Ollama in a separate container:

```yaml
# Uncomment these lines in docker-compose.yml
ollama:
  image: ollama/ollama:latest
  container_name: ollama
  ports:
    - "11434:11434"
  volumes:
    - ollama_data:/root/.ollama
```

Then run:
```bash
docker-compose up --build
```

## Production Deployment

### Using Docker Compose

1. **Create a production override file:**
```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  smart-cv-evaluator:
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    restart: always
```

2. **Deploy with production settings:**
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Using Docker Swarm

```bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml smart-cv-evaluator
```

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Check what's using port 8501
   netstat -tulpn | grep 8501
   
   # Use a different port
   docker run -p 8502:8501 smart-cv-evaluator
   ```

2. **Ollama connection issues:**
   - Ensure Ollama is running: `ollama serve`
   - Check if the model is installed: `ollama list`
   - Test connection: `curl http://localhost:11434/api/tags`

3. **Permission issues:**
   ```bash
   # Fix volume permissions
   sudo chown -R $USER:$USER ./uploads ./temp
   ```

### Health Checks

The application includes health checks. Monitor with:

```bash
# Check container health
docker ps

# View logs
docker logs smart-cv-evaluator

# Check health endpoint
curl http://localhost:8501/_stcore/health
```

## Development

### Development Mode

For development with live code reloading:

```bash
# Mount source code as volume
docker run -p 8501:8501 \
  -v $(pwd):/app \
  -v $(pwd)/uploads:/app/uploads \
  smart-cv-evaluator
```

### Debugging

```bash
# Run with debug output
docker run -p 8501:8501 \
  -e STREAMLIT_LOGGER_LEVEL=debug \
  smart-cv-evaluator

# Interactive shell
docker run -it --rm smart-cv-evaluator /bin/bash
```

## Security Considerations

1. **Network Security:**
   - Use reverse proxy (nginx) for production
   - Enable HTTPS with SSL certificates
   - Restrict container network access

2. **File Security:**
   - Regularly clean temporary files
   - Implement file size limits
   - Scan uploaded files for malware

3. **Resource Limits:**
   ```yaml
   # Add to docker-compose.yml
   deploy:
     resources:
       limits:
         memory: 2G
         cpus: '1.0'
   ```

## Monitoring and Logs

```bash
# View real-time logs
docker-compose logs -f

# View specific service logs
docker-compose logs smart-cv-evaluator

# Monitor resource usage
docker stats smart-cv-evaluator
```

## Cleanup

```bash
# Stop and remove containers
docker-compose down

# Remove images
docker rmi smart-cv-evaluator

# Clean up volumes
docker-compose down -v

# Full cleanup (removes everything)
docker system prune -a
```

## Support

For issues related to:
- **Docker**: Check Docker documentation
- **Streamlit**: Visit Streamlit documentation
- **Ollama**: Check Ollama documentation
- **Application**: Check the main README.md
