import requests, uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()
nodes = [("127.0.0.1", "8000")]

@app.get("/register")
async def register_node(host: str, port:str):
    nodes.append((host, port))

@app.post("/convert/{category}")
async def convert(category: str, file: UploadFile, target_filetype: str, output_filename: str=None, max_filesize: str=None):
    node = nodes[0]
    url = "http://"+node[0]+":"+node[1]+"/convert/"+category
    file = file.file
    
    print(url)
    r = requests.post(url, files={"file": file}, params={"target_filetype": "jpg"})
    return r.json()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)