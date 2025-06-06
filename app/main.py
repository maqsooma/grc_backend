from fastapi import FastAPI, APIRouter
from services.neo4j_client import get_neo4j_driver
app = FastAPI()
router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/test-neo4j")
def test_neo4j():
    driver = get_neo4j_driver()
    with driver.session() as session:
        result = session.run("RETURN 'Neo4j is connected!' AS message")
        msg = result.single()["message"]
        return {"neo4j_status": msg}



app.include_router(router)