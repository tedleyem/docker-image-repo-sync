# Docker Image Repo Sync 
# This will check the latst docker image tags in dockerhub, then pull and 
# sync them to Harbor
import requests
import subprocess

# Docker Registry Credentials
DOCKER_HUB_URL = "https://hub.docker.com/v2/repositories/library"
DOCKER_REGISTRY = "docker.io"
HARBOR_URL = "http://bigharborregistry.com/api/v2.0/projects"
HARBOR_REGISTRY = "bigharborregistry.com"
HARBOR_USERNAME = "automation"
HARBOR_PASSWORD = "RoBoTaCcOuNt16DiGiTpAsSwOrd"
PROJECT_NAME = "library"

# Disable SSL verification (use at your own risk)
VERIFY_SSL = False
IMAGE_NAMES = [
    "python",
    "nginx",
    "ubuntu",
    "redis"
]

def run_command(cmd):
    """Run a shell command and print output."""
    print(f"Running: {cmd}")
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"❌ Command failed: {cmd}\n")
        print(f"❌ Error: {process.stderr}\n")
        exit()
    else:
        print(f"✅ Success: {cmd}")

def get_docker_image_tags(IMAGE_NAMES):
    """
    Grab the last 5 tags for requested Docker images from Docker Hub
    """
    url = f"{DOCKER_HUB_URL}/{IMAGE_NAMES}/tags/"

    response = requests.get(url, verify=VERIFY_SSL)

    if response.status_code == 200:
        tags_data = response.json()
        tags = [tag['name'] for tag in tags_data['results']]
    
        # Get the last 5 tags
        last_5_tags = tags[:5]
        return last_5_tags
    else:
        print(f"Failed to retrieve tags for {IMAGE_NAMES}. Status code: {response.status_code}")
        return []
 
def check_docker_image_exists(IMAGE_NAMES):
    #Checks if a Docker image with the specified tag exists locally.
    #Returns True if the image exists locally, False otherwise.
    
    try:
        subprocess.run(
            ["docker", "image", "inspect", "{IMAGE_NAMES}:{tags}"],
            check=True,
            capture_output=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_pull_image_locally(IMAGE_NAMES, tag):
    image_tag = f"{IMAGE_NAMES}:{tag}"

    if check_docker_image_exists(IMAGE_NAMES):
        print(f"Docker image '{image_tag}' exists locally.")
    else:
        print(f"Docker image '{image_tag}' does not exist locally.")

        try:
            # Try to pull the image from Docker Hub if not found locally
            print(f"Pulling image {image_tag} locally...")
            # Pull the new image
            run_command(f"docker pull {DOCKER_REGISTRY}/{image_tag}")

            print(f"Successfully pulled image {image_tag}.")
        except Exception as e:
            print(f"Failed to pull image {image_tag}: {e}")


def check_tag_exists_in_harbor(tag, HARBOR_URL, PROJECT_NAME, repository_name):
    harbor_api_url = f"{HARBOR_URL}/{PROJECT_NAME}/repositories/{repository_name}/tags/{tag}"
    response = requests.get(harbor_api_url, verify=VERIFY_SSL)
    
    if response.status_code == 200:
        return True  # Tag exists
    elif response.status_code == 404:
        return False  # Tag does not exist
    else:
        print(f"Error checking tag {tag}: {response.status_code}")
        return False

def push_image_to_harbor(IMAGE_NAMES, tag, HARBOR_URL, PROJECT_NAME):
    image_tag = f"{IMAGE_NAMES}:{tag}"
    harbor_image = f"{HARBOR_URL}/{PROJECT_NAME}/{IMAGE_NAMES}:{tag}"

    try:
        # Tag the image with the Harbor registry destination
        print(f"\n Tagging Image {image_tag} \n")
        print(f"\n docker tag {IMAGE_NAMES} {HARBOR_REGISTRY}/{PROJECT_NAME}/{IMAGE_NAMES}:{tag} \n")
        run_command(f"docker tag {IMAGE_NAMES} {HARBOR_REGISTRY}/{PROJECT_NAME}/{IMAGE_NAMES}:{tag}")
        
        # Push the image to Harbor
        print(f"\n Pushing image {image_tag} to Harbor: {harbor_image}")
        run_command(f"docker push {HARBOR_REGISTRY}/{PROJECT_NAME}/{IMAGE_NAMES}:{tag}")

        #print(f"Successfully pushed image {harbor_image}.")
    except Exception as e:
        print(f"Failed to push image {image_tag} to Harbor: {e}")

def check_and_pull_if_not_found_loop(IMAGE_NAMES, HARBOR_URL, PROJECT_NAME):
    # Loop through the list of image names
    for IMAGE_NAMES in IMAGE_NAMES:
        print(f"\nChecking tags for image: {IMAGE_NAMES}")
        
        # Retrieve the last 5 tags from Docker Hub for the current image
        tags = get_docker_image_tags(IMAGE_NAMES)
        print(f"\n DockerHub tags located for image: {IMAGE_NAMES}")
        print(f"\n {tags}")
        
        if not tags:
            print(f"No Dockerhub tags retrieved for {IMAGE_NAMES}. \n")
            continue

        # Check if each of the last 5 tags exists in the Harbor registry
        for tag in tags:
            exists = check_tag_exists_in_harbor(tag, HARBOR_URL, PROJECT_NAME, IMAGE_NAMES)
            print(f"  Tag '{tag}' exists in Harbor: {exists}")
            
        # If the tag does not exist in Harbor, try pulling it locally and pushing to Harbor
            if exists == False:
                # Check if the image with the specific tag exists locally
                print(f"Pulling tag '{tag}' for {IMAGE_NAMES} from DockerHub \n")
                # Image not found locally, pull it from Docker Hub
                check_and_pull_image_locally(IMAGE_NAMES, tag)
                # After pulling, push it to Harbor using robot credentials
                push_image_to_harbor(IMAGE_NAMES, tag, HARBOR_URL, PROJECT_NAME)
            else:
                print(f"Failed to pull tag '{tag}' {IMAGE_NAMES} from DockerHub \n")

def main():
    # Authenticate Docker client with Harbor robot credentials
    print(f"\n Attempting Login to Harbor Dev")
    run_command(f"docker login -u '{HARBOR_USERNAME}' -p '{HARBOR_PASSWORD}' {HARBOR_REGISTRY} \n")
    # Put it all together
    check_and_pull_if_not_found_loop(IMAGE_NAMES, HARBOR_URL, PROJECT_NAME)

if __name__ == '__main__':
    main()