# FastAPI + Tebi S3 File Upload & Row Counter

This is a **FastAPI** application that integrates with **Tebi S3 (S3-compatible storage)** to:  

1. Generate **pre-signed URLs** for uploading files directly to S3.  
2. Accept **CSV/XLSX uploads**, count the number of rows, and return the row count along with a pre-signed upload URL.  

---

## Features

- Load configurations from `.env` file using **Pydantic Settings**.  
- Use **Boto3** to connect to Tebi S3 storage.  
- API endpoint for generating **pre-signed upload URLs**.  
- API endpoint for uploading CSV/XLSX and returning row count.  
- Supports **CSV** (skips header) and **Excel (.xlsx)** files.  

---