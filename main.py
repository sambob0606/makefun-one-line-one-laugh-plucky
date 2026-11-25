"""Write one funny line for the One Line, One Laugh bounty."""

from pathlib import Path

LINE = (
    'My cat left a dead mouse on my pillow, his way of saying: '
    '"One of us finishes things around here."'
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
