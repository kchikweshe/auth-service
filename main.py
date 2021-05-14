from fastapi import FastAPI
from models import Base
from database import engine
from routers import actors
from routers import users
from routers import authentication
from routers import genre
from routers import directors
from routers import movies


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(actors.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(genre.router)
app.include_router(directors.router)
app.include_router(movies.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}
# if __name__ == '__main__':
#     print_hi('PyCharm')
