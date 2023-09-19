#!/bin/sh

until cd /app/frontend
do
    echo "Waiting for react app volume..."
done

npm start