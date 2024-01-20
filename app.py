import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text",
                     title="AI Chatbot", description="Ask anything you want",
                     theme="compact")

iface.launch(share=True)