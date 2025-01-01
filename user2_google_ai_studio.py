import os
import logging
import google.generativeai as genai
import absl.logging


logging.basicConfig(level=logging.INFO)
absl.logging.set_verbosity(absl.logging.ERROR)
absl.logging.set_stderrthreshold('error')



genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("hi my name is akhilesh and not feeling well it feels like I'm lost and what to do don't know please give me step by step guide what to do ")
print(response.text)
