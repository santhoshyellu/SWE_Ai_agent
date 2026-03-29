from ai_agent.agent import Agent
from ai_agent.memory import MemoryManager
from ai_agent.tool_registry import ToolRegistry
from ai_agent.observer import LoggingObserver
from ai_agent.tools.calculator import CalculatorTool
from ai_agent.tools.weather import WeatherTool
from ai_agent.tools.time_tool import TimeTool
from ai_agent.tools.translation import TranslationTool
from ai_agent.tools.file_reader import FileReaderTool

def main():
    memory = MemoryManager()
    registry = ToolRegistry()

    # Register tools
    registry.register(CalculatorTool())
    registry.register(WeatherTool())
    registry.register(TimeTool())
    registry.register(TranslationTool())
    registry.register(FileReaderTool())

    agent = Agent(memory, registry)
    logging_observer = LoggingObserver()
    agent.add_observer(logging_observer)
    agent.run()

if __name__ == "__main__":
    main()