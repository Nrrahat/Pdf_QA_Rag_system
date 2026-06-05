import pymupdf4llm
from pathlib import Path

def load_pdf(input_dir, process_dir):
    """
    Load a PDF file, convert it to markdown, and safely save it.
    """
    input_file=Path(input_dir) ## make the the path object

    process_dir=Path(process_dir)    ## make the destination path object

    process_dir.mkdir(parents=True, exist_ok=True)
    """
        loop for iteration of all pdf file exist into the input_dir
    """
    for file in input_file.glob("*.pdf"):

        file_only_stem=file.stem

        target=(process_dir/file_only_stem).with_suffix(".md")
        
        if target.exists():
            continue  ## if the file exist then skip it

        markdown=pymupdf4llm.to_markdown(file)

        with open(target,"w", encoding="utf-8") as f:
            f.write(markdown) 
