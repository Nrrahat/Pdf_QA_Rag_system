
from app.chunking.chunk_pipline import hybrid_chunking


if __name__ == "__main__":
    # Point it to your test directories
    hybrid_chunking(input_dir="app/test/test_input", process_dir="app/test/test_output")
    print("Chunking pipeline completed! Check the test_output folder.")