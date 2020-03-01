FROM node:8

WORKDIR /code/

COPY package.json package-lock.json /code/
RUN npm install

# add rest of the client code
COPY . /code/
