# external imports
import sys
from pathlib import Path

import gradio as gr

# internal imports
sys.path.append(str(Path(__file__).parent.parent))


# define the inputs
def calc_score(inputs: str) -> dict:
    prediction = [
        {"label": "positive", "score": 0.9999, "input": inputs},
        {"label": "negative", "score": 0.0001, "input": inputs},
    ]
    # convert list to dict
    result = {}
    pred = prediction[0]
    result[pred["label"]] = pred["score"]
    return result


# definne the gradio interface
demo = gr.Interface(
    title="AWS Lambda Gradio Demo",
    fn=calc_score,
    inputs=gr.Textbox(placeholder="Enter a positive or negative sentence here..."),
    outputs="label",
    examples=[
        ["I Love Serverless Machine Learning"],
        ["Running Gradio on AWS Lambda is amazing"],
    ],
    allow_flagging="never",
)


if __name__ == "__main__":
    demo.launch(
        server_port=8080,
    )
