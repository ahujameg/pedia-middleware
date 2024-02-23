# PEDIA-middleware
This is a middleware application for handling integration of variant analysis tools like VarFish with PEDIA (Prioritization of Exome data by image analysis). It can be independently embeded 
as an iFrame in the Variant Analysis tool. There is a a view displayed that takes the patient image as input and submits it to the GestaltMatcher service. It then retrieves the gene list with the 
gestalt scores from the GestaltMatcher service and posts it back to the parent window (i.e. the tool embedding this application) 

### Pre-requisites:
This application works with python version 3.10, make sure it is installed or use the following command to install it:
```
sudo apt update
sudo apt install python3
```

Install pip3:
``` 
sudo apt install pip3 
```

Then, install Pipenv. Pipenv is a tool that provides all necessary means to create a virtual environment for a 
Python project. It automatically manages project packages through the Pipfile file as packages are installed or uninstalled:
```
pip3 install pipenv
```

### Install requirements
To run the django application, first set the environment using the pipfile:
```
pipenv shell
```
Install the requirements:
```
pipenv sync
```
Alternatively, if you are unfamiliar with pipenv you can use the requirements.txt file to install required packages.
```
pip3 install -r requirements.txt
```

### Application Startup
Start the application server on a different port than Varfish, for example on port 7000:
```
python3 manage.py runserver 7000
```

## Docker setup:
PEDIA-middleware application can be started in the docker container using the following steps.

Make sure Docker is installed, you can use the steps mentioned here to install Docker - https://docs.docker.com/engine/install/ 
1. Build the docker image
    ```
    sudo docker build -t middleware-app .
    ```
2. Run the image in a docker container
    ```
    sudo docker run -p 7000:7000 middleware-app
    ```

### Starting other services with Docker compose

#### GestaltMatcher service

To run the GestaltMatcher service, get the code and follow the steps mentioned here:
https://github.com/igsb/GestaltMatcher-Arc/tree/service#gestaltmatcher-rest-api

Build the docker image 
    ```
    sudo docker build -t gm-api .
    ```
#### PEDIA service
To run the PEDIA service, get the code and follow the steps mentioned here:
https://github.com/PEDIA-Charite/classifier#pedia-rest-api

Build the docker image 
    ```
    sudo docker build -t pedia-classifier-api .
    ```

### Send image through PEDIA-Middleware
1. Launch the PEDIA Middleware server in browser at http://127.0.0.1:7000
2. Click on 'Choose File' button and select the image to send.
3. After choosing a file, the 'Submit to GestlatMatcher' button is enabled, click to submit.
4. The image is sent to GestaltMatcher service API at http://127.0.0.1:5000/predict and a successful message or error 
message is displayed depending on the response received from GestaltMatcher service.

