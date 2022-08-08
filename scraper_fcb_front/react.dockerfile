FROM node
WORKDIR /app
COPY /scraper_fcb_front/package.json .
RUN npm i
COPY . /app
EXPOSE 3000
CMD ["npm", "start"]