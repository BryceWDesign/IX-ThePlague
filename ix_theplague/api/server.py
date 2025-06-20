"""
IX-ThePlague REST API Server

Provides HTTP endpoints to interact with the infectious disease query processor,
allowing real-time querying within the IX-Gibson AI ecosystem.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXThePlagueQueryProcessor

app = FastAPI()
query_processor = IXThePlagueQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        answer = query_processor.process_query(request.query)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8021)
