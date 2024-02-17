from fastapi import FastAPI

from config.config import initiate_database
from routes.author import router as AuthorRouter
from routes.book import router as BookRouter

app = FastAPI(docs_url="/", redoc_url=None)


@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(BookRouter, tags=["Books"], prefix="/book")
app.include_router(
    AuthorRouter,
    tags=["Author"],
    prefix="/author",
)
