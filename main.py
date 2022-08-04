import json
import time
import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware

from finder import check_page_exists
from scraper import Scraper
from utils import scroll_to_bottom



app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/launch")
async def get_scraped_data(fastapi_req: Request):
    body = await fastapi_req.body()
    my_json = body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    print(data["page_name"])


    result = check_page_exists(data["page_name"])
    if not result:
        print("Page doesn't exist !")
        return False

    else:
        scrap = Scraper(data["page_name"], 200)
        scrap.init_driver()
        scroll_to_bottom(scrap.driver, 8)
        # time.sleep(200)
        scraped_data = scrap.scrape_data()
        print(scraped_data)

        # Serializing json
        json_object = json.dumps(scraped_data, indent=4)
        print(json_object)

        return scraped_data

if __name__ == "__main__":
    uvicorn.run(app='main:app')