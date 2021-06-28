# syntax=docker/dockerfile:1
FROM node:12-alpine
RUN apk add --nocache python g++ make
WORKDIR /app
COPY ..
RUN yarn install --production
CMD ["node", "src/index.js"]
