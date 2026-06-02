import os
from pathlib import Path
import pymupdf4llm
from app.ingestion.pdf_loader import load_pdf

def main():
   load_pdf("app/data/raw/pdfs","app/data/processed")


if __name__ == "__main__":
    main()