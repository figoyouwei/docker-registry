"""
docker-registry
"""

def tag_and_push_image(image_name: str, registry_url: str = "localhost:5000") -> bool:
    """
    Tags a Docker image and pushes it to the specified registry
    
    Args:
        image_name: Name of the image to tag and push (e.g. 'hello-world')
        registry_url: URL of the registry (defaults to localhost:5000)
        
    Returns:
        bool: True if successful, False otherwise
    """
    import subprocess
    
    try:
        # Tag the image
        tag_cmd = f"docker tag {image_name} {registry_url}/{image_name}"
        subprocess.run(tag_cmd, shell=True, check=True)
        
        # Push the image
        push_cmd = f"docker push {registry_url}/{image_name}"
        subprocess.run(push_cmd, shell=True, check=True)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error tagging/pushing image: {e}")
        return False


if __name__ == "__main__":
    # Get image name from user
    image_name = input("Enter the Docker image name (e.g. hello-world): ")
    print(f"Preparing image: {image_name}")
    
    # Tag and push the image
    if tag_and_push_image(image_name):
        print(f"Successfully tagged and pushed {image_name} to localhost:5000")
    else:
        print("Failed to tag and push image")
