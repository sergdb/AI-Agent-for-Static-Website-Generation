# AI Agent for Static Website Generation

A simple LangChain-based agent project that generates static website files and writes them to the `output/` folder.

## Project Structure

- `main.py` — main Python script that defines tools and starts the agent
- `requirements.txt` — Python dependencies required by the project
- `output/` — generated website files are written here at runtime
- `.env` — environment variable support for OpenAI credentials

## Requirements

- Python
- `pip` available
- OpenAI API key configured in `.env`

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage

1. Create a `.env` file (or update `.env.example`) with your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```
2. Run the project:
   ```bash
   python main.py
   ```
3. Follow the prompt and let the agent generate files in the `output/` directory.

## Dependencies

- `langchain`
- `langchain-core`
- `langchain-openai`
- `python-dotenv`
- `openai`

## Notes

- The code uses `langchain_openai.ChatOpenAI` with the GPT-4o model.
- Generated files are written to `output/` using the provided tool functions.
