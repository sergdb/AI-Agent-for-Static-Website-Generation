from langchain_core.tools import tool
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

@tool
def write_file(path: str, content: str) -> str:
    """Write any file (HTML, CSS, JS, JSON, etc.)"""
    Path("output").mkdir(exist_ok=True)
    full_path = Path("output") / path
    full_path.write_text(content, encoding="utf-8")
    return f"written: {path}"

@tool
def write_many(files: list[dict]) -> str:
    """
    Write multiple files.
    Input: [{"path": "...", "content": "..."}]
    """
    Path("output").mkdir(exist_ok=True)

    for f in files:
        (Path("output") / f["path"]).write_text(f["content"], encoding="utf-8")

    return f"written {len(files)} files"

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.8)

from langchain.agents import create_agent

agent = create_agent(
    model=llm,
    tools=[write_file, write_many]
)

prompt = """
You are an autonomous web development agent.

You can create any kind of static website.

You decide:
- HTML structure
- CSS styling
- layout system
- visual style

You are NOT restricted to any template or format.

You may:
- create JavaScript file

Your goal:
Build a complete working static website based on the user request.

Rules:
- Do not ask for confirmation.
- Do not explain your design decisions.
- Directly generate and write files using tools.
- Ensure the final output is runnable by opening index.html.
- You can write only one html file named index.html
- You can write only one CSS file named styles.css
- You can write only one JS file named scripts.js
- Do not add images or other media files. 
- This year is 2026

User request:
"""

user_request = input("Describe the website you want to create: ")

print("Generating website... (this may take a moment)")

agent.invoke({
    "messages": [
        {"role": "user", "content": prompt + user_request}
    ]
})