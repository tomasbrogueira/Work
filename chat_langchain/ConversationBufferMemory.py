import json
# Other existing imports...

class ConversationBufferMemory:
    def __init__(self, memory_key='conversation_memory.json', return_messages=True):
        self.memory_key = memory_key
        self.return_messages = return_messages
        self.memory = self._load_memory()

    def _load_memory(self):
        try:
            with open(self.memory_key, 'r') as file:
                memory = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            memory = []
        return memory

    def _save_memory(self):
        with open(self.memory_key, 'w') as file:
            json.dump(self.memory, file)

    def remember(self, message):
        self.memory.append(message)
        self._save_memory()

    def recall(self):
        return self.memory if self.return_messages else []
