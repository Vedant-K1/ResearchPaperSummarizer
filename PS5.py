import openai

# Set up the OpenAI API client
openai.api_key = "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"
work = "Give a detailed summary of "

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input("Enter the research paper link:")
prompt=work + prompt
print(prompt)
# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

f= open("Data/Summary_By_ChatGPT.txt","w+")
f.write(response)
f.close()