# Main file for running the Dialectic French translation API

from fastapi import FastAPI
import uvicorn
from dialectic_config import config

app = FastAPI(
    title="Dialectic French Translation API",
    description="API for translating text to French using LLM models.",
)

if __name__ == "__main__":
    uvicorn.run(app, host=config['host'], port=config['port'])