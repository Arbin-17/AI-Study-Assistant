import numpy as np 
import pandas as pd 

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# # -> **IMPORTING LIBRARIES :-**
# 
# **import numpy as np** :- Imports the NumPy library, which is used for numerical computations and linear algebra operations.
# 
# **import pandas as pd** :- Imports the Pandas library, which is used for data manipulation and analysis, especially for handling structured data like CSV files.
# 
# <br>
# 
# ---
# # -> LISTING INPUT FILES :-
# 
# **import os** :- Imports the os module, which provides a way to interact with the operating system, such as navigating directories and handling files.
# 
# The **os.walk('/kaggle/input')** function is used to traverse the directory /kaggle/input, which is a read-only directory in Kaggle notebooks containing input data files.
# 
# The nested for loops iterate through all the files in this directory and print their full paths using **os.path.join(dirname, filename).**
# 
# <br>
# 
# ---
# 

# In[ ]:


# get_ipython().system('pip install -q google-generativeai') ---> THIS LINE SHOWED ERROR BECAUSE OF THIS IS ONLY A JUPYTER COMMAND 


# This installs the **Google Generative AI Python SDK**, which lets you use Gemini models (like gemini-pro) directly in your code.
# 
# **!** — Tells the notebook to run this as a terminal command.
# 
# **pip install** — Installs a Python package.
# 
# **-q** — Quiet mode (hides extra output).
# 
# 
# ---

# In[ ]:


# Imports the SDK that we just installed.
import google.generativeai as genai


# INSERT HERE YOUR OWN API KEY 
api_key = ""


# Configure Gemini
 genai.configure(api_key=api_key)
# This connects the Gemini SDK to your API key


# **genai** gives access to Gemini models and their features (like text generation).
# 
# ## I. THESE STEPS SETS UP & UNLOCKS YPUR ACCESS TO GEMINI FROM YOUR NOTEBOOK.
# 
# ---

# In[ ]:


# Load the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')


# **genai.GenerativeModel(...)** :- This is how you create a Gemini model object.
# 
# **'gemini-pro'**--- This is the name of the model you're using. It’s one of Google’s powerful text generation models (like ChatGPT).
# 
# ## II. NOW YOUR MODEL IS READY TO TAKE PROMPTS AND GENERATE RESPONSES
# ---

# In[ ]:


# DON'T FORGET TO INSERT YOUR ACTUAL API KEY HERE 
genai.configure(api_key="") 


# **genai.configure(...)** :- This sets up the connection to Google’s AI services.
# 
# **api_key=" "** :- 
# **YOU NEED TO PASTE YOUR ACTUAL API KEY INSIDE THE QUOTES,**
# 
# ## III. THIS AUTHENTICATES YOUR CODE WITH THE GOOGLE GENERATIVE AI API USING YOUR API KEY
# 
# ---

# In[ ]:


# Installs the Google Generative AI Python package.
# get_ipython().system('pip install -q google-generativeai') ---> THIS LINE SHOWED ERROR BECAUSE OF THIS IS ONLY A JUPYTER COMMAND 


# Imports the library and names it genai for shorter access.
import google.generativeai as genai


# DON'T FORGET TO INSERT YOUR ACTUAL API KEY HERE 
genai.configure(api_key="")


# To check available models
for m in genai.list_models():
    print(m.name)
# Lists all available Gemini models (like gemini-pro, gemini-1.5-flash, etc.).
# Useful for choosing the correct model name in your project.


# **-q** means quiet mode, so it doesn't print unnecessary output.
# 
# ## IV. THIS BLOCK SETS UP YOUR ENVIRONMENT, LOGS YOU INTO GEMINI USING YOUR API KEY, AND SHOWS YOU WHICH MODELS ARE AVAILABLE TO USE.
# 
# ---

# In[ ]:


import google.generativeai as genai

# Step 1: INSERT YOUR ACTUAL API KEY HERE 
genai.configure(api_key="")
# Authenticates you with Google’s Generative AI service using your API key.


# Step 2: Choose a valid model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")


