AI Orchestrator
A simple AI-powered task orchestrator that leverages a Large Language Model (LLM) to parse user requests and automatically execute relevant containerized tasks like data cleaning and sentiment analysis.

✨ Features
🔗 LLM Integration – Uses Groq’s llama3-70b-8192 model to intelligently parse user intent.

🐳 Containerized Services – Clean and modular tasks using Docker containers.

🧹 Data Cleaner – Removes empty rows from CSV data using pandas.

💬 Sentiment Analyzer – Detects sentiment in text using TextBlob.

🧰 CLI Interface – Interact with the orchestrator from the command line.

🧩 Docker Compose – Handles service orchestration with ease.

📜 Logged Output – Detailed logs for every step of the execution process.

📁 Project Structure

ai-orchestrator/
├── orchestrator/
│   ├── main.py                # Main orchestrator logic
│   ├── requirements.txt       # Python dependencies
├── services/
│   ├── data_cleaner/
│   │   ├── Dockerfile
│   │   ├── clean.py
│   │   ├── requirements.txt
│   ├── sentiment_analyzer/
│   │   ├── Dockerfile
│   │   ├── analyze.py
│   │   ├── requirements.txt
├── docker-compose.yml         # Orchestration config
├── README.md                  # This file


Features Implemented
LLM Integration:

Uses Groq's Llama3-70b model to interpret user requests

Simple prompt engineering to map requests to containerized tasks

JSON response parsing with error handling

Containerized Services:

Data cleaning service (removes empty rows from CSV)

Sentiment analysis service (TextBlob-based)

Each service in its own Docker container

Orchestrator:

Coordinates the workflow

Handles user input

Manages container execution

Collects and presents results

Error Handling:

Basic error handling for LLM responses

Error handling in containerized services

⚙️ Setup Instructions
1. Install Prerequisites

Python 3.9 or higher
Docker Desktop
VS Code (optional)
Groq API Key (free signup)

2. Set Up the Project
Clone or create a folder with the structure above.

3. Install Python Dependencies

cd ai-orchestrator/orchestrator
pip install -r requirements.txt

4. Set Your Groq API Key
Windows:
set GROQ_API_KEY=your_api_key_here

macOS/Linux:
export GROQ_API_KEY=your_api_key_here

5. Build Docker Containers
From the root directory:
docker-compose build

6. Run the Orchestrator
Navigate to the orchestrator directory:

cd orchestrator
python main.py
You'll be prompted to input:

A request (e.g., "Clean this dataset")

Corresponding data (e.g., "name,age\nAlice,25\n,,30\nBob,28")

The orchestrator will:

Ask the LLM to decide the appropriate tasks.

Run the relevant Docker containers.

Show the final output.

🧠 Example Usage

Request: Clean this dataset  
Data: name,age\nAlice,25\n,,30\nBob,28

Output:
Cleaned CSV:
name,age
Alice,25
Bob,28

Input:
Request: Analyze sentiment in this text  
Data: I love this product!

Output:
Sentiment: Positive

🧭 Architecture Overview
The orchestrator follows a modular, containerized architecture:

main.py takes user input and asks the Groq LLM what needs to be done.

Based on the response, relevant containers are run via Docker Compose.

Each container performs a task:

CSV cleanup via pandas

Sentiment analysis via TextBlob

Results are collected and returned to the user in CLI.

This decoupled design allows easy scaling – just add a new service folder and map it to a task.

🧪 Demo Video
A screen recording (provided separately) demonstrates:

Cleaning a CSV dataset

Analyzing text sentiment

Orchestrator's interaction with containers

🧾 Assumptions
Inputs are raw text or CSV strings.

Groq API returns a valid JSON task list.

Docker Desktop is running during execution.

📌 Future Enhancements
Add services like:

📄 Summarization

🌐 Translation

📊 Keyword extraction

Retry mechanism for failed containers

Web interface for non-technical users

Real-time progress bar in CLI

