from ai_agent.base_tool import BaseTool

class FileReaderTool(BaseTool):
    @property
    def name(self) -> str:
        return "file_reader"

    @property
    def description(self) -> str:
        return "Reads the content of a local file. Args: file_path (str)"

    def execute(self, file_path: str) -> str:
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"