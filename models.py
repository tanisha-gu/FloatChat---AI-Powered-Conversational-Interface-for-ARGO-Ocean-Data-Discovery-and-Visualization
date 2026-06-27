from pydantic import BaseModel
#here models
class QueryRequest(BaseModel):
    query: str
