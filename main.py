import io
from fastapi import FastAPI
from s3_config import s3_client
from openpyxl import load_workbook
from fastapi import UploadFile, File

app = FastAPI()

@app.get("/get-presigned-url")
def generate_url(filename: str):
    url = s3_client.generate_presigned_url(
        ClientMethod='put_object',
        Params={'Bucket': 'file-bucket', 'Key': filename},
        ExpiresIn=300
    )
    return {"url": url}


@app.post("/get-purl-with-row-count")
async def count_and_upload(file: UploadFile = File(...)):
    
    contents = await file.read()

    if file.filename.endswith(".csv"):
        text = contents.decode()
        lines = text.splitlines()
        header_skipped = lines[1:]
        row_count = sum(1 for line in header_skipped if line.strip())
        # return {"contents":contents, "text": text, "lines":lines, "header_skipped": header_skipped}
    
    elif file.filename.endswith(".xlsx"):

        excel_file = io.BytesIO(contents)
        wb = load_workbook(excel_file)
        ws = wb.active

        row_count = 0
        for row in ws:
            if not all([cell.value == None for cell in row]):
                row_count += 1
    else:
        return {"error": "Unsupported file type. Only CSV and XLSX are allowed."}

    url = generate_url(file.filename)

    return {"count": row_count, "filename": file.filename, **url}