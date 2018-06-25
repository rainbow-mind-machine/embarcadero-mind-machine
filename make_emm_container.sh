#!/bin/bash
#
# Once you build this emm container,
# you can build other images from it
# by putting the following in your Dockerfile:
# 
#    FROM emm
#    ...
#
# If you haven't built this container,
# you'll get an error about docker 
# not being able to find a container
# named emm.
# 
# Dockerhub container image is built directly
# from the Dockerfile in this repo.

docker build --no-cache -t emm .
