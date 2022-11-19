from fastapi import FastAPI
from copykitt import generate_branding_snippet, generate_keywords

app = FastAPI()


@app.get("/generate_snippet")
async def generate_branding_snippet_api(prompt: str):
    snippet = generate_branding_snippet(prompt)
    return {"Snippet": snippet, "Keywords": []}

@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    keywords = generate_keywords(prompt)
    return {"Snippet": None, "Keywords": keywords}

@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"Snippet": snippet, "Keywords": keywords}
 
