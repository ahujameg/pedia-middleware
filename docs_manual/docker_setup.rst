.. _docker_setup:

======================
Docker Setup
======================

PEDIA-middleware application can be started in the docker container using the following steps.

.. note::

    Make sure Docker is installed, you can use the steps mentioned here to install Docker - https://docs.docker.com/engine/install/

1. Build the docker image

    .. code-block:: console

        $sudo docker build -t middleware-app .

2. Run the image in a docker container

    .. code-block:: console

        $sudo docker run -p 7000:7000 middleware-app

-------------------------------------------
Starting other services with Docker compose
-------------------------------------------


GestaltMatcher service
======================

To run the GestaltMatcher service, get the code and follow the steps mentioned here:
https://github.com/igsb/GestaltMatcher-Arc/tree/service#gestaltmatcher-rest-api

Build the docker image
    .. code-block:: console

        $sudo docker build -t gm-api .


PEDIA service
======================
To run the PEDIA service, get the code and follow the steps mentioned here:
https://github.com/PEDIA-Charite/classifier#pedia-rest-api

Build the docker image
    .. code-block:: console

        $sudo docker build -t pedia-classifier-api .


Run Docker-compose
======================

Once the images of the services are ready, run the following command to start all of them in docker container.
    .. code-block:: console

        $sudo docker-compose up
