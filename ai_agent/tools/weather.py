import requests
from ai_agent.base_tool import BaseTool

class WeatherTool(BaseTool):
    @property
    def name(self) -> str:
        return "weather"

    @property
    def description(self) -> str:
        return "Gets weather for a city. Args: city (str)"

    def execute(self, city: str) -> str:
        # Mock for now, replace with real API
        return f"Weather in {city}: Sunny, 25°C"