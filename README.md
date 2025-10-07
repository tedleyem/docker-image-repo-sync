# Docker Image Repo Sync

There are two Sync projects that help syncing docker images to [Dockerhub](https://hub.docker.com/search) or a [Harbor](https://goharbor.io/) Private repo.  

* **private_sync.py**: Sync Docker Images to a Private Harbor Registry with Python.
* **GH Actions - docker build and sync to dockerhub**: Sync Docker projects to DockerHub using GitHub Actions.

### Cloning and Syncing CI/CD

The DockerHub sync will run and sync automatically. Copy this repo and use the `update.sh` script to add a timestamp to the `UPDATE.MD` file. That will trigger the GitHub Action that will build the Docker projects in the apps/ dir and push them to DockerHub based on `secrets.DOCKERHUB_USERNAME` and `secrets.DOCKERHUB_TOKEN`.

### Prerequisites
1. **Docker** installed on your local machine.
2. A **Harbor** registry set up. If you don't have one, follow [Harbor's installation guide](https://goharbor.io/docs/).
3. **Python 3.x** installed on your machine.
4. The **Harbor API credentials** (username and password) to authenticate with your Harbor registry.
5. A **Linux** machine.

Note: A DockerHub account may be required for pulling private images but this script "currently" doesn't have that functionality.

### GitHub Environment Variables Configuration
To set up the repository for GitHub CI/CD automation, you will need to configure these environment variables as GitHub environment variables.

### Required Environment Variables

| Environment Variable       | Description                                         |
|----------------------------|-----------------------------------------------------|
| `DOCKER_HUB_URL`           | Docker Hub URL                                      |
| `DOCKER_REGISTRY`          | Docker Registry                                     |
| `HARBOR_URL`               | Harbor URL                                          |
| `HARBOR_REGISTRY`          | Harbor Registry                                     |
| `HARBOR_USERNAME`          | Harbor Username                                     |
| `HARBOR_PASSWORD`          | Harbor Password                                     |
| `PROJECT_NAME`             | Project name                                        |

### Setup

1. Clone the repository to your local machine:
   ```sh
   git clone <repository-url>
   ```

2. Navigate to the cloned repository directory:
   ```sh
   cd <repository-directory>
   ```

3. Add the environment variables to your GitHub repository's secrets:
   - Go to the repository on GitHub.
   - Click on the "Settings" tab.
   - In the left sidebar, click on "Secrets and variables".
   - Click on the "New repository secret" button.
   - Add each environment variable as a secret.

By setting these environment variables as GitHub Secrets, you will be able to use GitHub Actions for CI/CD automation with the required Docker and Harbor registries configured for this project.

Once these step are completed you can run the update.sh script to push updates to any of the docker projects under the apps/ dir. 


---

* Old Blog reference [here](https://ted.meralus.com/docker-image-repo-sync/).
* Dockerhub [link](https://hub.docker.com/u/tedleyem)