import ast
import operator
from ai_agent.base_tool import BaseTool

class CalculatorTool(BaseTool):
    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Performs basic arithmetic calculations. Args: expression (str)"

    def execute(self, expression: str) -> str:
        try:
            # Safe evaluation
            result = eval(expression, {"__builtins__": {}}, {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv})
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"