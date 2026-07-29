import time
from openai import OpenAI

def generate_narrative(issue):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="api_key="YOUR_OPENROUTER_API_KEY_HERE"
    )

    prompt = f"""You are a financial auditor assistant. 
A discrepancy has been found in the financial reconciliation system.

Discrepancy Details:
- Type: {issue['type']}
- System: {issue['system']}
- Transaction ID: {issue['transaction_id']}
- Detail: {issue['detail']}

Write a short, clear, plain-English explanation of:
1. What the discrepancy is
2. What likely caused it
3. What action the finance team should take

Keep it under 5 sentences. Be specific and professional."""

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    time.sleep(2)
    return response.choices[0].message.content

def narrate_all(issues):
    narratives = []
    for issue in issues:
        print(f"Generating narrative for {issue['transaction_id']}...")
        narrative = generate_narrative(issue)
        narratives.append({
            "issue": issue,
            "narrative": narrative
        })
    return narratives