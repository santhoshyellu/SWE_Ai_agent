import json
import google.generativeai as genai
from ai_agent.memory import MemoryManager
from ai_agent.tool_registry import ToolRegistry
from ai_agent.observer import Observer
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class Agent:
    def __init__(self, memory: MemoryManager, tool_registry: ToolRegistry):
        self.memory = memory
        self.tool_registry = tool_registry
        self.model = genai.GenerativeModel('models/gemini-1.0-pro')
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, event: str, data):
        for observer in self.observers:
            observer.update(event, data)

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, event: str, data):
        for observer in self.observers:
            observer.update(event, data)

    def run(self):
        print("AI Agent started. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            self.memory.add_message("user", user_input)
            response = self.process_request(user_input)
            print(f"Agent: {response}")
            self.memory.add_message("assistant", response)

    def process_request(self, user_input: str) -> str:
        # Get tool descriptions
        tools_desc = self.tool_registry.list_tools()
        tools_str = "\n".join([f"- {name}: {desc}" for name, desc in tools_desc.items()])

        # Prompt for reasoning
        prompt = f"""
You are an AI assistant with access to tools. Use the ReAct pattern: Reason step by step, then Act if needed.

Available tools:
{tools_str}

Conversation history:
{self.memory.get_history()}

User: {user_input}

If you need to use a tool, respond with JSON: {{"tool": "tool_name", "args": {{"key": "value"}}}}
Otherwise, respond with the final answer.
"""

        # Mock response for testing - replace with actual API call when API is set up
        # if "2+2" in user_input:
        #     response = '{"tool": "calculator", "args": {"expression": "2+2"}}'
        # else:
        #     response = "Hello! How can I help you today? If you need calculations, weather, time, translation, or file reading, let me know!"
        try:
            response = self.model.generate_content(prompt).text.strip()
        except Exception as e:
            response = "API NOT FUNCTIONAL"

        # Check if it's a tool call
        try:
            tool_call = json.loads(response)
            if "tool" in tool_call:
                tool = self.tool_registry.get_tool(tool_call["tool"])
                result = tool.execute(**tool_call.get("args", {}))
                self.notify_observers("tool_used", {"tool": tool_call["tool"], "args": tool_call.get("args", {}), "result": result})
                # Observe and reason again
                observe_prompt = f"""
Tool result: {result}

Now, provide the final answer based on the tool result.
"""
                try:
                    final_response = self.model.generate_content(observe_prompt).text.strip()
                except Exception as e:
                    final_response = f"API NOT FUNCTIONAL - Tool result: {result}"
                return final_response
        except json.JSONDecodeError:
            pass

        return response