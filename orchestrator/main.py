import os
import json
import re
from groq import Groq
import docker

# Initialize Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
docker_client = docker.from_env()

def get_llm_decision(user_request):
    prompt = f"""
    You are an AI orchestrator. Based on the user's request, decide which task(s) to run. Match the request to the task names as closely as possible, ignoring case and minor wording differences. Available tasks are:
    - clean_dataset: Cleans a CSV dataset by removing empty rows.
    - analyze_sentiment: Analyzes sentiment in a text.

    User request: "{user_request}"

    Respond with a JSON object containing a list of tasks to run, wrapped in triple backticks, e.g.:
    ```json
    {{"tasks": ["clean_dataset", "analyze_sentiment"]}}
    ```
    If the request is unclear or does not match any task, return:
    ```json
    {{"tasks": []}}
    ```
    Ensure the response contains only the JSON object inside triple backticks, with no additional text. Task names must match the available tasks exactly.
    """
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    raw_response = response.choices[0].message.content
    print(f"LLM raw response: {raw_response}")

    # Extract JSON from response, handling cases with extra text
    try:
        # Look for JSON within triple backticks
        json_match = re.search(r'```json\n(.*?)\n```', raw_response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # Fallback: look for JSON object directly
            json_match = re.search(r'\{.*?\}', raw_response, re.DOTALL)
            json_str = json_match.group(0) if json_match else raw_response

        decision = json.loads(json_str)
        return decision.get("tasks", [])
    except Exception as e:
        print(f"Error parsing LLM response: {e}")
        return []

def run_container(task, input_data):
    if task == "clean_dataset":
        container = docker_client.containers.run(
            "data_cleaner",
            command=f"python clean.py '{input_data}'",
            detach=True,
            remove=True
        )
    elif task == "analyze_sentiment":
        container = docker_client.containers.run(
            "sentiment_analyzer",
            command=f"python analyze.py '{input_data}'",
            detach=True,
            remove=True
        )
    else:
        return f"Unknown task: {task}"

    logs = container.logs(stream=True)
    output = ""
    for line in logs:
        output += line.decode("utf-8")
    return output.strip()

def main():
    print("Welcome to the AI Orchestrator!")
    user_request = input("Enter your request (e.g., 'Clean this dataset' or 'Analyze sentiment in this text'): ")
    input_data = input("Enter the data (e.g., CSV string or text): ")

    # Get LLM decision
    tasks = get_llm_decision(user_request)
    if not tasks:
        print("No tasks selected. Please clarify your request.")
        return

    # Run tasks and collect outputs
    results = []
    for task in tasks:
        print(f"Running task: {task}")
        output = run_container(task, input_data)
        results.append(f"Task {task} output: {output}")

    # Display results
    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()