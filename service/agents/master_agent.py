from core.logger import logger

class MasterAgent:
    def __init__(self):
        logger.info("MasterAgent initialized")

    def execute(self, task_input):
        return {"response": "Hi, I'm Nexa! How can I help you today?"}
