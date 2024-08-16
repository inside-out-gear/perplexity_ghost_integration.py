# Deploying Perplexity AI to Ghost Post Script as a Docker Container

This guide explains how to deploy the Python script that sends prompts to Perplexity AI and posts the responses to a Ghost blog as a Docker container.

## Prerequisites

- Docker installed on your machine or build server
- Perplexity AI and Ghost API keys and URLs

## Step 1: Create a Dockerfile

Create a `Dockerfile` in the same directory as your Python script with the following contents:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "perplexity_to_ghost.py"]
```

## Step 2: Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t perplexity-to-ghost .
```

This will create a Docker image named `perplexity-to-ghost` using the instructions in the `Dockerfile`.

## Step 3: Run the Docker Container

To run the container, use the following command:

```bash
docker run \
  -e PERPLEXITY_API_KEY=$PERPLEXITY_API_KEY \
  -e GHOST_API_KEY=$GHOST_API_KEY \
  -e GHOST_API_POST_URL=$GHOST_API_POST_URL \
  perplexity-to-ghost
```

This command:
- Runs the `perplexity-to-ghost` image as a container
- Passes the required environment variables (`PERPLEXITY_API_KEY`, `GHOST_API_KEY`, `GHOST_API_POST_URL`) to the container using the `-e` flag
- Assumes you have set these environment variables in your shell or a `.env` file

## Step 4: Deploy to a Container Platform

Once you have the Docker image built, you can deploy it to a container platform like:
- Docker Hub
- Amazon Elastic Container Registry (ECR)
- Google Container Registry (GCR)
- Azure Container Registry (ACR)

The specific steps will depend on the platform you choose, but the general process involves:
1. Pushing the Docker image to the registry
2. Deploying the image to a container service (e.g., AWS ECS, Google Cloud Run, Azure Container Instances)

## Conclusion

By containerizing your Python script using Docker, you can ensure consistent and reliable deployments across different environments. The Docker image encapsulates the script along with its dependencies, making it easy to distribute and run.

Remember to securely store your API keys and URLs as environment variables, either in a `.env` file or in the container platform's configuration.
