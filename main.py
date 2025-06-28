# main.py

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from services.graphql import schema
from services.database import get_session

app = FastAPI()

# Provide context (session) to GraphQL
async def get_context():
    session_gen = get_session()
    session = await anext(session_gen)
    return {"session": session}

graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/graphql")
