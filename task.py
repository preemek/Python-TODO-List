class Task:
    def __init__(self, title, description, deadline, status=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        self.status = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["description"], data["deadline"], data["status"])