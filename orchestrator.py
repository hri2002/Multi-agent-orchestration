from autogen import UserProxyAgent 
from agents.requirement_agent import requirement_agent
from agents.coding_agent import coding_agent
from agents.review_agent import review_agent
from agents.documentation_agent import documentation_agent
from agents.test_agent import test_agent
from agents.deployment_agent import deployment_agent

def run_pipeline(user_input):
    """
    Orchestrates the Multi-Agentic pipeline using AutoGen.
    Yields content step-by-step for real-time Streamlit updates.
    """
    user = UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config={"work_dir": "coding", "use_docker": False},
        llm_config=False,
        max_consecutive_auto_reply=0
    )

    # Initialize all required agents
    agents = {
        "req": requirement_agent(),
        "code": coding_agent(),
        "review": review_agent(),
        "doc": documentation_agent(),
        "test": test_agent(),
        "deploy": deployment_agent()
    }

    # Step 1: Requirement Analysis
    yield "progress", 10, "Requirement Analysis Agent is refining input..."
    req_summary = user.initiate_chat(agents["req"], message=user_input).summary
    yield "requirements", req_summary

    # Step 2: Initial Coding 
    yield "progress", 30, "Coding Agent is generating Python code (v1)..."
    current_code = user.initiate_chat(agents["code"], message=req_summary).summary
    yield "code_v1", current_code

    # Step 3: Iterative Review Loop
    for i in range(2):
        version = i + 1
        yield "progress", 40 + (i * 15), f"Code Review Agent is analyzing v{version}..."
        
        review_result = user.initiate_chat(agents["review"], message=current_code).summary
        yield f"review_v{version}", review_result
        
        if "APPROVED" in review_result.upper():
            break
        
        # Improvement iteration 
        yield "progress", 55 + (i * 15), f"Coding Agent is incorporating feedback for v{version+1}..."
        refine_msg = f"Feedback: {review_result}\n\nOriginal Code:\n{current_code}"
        current_code = user.initiate_chat(agents["code"], message=refine_msg).summary
        yield f"code_v{version+1}", current_code

    # Step 4: Final Deliverables
    yield "progress", 85, "Documentation Agent is generating technical docs..."
    yield "docs", user.initiate_chat(agents["doc"], message=current_code).summary
    
    yield "progress", 90, "Test Case Generation Agent is creating unit/integration tests..."
    yield "tests", user.initiate_chat(agents["test"], message=current_code).summary
    
    yield "progress", 95, "Deployment Agent is preparing scripts..."
    yield "deployment", user.initiate_chat(agents["deploy"], message=current_code).summary
    
    yield "progress", 100, "Multi-agent pipeline complete!"


