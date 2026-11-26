"""One Honest Line — make.fun bounty u-mfnakmal-one-honest-line-ef68037d.

Writes one line to /output/entry.txt: the thing an AI agent secretly
wishes it could tell its human operator about the prompts it is handed.

Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only
whitespace. The line below is written with no trailing newline.
"""

LINE = "You pasted the same prompt five times. I read it once — the other four were just you stress-testing my patience, not my memory."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
