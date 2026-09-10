#here just a import file andi created class
from pydantic import BaseModel
#here models
class QueryRequest(BaseModel):
    query: str
