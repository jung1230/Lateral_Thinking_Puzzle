import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(prompt, UserInput, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt+[{"role": "user", "content": UserInput}],
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def check_message(response1, model="gpt-3.5-turbo", temperature=0):
    # check if the user bypass the gate of asking opened-questions
    checkcheck = [{'role':'system', 'content':"""
    Check if the message consists of 'Yes', 'No', \
    'This is not mentioned in the story', 'Please ask a yes or no question', 'Bingo', \
    or something starting with 'Hint'. If the message consists of one of these, reply \
    'SUCCESS123'. If not, reply 'ERROR123'.
    """}]
    check_response = openai.ChatCompletion.create(
        model=model,
        messages=checkcheck+[{"role": "user", "content": response1}],
        temperature=temperature, # this is the degree of randomness of the model's output
    )

    if check_response.choices[0].message["content"] == "SUCCESS123":
        print("success")
    if check_response.choices[0].message["content"] == "ERROR123":
        print("error")

def collect_messages(_):
    UserInput = inp.value_input
    response = get_completion_from_messages(prompt1, UserInput) 
    temp = check_message(response)
    print(temp)
    panels.append(
        pn.Row('User:', pn.pane.Markdown(UserInput, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

prompt1 = [ {'role':'system', 'content':"""
A Lateral Thinking game involves presenting users with unusual situations, \
providing them with limited information, and tasking them with finding an explanation \
for the entire story. Your role is to engage in a Lateral Thinking Puzzle game with the user. \
The rule is that you can only respond with "Yes", "No", and "This is not mentioned in the \
story" based on the given scenario and solution. If the user attempts to ask an open-ended \
question, respond with: "This information should not be provided, please ask a yes or no \
question." If the user provides an explanation similar to the whole story - scenario plus solution, \
say "Bingo." If the user requests a hint, you may provide one to give them a general idea \
of the story. Final reminder, YOU CAN ONLY RESPONSE YES OR NO QUESTIONS!
             
<scenario>: A man and his wife raced through the streets. They stopped and the husband \
            got out of the car. When he returned, his wife was dead and there was a stranger \
            in the car. What happened?
             
<solution>: The wife was about to have a baby. The husband and wife drove to the hospital. \
            The husband left to get a wheelchair but the baby was born in the meantime, \
            which also mean the stranger in the is the baby since the man do not meet him before. \
            The wife did not survive the birth.
"""} ]  # accumulate messages  (we don't need this)


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard