from autogen import AssistantAgent
from config import LLM_CONFIG

def documentation_agent():
    return AssistantAgent(
        name="DocumentationAgent",
        system_message="""
Generate professional Markdown documentation:
- Overview
- Architecture
- Code explanation
- Setup
- Usage
""",
        llm_config=LLM_CONFIG,
        max_consecutive_auto_reply=1
    )
