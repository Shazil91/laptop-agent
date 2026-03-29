from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import uuid
import os

# load env FIRST
load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION = "laptops"


def init_db():
    if not client.collection_exists(COLLECTION):
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )


def embed(text: str):
    return model.encode(text).tolist()


def upsert_laptops(laptops):
    points = []

    for l in laptops:
        text = f"{l['name']} {l['price']} {l['ram']} {l['gpu']} {l['usage']}"

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embed(text),
                payload=l
            )
        )

    client.upsert(collection_name=COLLECTION, points=points)

def search_laptops(query: str, limit=3):
    results = client.query_points(
        collection_name=COLLECTION,
        query=embed(query),
        limit=limit
    ).points

    return [r.payload for r in results]