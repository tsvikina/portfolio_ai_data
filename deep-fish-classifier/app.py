# Gradio app script 
from fastai.vision.all import *
import gradio as gr

learn = load_learner('deep_fish_classifier.pkl')

# Prediction function
def classify_image(img):
    pred_class, pred_idx, probs = learn.predict(img)
    return f"{pred_class} ({probs[pred_idx]:.2%})"

# Building Gradio interface
demo = gr.Interface(fn=classify_image, inputs="image", outputs="text")
demo.launch()
