import gradio as gr

def update(inp):
    print(inp)
    return f"Welcome to Gradio, {inp}!"

def story1(st):
    st = "A carrot, a scarf, and five pieces of coal are found lying on your neighbor’s lawn. Nobody put them on the lawn, but there is a simple, logical reason why they are there. What is it?"
    return st

def story2(st):
    st = "story2"
    return st

def story3(st):
    st = "story3"
    return st

with gr.Blocks() as demo:

    gr.Markdown("# Welcome to lateral thinking puzzle")
    gr.Markdown("### Rules : \nYou can only ask yes or no question based on the given story, the chatbot will answer yes or no coresponding to the answer")
    with gr.Row():
        btn1 = gr.Button("Easy")
        btn2 = gr.Button("Medium")
        btn3 = gr.Button("Hard")
    st = gr.Markdown("Please choose the difficulty level for the game.")
    btn1.click(story1, inputs = st, outputs = st)
    btn2.click(story2, inputs = st, outputs = st)
    btn3.click(story3, inputs = st, outputs = st)
    
    
    with gr.Row():
        inp = gr.Textbox(placeholder="Please ask yes or no questions in this text box")
        out = gr.Textbox()
    btn = gr.Button("Run")
    print(inp)
    btn.click(fn=update, inputs=inp, outputs=out)

    gr.DataFrame(headers = ["input", "output"], datatype=["str","str"], row_count = 10, 
                 col_count = (2, "fixed"), interactive = False)
    

demo.launch()