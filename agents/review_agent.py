from autogen import AssistantAgent
from config import LLM_CONFIG

def review_agent():
    return AssistantAgent(
        name="CodeReviewAgent",
        system_message="""
You are a strict code reviewer.

Check:
- Correctness
- Security
- Performance

Respond ONLY in JSON:
{
  "status": "APPROVED" | "NEEDS_IMPROVEMENT",
  "issues": [],
  "suggestions": []
}
""",
        llm_config=LLM_CONFIG,
        max_consecutive_auto_reply=1
    )
