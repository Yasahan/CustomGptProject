from openai import OpenAI

client = OpenAI(api_key="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")
import gradio as gr


messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text",
                     title="AI Chatbot", description="Ask anything you want",
                     theme="compact")

iface.launch(share=True)