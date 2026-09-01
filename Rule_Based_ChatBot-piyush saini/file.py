from pathlib import Path

file_path = Path(__file__).with_name("file.txt")

if file_path.exists():
    print("\n FILE FOUND!\n")

with file_path.open(encoding="utf-8") as f:
    print(f.read())
