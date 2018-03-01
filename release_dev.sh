#!/usr/bin/env bash

export ORG="bluelens"
export IMAGE="bl-ticker"
export TAG='dev'
export NAMESPACE="dev"

docker login

docker build -t $IMAGE:$TAG .
docker tag $IMAGE:$TAG $ORG/$IMAGE:$TAG
docker push $ORG/$IMAGE:$TAG
