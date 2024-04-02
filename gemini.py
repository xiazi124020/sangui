"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import traceback
import google.generativeai as genai
import time, os
from dotenv import load_dotenv

load_dotenv()

def create_text(question, content):
    max_retries = 4  # 最大重试次数
    retries = 0  # 当前重试次数
    wait_time = 5  # 重试间等待时间，单位为秒
    while retries < max_retries:

        try:
            GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
            genai.configure(api_key=GOOGLE_API_KEY)

            # Set up the model
            generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 10000,
            }

            safety_settings_NONE=[
                { "category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE" },
                { "category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE" },
                { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE" },
                { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
            ]

            model = genai.GenerativeModel(model_name="gemini-pro",
                                        generation_config=generation_config,
                                        safety_settings=safety_settings_NONE)

            convo = model.start_chat(history=[
            ])

            convo.send_message(f"{question}\n{content}")
            return convo.last.text
        except Exception as e:    
            retries += 1  # 增加重试计数
            print(f"Attempt {retries} failed: {e}")
            traceback.print_exc()
            if retries < max_retries:
                time.sleep(wait_time)  # 等待一段时间后重试
            else:
                return ''