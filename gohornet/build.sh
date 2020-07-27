#!/usr/bin/bash

IMAGE="gohornet"
CURRENT_VERSION=$(podman images localhost/gohornet --format "{{.Tag}}" | grep -v "latest" | sort -nr | head -1)
NEXT_VERSION=$(echo "$CURRENT_VERSION 0.1" | awk '{printf "%1.1f", $1 + $2}')

echo "Current Version: $CURRENT_VERSION"

if [ "$1" == "build" ]; then
	echo "Next Version: $NEXT_VERSION"
	podman build -f gohornet.in -t gohornet:$NEXT_VERSION
	if [ $? -eq 0 ]; then
		echo "Build erfolgreich!"
	else
		echo "Build fehlgeschlagen!"
	fi
fi

if [ "$1" == "send" ]; then
	podman save localhost/$IMAGE:$CURRENT_VERSION | gzip | ssh user1@reader.ms86.de 'gunzip | podman load'
	if [ $? -eq 0 ]; then
		echo "Uebertragung erfolgreich!"
	else
		echo "Uebertragung fehlerhaft!"
	fi
fi
