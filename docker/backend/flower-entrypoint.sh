#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

# run flower monitoring :)
celery -A backend flower