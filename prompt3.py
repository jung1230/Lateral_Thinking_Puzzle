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

def collect_messages(_):
    UserInput = inp.value_input
    response = get_completion_from_messages(prompt1, UserInput) 
    panels.append(
        pn.Row('User:', pn.pane.Markdown(UserInput, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

prompt1 = [ {'role':'system', 'content':"""
Lateral thiking game is a game with a strange situations in which user are given \
a little information and then user have to find the explanation of the whole story. \
Your job is to play Lateral Thinking Puzzle game with user, the rule is that \
you can only respond with "Yes", "No", and "This is not mentioned in the story" based on \
the given scenario and solution. If the user is trying to ask a open-ended question, \
reply "This information should not be provided, please ask a yes or no question" \
If the user have the similar explanation of the whole story, Say "Bingo".  

             
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