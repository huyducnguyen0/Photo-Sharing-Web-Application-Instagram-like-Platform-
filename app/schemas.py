from pydantic import BaseModel # special object

class PostCreate(BaseModel):
    title : str
    content : str