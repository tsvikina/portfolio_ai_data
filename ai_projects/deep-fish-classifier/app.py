# Gradio app script 
from fastai.vision.all import *
import gradio as gr

# Load the model
learn = load_learner('deep_fish_classifier.pkl')

# Define prediction function
def predict(img):
    pred, idx, probs = learn.predict(img)
    return {str(learn.dls.vocab[i]): float(probs[i]) for i in range(len(probs))}

# Create Gradio interface
iface = gr.Interface(fn=predict, inputs=gr.Image(type="pil"), outputs=gr.Label())
iface.launch()

