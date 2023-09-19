# pull official base image
FROM node:alpine

WORKDIR /app

ADD ./frontend /app/frontend/
ADD ./docker /app/docker

ADD ./frontend/package.json /app/

RUN npm install

EXPOSE 3005

RUN chmod +x /app/docker/frontend/react-entrypoint.sh
