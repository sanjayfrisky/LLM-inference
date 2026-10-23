


from fastapi import UploadFile
from fastapi import APIRouter
router = APIRouter()

@router.post("/upload")
async def upload_file(file:UploadFile):
    load_text = await file.read()
    content = []

    for text in load_text.splitlines():
        content.append(text)
        
    return content