# Sample study input
study_text = """
Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy.
This chemical energy is stored in carbohydrate molecules, such as sugars, which are synthesized from carbon dioxide and water.
Photosynthesis occurs in the chloroplasts of plant cells and involves two main stages: the light-dependent reactions and the Calvin cycle.
"""
# Defines the input text you want to summarize.


# Step 3: Ask Gemini to summarize
response = model.generate_content(f"Summarize this for a student in simple language:\n\n{study_text}")


print("📘 Summary:\n") #Displays the generated summary to the user in a readable format.
print(response.text)   #response.text contains the summary that the model generated.


# ### "gemini-1.5-pro" is specified, but you could choose a different model from the list you found earlier.
# 
# ## V. THE PROMPT "Summarize this for a student in simple language:\n\n" IS PASSED TO GUIDE GEMINI ON HOW TO PROCESS THE INPUT TEXT.
# 
# ---

# ## VI. **FEW-SHOT PROMPTING** :- 
# 
# In this capability, we'll provide the model with a few examples of how to perform a task, and then ask it to generate content based on those examples. This is useful when the model needs to infer a pattern or generate text in a specific way.
# 
# <br>
# 
# 

# In[ ]:


                                     # FEW-SHOT PROMPTING 
# Import necessary library
import google.generativeai as genai

# Insert your actual API key
genai.configure(api_key="")

# Choose the model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# Example input text
study_text = """
Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy.
This chemical energy is stored in carbohydrate molecules, such as sugars, which are synthesized from carbon dioxide and water.
Photosynthesis occurs in the chloroplasts of plant cells and involves two main stages: the light-dependent reactions and the Calvin cycle.
"""

# Few-Shot Examples
examples = [
    "Summarize this scientific article for a student: The Theory of Relativity explains the relationship between space and time. It states that objects with mass bend space and time, and this curvature is what we perceive as gravity.",
    "Summarize this historical event: The French Revolution began in 1789 and was a period of radical social and political upheaval in France. It led to the rise of Napoleon Bonaparte."
]
# FOLLOWING THIS FORMAT WHILE SUMARIZING "


# Provide the few-shot examples and ask the model to summarize the study_text in a similar manner
prompt = f"Here are some examples of summarizing texts:\n\n{examples[0]}\n{examples[1]}\n\nNow, summarize this scientific article for a student:\n\n{study_text}"

# Generate content using the model
response = model.generate_content(prompt)

# Output the result
print("📘 Summary based on Few-Shot Prompting:\n")
print(response.text)


# --- 
# 
# ## VII. **FUNCTION CALLING** :- 
# 
# In this capability, we'll define a function (like a simple calculation or querying an external API), and ask the model to invoke this function to carry out a task.

# In[ ]:


                                        # FUNCTION CALL
# Import necessary library
import google.generativeai as genai

# Insert your actual API key
genai.configure(api_key="")

# Choose the model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# Define a function for calculating the average
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Function that simulates asking the model to call the function
def function_call_example():
    prompt = "Given a list of numbers, calculate the average."
    numbers = [10, 20, 30, 40, 50]

    # Ask the model to call the function to calculate the average
    average = calculate_average(numbers)

    response = model.generate_content(f"{prompt} Here is the list: {numbers}")
    print(f"Model says: {response.text}")
    print(f"Function call result: The average of the numbers is {average}")

# Execute the function call example
function_call_example()


# --- STREAMLIT DEPLOYMENT ---
import streamlit as st
import google.generativeai as genai

# Set page title
st.set_page_config(page_title="📚 AI Study Assistant", layout="centered")

# Title and intro
st.title("📚 AI-Powered Study Assistant")
st.markdown("This app uses **Gemini 1.5 Pro** to simplify and summarize your study material.")

# Input field
user_input = st.text_area("✏️ Enter your academic text here:", height=250)

# Set your API key (use st.secrets in production)
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

# Generate summary on button click
if st.button("🧠 Generate Summary"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            prompt = f"Summarize this for a student in simple language:\n\n{user_input}"
            response = model.generate_content(prompt)
            st.success("✅ Summary Ready!")
            st.markdown("### 📝 Simplified Summary:")
            st.write(response.text)
