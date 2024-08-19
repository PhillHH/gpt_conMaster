from datetime import datetime

class Branch:
    def __init__(self, branch_id, chat_id, parent_id=None, content=None):
        self.branch_id = branch_id
        self.chat_id = chat_id
        self.parent_id = parent_id
        self.content = content
        self.created_at = datetime.utcnow()