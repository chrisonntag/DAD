FROM node:16-alpine as builder

WORKDIR /app/frontend

ENV PATH /app/frontend/node_modules/.bin:$PATH

COPY ./package.json /app/frontend/package.json
RUN npm install

COPY . /app/frontend

RUN npm run build
