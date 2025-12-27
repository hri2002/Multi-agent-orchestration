import streamlit as st
import difflib
import json
from orchestrator import run_pipeline

st.set_page_config(page_title="Multi-Agent Coding Framework", layout="wide")

st.title("🤖 Multi-Agentic Coding Framework")
st.caption("AutoGen-powered collaborative pipeline for software development ")

user_input = st.text_area(
    "📥 Enter Software Requirement", 
    placeholder="Example: Build a Python script for real-time weather alerts...",
    height=100
)

if st.button("🚀 Run Pipeline"):
    if not user_input.strip():
        st.warning("Please provide a requirement description.")
    else:
        # Progress UI elements
        progress_bar = st.progress(0)
        status_info = st.empty()
        
        # UI Tabs for organized output 
        tab_req, tab_code, tab_rev, tab_doc, tab_test, tab_dep = st.tabs([
            "📋 Requirements", "💻 Code Workbench", "🔍 Review Logs", "📄 Documentation", "🧪 Test Cases", "⚙️ Deployment"
        ])

        versions = {"v1": "", "v2": "", "v3": ""}

        # Active processing spinner 
        with st.spinner("Agents are collaborating (Analyzing ➔ Coding ➔ Reviewing)..."):
            for data in run_pipeline(user_input):
                key, content = data[0], data[1]
                
                if key == "progress":
                    progress_bar.progress(data[1])
                    status_info.markdown(f"**Current Status:** {data[2]}")
                
                elif key == "requirements":
                    tab_req.subheader("Structured Requirements")
                    tab_req.json(content)

                elif "code_v" in key:
                    v_label = key.split("_")[1]
                    versions[v_label] = content
                    with tab_code:
                        st.subheader(f"Python Code Output ({v_label}) ")
                        if v_label != "v1" and versions["v1"]:
                            st.write("🔄 **Diff from v1:**")
                            diff = difflib.ndiff(versions["v1"].splitlines(), content.splitlines())
                            st.code("\n".join(diff), language="diff")
                        st.code(content, language="python")

                elif "review_v" in key:
                    v_num = key.replace("review_v", "")
                    with tab_rev:
                        with st.expander(f"📜 Detailed Review Log - Version {v_num}", expanded=True):
                            # Pretty printing logic for review logs 
                            if "APPROVED" in content.upper():
                                st.success("✅ **Status: APPROVED**")
                            else:
                                st.warning("⚠️ **Status: REVISIONS NEEDED**")
                            
                            st.markdown("### Agent Feedback:")
                            st.json(content)

                elif key == "docs":
                    tab_doc.subheader("Technical Documentation ")
                    tab_doc.markdown(content)
                
                elif key == "tests":
                    tab_test.subheader("Unit & Integration Tests ")
                    tab_test.code(content, language="python")
                
                elif key == "deployment":
                    tab_dep.subheader("Deployment Script ")
                    tab_dep.code(content, language="bash")

        status_info.success("✅ Execution Finished Successfully!")
        st.balloons()