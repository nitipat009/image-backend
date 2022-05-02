from fastapi import FastAPI

import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# routes
from routes.r_model1 import model1
from routes.r_model2 import model2

origins = ["*"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(model1)
app.include_router(model2)


if __name__ == "__main__":
    uvicorn.run("app:app", host='localhost', port=5000 ,reload=True )