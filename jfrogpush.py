import requests
import subprocess



# Define the URL you want to check
url_to_check = "http://184.169.215.169:8082/"  # Replace with the URL you want to test

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url_to_check)

    # Check the HTTP status code
    if response.status_code == 200:
        print(f"The URL {url_to_check} is serving the request with status code 200 (OK).")
#        curl -X PUT -u admin -T target/kubernetes-configgap-reload-0.0.1-SNAPSHOT.jar http://184.169.215.169:8082/artifactory/example-repo-local/
    else:
        print(f"The URL {url_to_check} returned status code {response.status_code}.")
    # Execute the curl command
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
