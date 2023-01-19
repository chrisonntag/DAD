FROM node:16-alpine

WORKDIR /app/frontend/

COPY package.json /app/frontend/package.json
RUN npm install

COPY . /app/frontend/

CMD ["npm", "start"]
