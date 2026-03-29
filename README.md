# AI Agent with Google Gemini API

This is an adaptive AI agent built using the Google Gemini API, following SOLID principles and design patterns.

## Features

- Modular architecture with Agent, MemoryManager, ToolRegistry, and Observer pattern for monitoring
- Supports multiple tools: Calculator, Weather, Time, Translation, FileReader
- ReAct pattern for reasoning and acting
- CLI interface with logging of tool usage

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Set up API key in .env file: `GEMINI_API_KEY=your_key_here`
3. Run: `python main.py`

## Usage

Run the agent and interact via CLI.