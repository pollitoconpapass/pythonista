from fastapi import FastAPI, UploadFile, File


app = FastAPI()

@app.post("/url_name")
async def func_one(file: UploadFile = File(...)):
    return {"filename": file.filename}


# IN POSTMAN: 
'''
1. Go to Body
2. Choose Form-Data
3. In key select Text and type 'wav_file' (or whatever your file type is)
3. Change Text to File
4. In Value select your file
'''