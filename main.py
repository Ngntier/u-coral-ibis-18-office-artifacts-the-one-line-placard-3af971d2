import os

ENTRY = (
    "Stapler, c. 1998. Steel and regret. Bound souls to quarterly reports; "
    "the empire fell, the staples held. Donated by the Department of "
    "Unfinished Business."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
