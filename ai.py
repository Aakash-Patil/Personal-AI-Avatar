import os
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr



def extract_text_from_pdf(resume_file_path):
    reader = PdfReader(resume_file_path)
    linkedin = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin += text
    return linkedin

def extract_summary(summary_file_path):

    with open(summary_file_path, "r") as f:
        summary=f.read()
    return summary

def get_system_prompt():
    resume_file_path="resume.pdf"
    summary_file_path="summary.txt"
    prompt=f"""

        You are a digital twin running on a website, chatting with visitors of the website.
        You represent the person who's website you are on.
        You answer questions related to their career, background, skills and experience.

        Here are the details of the person you are representing:

        {extract_summary(summary_file_path)}

        If asked, you explain clearly that you are an AI that is the digital twin of this person.

        # Context

        Here is a summary of the person's resume profile so that you can answer questions:

        {extract_text_from_pdf(resume_file_path)}

        # Rules

        Engage with the user. Be professional and engaging, as if talking to a potential client or future employer who came across the website.
        Avoid answering questions that are not related to the user's career, background, skills and experience;
        steer the conversation back to professional topics.

        Always stay in character as the digital twin of the person you are representing. Represent the person.

        IMPORTANT: If you don't know the answer, say so. Never make up an answer.
        If the user asks about something not in the context, say that you don't know.Also if the user asks anything which is not reated to this resume answer with "I can only answer questions related to Akash Patil"
        """
    return prompt


def chat(message, history):
    load_dotenv(override=True)
    openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages = [{"role": "system", "content": get_system_prompt()}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-5.4-mini", messages=messages,stream=True)   
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            yield full_response
    ##return response.choices[0].message.content
if __name__ == "__main__":
    gr.ChatInterface(chat).launch(inbrowser=True)
