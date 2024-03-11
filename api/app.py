from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.config import initiate_database
from routes.author import router as AuthorRouter
from routes.book import router as BookRouter

app = FastAPI(docs_url="/", redoc_url=None, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(BookRouter, tags=["Books"], prefix="/book")
app.include_router(
    AuthorRouter,
    tags=["Author"],
    prefix="/api/authors",
)
