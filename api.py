from fastapi import FastAPI
from notebook import Notebook

app = FastAPI()
notebook = Notebook()

@app.get("/notes")
def get_notes():
    return notebook.get_notes()

@app.post("/notes")
def add_note(title, content):
    notebook.add_note(title, content)
    return {"message": f"{title} added successfully!"}

@app.post("/get_note/{title}")
async def get_note(title):
    note = notebook.get_note(title)
    if note is None:
        return {"error": "Note does not exist!"}
    return {title: note}
