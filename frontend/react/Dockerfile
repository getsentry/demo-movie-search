FROM node

#
# Build:
# docker build -t ds_frontend:v0 .
#
# Run:
# docker run --rm -p 3000:3000 -it ds_frontend:v0
#

WORKDIR /app

COPY package.json yarn.lock ./
# Make sure react docker container can connect to django docker container
# see also docker-compose.yml
RUN sed -i -e 's/localhost/django/g' package.json

RUN yarn

COPY public/ ./public/
COPY src/ ./src/
COPY postcss.config.js .
COPY tailwind.config.js .

CMD ["yarn", "start"]
