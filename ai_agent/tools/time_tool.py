from datetime import datetime
from ai_agent.base_tool import BaseTool

class TimeTool(BaseTool):
    @property
    def name(self) -> str:
        return "time"

    @property
    def description(self) -> str:
        return "Gets the current date and time."

    def execute(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")