import json
import argparse
import os
import sys
from utils import print_response
import openai
from openai import OpenAI

parser = argparse.ArgumentParser()

parser.add_argument('--paper_name',type=str)
parser.add_argument('--model_name',type=str, default="gpt-3.5-turbo") 
parser.add_argument('--temperature',type=float, default=1.0)
parser.add_argument('--max_tokens',type=int, default=4000)

parser.add_argument('--paper_format',type=str, default="JSON", choices=["JSON", "LaTeX"])
parser.add_argument('--pdf_json_path', type=str) # json format
parser.add_argument('--pdf_latex_path', type=str) # latex format

parser.add_argument('--output_dir',type=str, default="")

args = parser.parse_args()

paper_name = args.paper_name
paper_format = args.paper_format
pdf_json_path = args.pdf_json_path
pdf_latex_path = args.pdf_latex_path
output_dir = args.output_dir

model_name = args.model_name
temperature = args.temperature
max_tokens = args.max_tokens

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Warning: OPENAI_API_KEY not found. Using demo mode.")
    client = None
else:
    client = OpenAI(api_key=api_key)

if paper_format == "JSON":
    with open(f'{pdf_json_path}') as f:
        paper_content = json.load(f)
elif paper_format == "LaTeX":
    with open(f'{pdf_latex_path}') as f:
        paper_content = f.read()
else:
    print(f"[ERROR] Invalid paper format. Please select either 'JSON' or 'LaTeX.")
    sys.exit(0)

analyze_msg = [
    {'role': "system", "content": f"""You are an expert code analyst and software architect with deep knowledge of machine learning implementations.
You will receive a research paper in {paper_format} format. 
Your task is to analyze the paper and create detailed specifications for implementing the described methodology.

Your response should be structured as follows:

1. **Core Components**: Identify the main components and modules needed
2. **Data Processing**: Specify data loading, preprocessing, and augmentation steps
3. **Model Architecture**: Define the neural network or algorithm structure
4. **Training Pipeline**: Outline the training process, loss functions, and optimization
5. **Evaluation Metrics**: Specify how to measure performance
6. **Configuration Parameters**: List all configurable hyperparameters
7. **File Dependencies**: Identify external files, datasets, or resources needed
8. **Implementation Notes**: Important considerations and potential challenges

Please provide detailed, actionable specifications that can be directly used for implementation."""},
    {'role': "user", "content": f"Please analyze the following research paper and create detailed implementation specifications:\n\n{paper_content}"}
]

def generate_response(messages, model_name="gpt-3.5-turbo", temperature=1.0, max_tokens=4000):
    """Generate response using OpenAI API or fallback to demo mode"""
    
    if client is None:
        # Demo mode
        return f"""Demo Analysis Response for {paper_name}:

1. **Core Components**: 
   - DataLoader class
   - Model class
   - Trainer class
   - Evaluator class

2. **Data Processing**: 
   - Load and preprocess input data
   - Apply data augmentation
   - Create train/val/test splits

3. **Model Architecture**: 
   - Define neural network layers
   - Implement forward pass
   - Add regularization techniques

4. **Training Pipeline**: 
   - Set up optimizer and scheduler
   - Implement training loop
   - Add logging and checkpointing

5. **Evaluation Metrics**: 
   - Accuracy, precision, recall
   - Custom metrics as needed

6. **Configuration Parameters**: 
   - Learning rate, batch size
   - Model hyperparameters
   - Training duration

7. **File Dependencies**: 
   - Dataset files
   - Configuration files
   - Utility modules

8. **Implementation Notes**: 
   - Memory optimization
   - GPU utilization
   - Reproducibility considerations

Note: This is a demo response. Set OPENAI_API_KEY for real analysis."""
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return f"Error: {str(e)}. Please check your API key and try again."

# Generate analyzing response
print(f"[INFO] Generating analysis for {paper_name}...")
analyzing_response = generate_response(analyze_msg, model_name, temperature, max_tokens)

# Save analyzing response
os.makedirs(output_dir, exist_ok=True)
with open(f'{output_dir}/analyzing_response.txt', 'w') as f:
    f.write(analyzing_response)

# Print response in a simple format
print("============================================")
print(analyzing_response)
print("============================================\n")

print(f"[INFO] Analysis completed for {paper_name}") 