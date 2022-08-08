<h1> Public Facebook Page scraper service </h1>

<p> Scrape Facebook public pages using FastAPI. Scraped data will be stored in a database (MongoDB). </p>

<hr>

<h2> Start the application </h2>

<p> To start, in the terminal, you need to clone the project using the following command: </p>

```
$ git clone https://github.com/nada191/FacebookPage_Scraper
``` 

<p> Then, create the 3 images and start the 3 containers ( one for the FastAPI application, one for the MongoDB database and one for the frontend "Reactjs" ) using this command: </p>

```
$ docker-compose up -d
```
<p> To test the scraper, open the following link in your browser and simply enter the name of the page and launch the scraper: </p>

* http://localhost:3000/

<p> To see the scraped data, open: </p>

* http://0.0.0.0:8000
