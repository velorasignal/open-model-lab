from lab.memory import ConversationMemory

if __name__ == "__main__":
    memory = ConversationMemory(); memory.add("user", "My name is Ada."); memory.add("assistant", "Nice to meet you!")
    print(memory.prompt())
