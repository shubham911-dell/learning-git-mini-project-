from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

# First API call with reasoning
response = client.chat.completions.create(
  model="google/gemini-2.0-flash-exp:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ]
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message

print("First Response:")
print(f"Content: {response.content}")
if hasattr(response, 'reasoning_details') and response.reasoning_details:
    print(f"Reasoning: {response.reasoning_details}")
print("\n" + "="*50 + "\n")

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="google/gemini-2.0-flash-exp:free",
  messages=messages
)

print("Second Response:")
print(f"Content: {response2.choices[0].message.content}")
if hasattr(response2.choices[0].message, 'reasoning_details') and response2.choices[0].message.reasoning_details:
    print(f"Reasoning: {response2.choices[0].message.reasoning_details}")

