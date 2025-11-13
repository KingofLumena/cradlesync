class EchoMemory:
    def __init__(self):
        self.memory = []

    def store(self, phrase):
        self.memory.append(phrase)

    def recall(self):
        return self.memory
