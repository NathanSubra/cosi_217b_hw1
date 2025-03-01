class Notebook:
    def __init__(self):
        self.notes = {}

    def add_note(self, title, content):
        if title in self.notes:
            self.notes[title+" 2"] = content
        else:
            self.notes[title] = content

    def get_note(self, title):
        if title in self.notes:
            return self.notes[title]
        else:
            return None

    def get_notes(self):
        return self.notes