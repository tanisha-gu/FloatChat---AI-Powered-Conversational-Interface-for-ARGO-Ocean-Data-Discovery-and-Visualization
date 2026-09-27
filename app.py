#import all 
from fastapi import FastAPI
from models import QueryRequest
from db import query_sql
from rag import search

app = FastAPI()
#attachted 
@app.get("/")
def home():
    return {"message": "FloatChat Backend Running"}
#DB query
def nl_to_sql(query):
    if "salinity" in query.lower():
        return "SELECT * FROM argo_data LIMIT 100"
    elif "temperature" in query.lower():
        return "SELECT * FROM argo_data LIMIT 100"
    else:
        return "SELECT * FROM argo_data LIMIT 50"
#db chat query
@app.post("/chat")
def chat(req: QueryRequest):
    sql = nl_to_sql(req.query)
    data = query_sql(sql)
    context = search(req.query)
#what we whant here return
    return {
        "sql": sql,
        "rows": data.head(10).to_dict(),
        "context": context
    }
