def create_file(filename: str):
    with open(filename, "w"):
        pass

def write_to_file(filename: str, text: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def read_from_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
