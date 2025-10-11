import hashlib
import sys

def get_file_hash(file_path):
    """
    Calculates the SHA-256 hash of a file.
    """
    h = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read in chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python integrity_check.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        file_hash = get_file_hash(file_path)
        print(f"SHA-256 hash of {file_path}: {file_hash}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
