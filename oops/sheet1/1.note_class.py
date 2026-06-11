class Note:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return f"{self.title} : {self.content}"

def create_notes() -> list[str]:
    note1 = Note("Meeting Notes", "Discuss project status with team.")
    note2 = Note("Grocery List", "Eggs, Milk, Bread")
    return [str(note1), str(note2)]

result = create_notes()
