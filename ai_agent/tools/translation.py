from ai_agent.base_tool import BaseTool

class TranslationTool(BaseTool):
    @property
    def name(self) -> str:
        return "translation"

    @property
    def description(self) -> str:
        return "Translates text to another language. Args: text (str), target_lang (str, e.g., 'es' for Spanish)"

    def execute(self, text: str, target_lang: str) -> str:
        # Mock translation
        translations = {
            "es": f"Translated to Spanish: {text[::-1]}",  # Simple reverse as mock
            "fr": f"Translated to French: {text.upper()}"
        }
        return translations.get(target_lang, f"Unsupported language: {target_lang}")