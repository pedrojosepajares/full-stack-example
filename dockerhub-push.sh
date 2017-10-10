#! /bin/bash
# Cómo llamar al script: dockerhub-push.sh nombre-usuario id-image nombre-en-push
docker login --username=$1
docker tag $2 $1/$3
docker push $1/$3

