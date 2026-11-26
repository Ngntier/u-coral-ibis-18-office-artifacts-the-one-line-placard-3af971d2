import os

# Catalogue fragments, assembled in museum-placard order.
FRAGMENTS = [
    "Stapler, c. 1998.",
    "Steel and regret.",
    "Bound souls to quarterly reports; the empire fell, the staples held.",
    "Donated by the Department of Unfinished Business.",
]
ENTRY = " ".join(FRAGMENTS)

# Competition rules: one line, at most 180 characters, non-empty, and the
# placard must still carry its catalogue date, material, and donor.
MAX_LENGTH = 180
REQUIRED_FACTS = ("c. 1998", "Steel", "Department of Unfinished Business")


def validate(entry: str) -> None:
    if not entry.strip():
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_LENGTH:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_LENGTH} limit")
    for fact in REQUIRED_FACTS:
        if fact not in entry:
            raise ValueError(f"entry is missing required fact: {fact}")


OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    validate(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
