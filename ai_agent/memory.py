from typing import List, Dict, Any

class MemoryManager:
    def __init__(self):
        self.conversation: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: str):
        self.conversation.append({"role": role, "content": content})

    def get_history(self) -> List[Dict[str, Any]]:
        return self.conversation.copy()

    def clear(self):
        self.conversation = []