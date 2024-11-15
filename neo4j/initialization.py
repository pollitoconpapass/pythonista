import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

neo4j_url = os.getenv("NEO4J_URL")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(neo4j_url, auth=(neo4j_user, neo4j_password))