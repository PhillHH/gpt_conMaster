import json
import zlib

class ContextManager:
    def __init__(self):
        self.contexts = {}  # Stores contexts by chat IDs
        self.thread_contexts = {} # Stores contexts by thread IDs

    def add_message(self, chat_id, user_message=None, assistant_message=None):
        """Fügt eine Nachricht zum Kontext hinzu und speichert diesen."""
        context = self.get_context(chat_id)
        if user_message:
            context.append({"role": "user", "content": user_message})
        if assistant_message:
            context.append({"role": "assistant", "content": assistant_message})
        self.save_context(chat_id, context)

    def get_context(self, chat_id):
        """Returns the entire context of the chat."""
        context = self.contexts.get(chat_id, [])
        if not context:
           # Adds a default message to ensure that the API is not called with an empty context.
            context.append({"role": "system", "content": "You are a helpful assistant."})
        return context

    def archive_context(self, chat_id):
        """Archives the context of a chat by compressing it and returning the compressed context."""
        if chat_id in self.contexts:
            context_json = json.dumps(self.contexts[chat_id])
            compressed_context = zlib.compress(context_json.encode('utf-8'))
            return compressed_context
        return None

    def load_context(self, chat_id, compressed_context):
        """Loads and decompresses an archived context and restores it for chat."""
        decompressed_context = zlib.decompress(compressed_context).decode('utf-8')
        self.contexts[chat_id] = json.loads(decompressed_context)

    def clear_context(self, chat_id):
        """Clears the context of a chat when it is no longer needed."""
        if chat_id in self.contexts:
            del self.contexts[chat_id]

    def save_context(self, chat_id, context):
        """Saves the context of a chat."""
        self.contexts[chat_id] = context
