from typing import Union

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .dependencies import get_db
from .models import WaitList
from .schema import WaitListSchema
from fastapi.middleware.cors import CORSMiddleware






app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/waitlist")
async def get_waitlist(db:Session=Depends(get_db)):
    waitlist = db.query(WaitList).all()
    return waitlist

@app.post("/add")
async def add_waitlist(payload: WaitListSchema, db: Session = Depends(get_db)):
    waitlist_entry = WaitList(**payload.model_dump()) 
    db.add(waitlist_entry)
    db.commit()
    db.refresh(waitlist_entry)
    return waitlist_entry