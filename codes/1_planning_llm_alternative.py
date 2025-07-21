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

plan_msg = [
    {'role': "system", "content": f"""You are an expert researcher and strategic planner with a deep understanding of experimental design and reproducibility in scientific research.
You will receive a research paper in {paper_format} format. 
Your task is to create a detailed and efficient plan to reproduce the experiments and methodologies described in the paper.

Your response should be structured as follows:

1. **Project Overview**: Brief summary of the paper's main contributions and objectives
2. **Technical Requirements**: List of software, libraries, and hardware requirements
3. **Implementation Plan**: Step-by-step breakdown of the implementation process
4. **File Structure**: Proposed directory structure for the code repository
5. **Dependencies**: Required Python packages and their versions
6. **Configuration**: Key parameters and settings that need to be configurable
7. **Testing Strategy**: How to validate the implementation
8. **Timeline**: Estimated time for each implementation phase

Please provide a comprehensive and actionable plan that can be used to implement the paper's methodology."""},
    {'role': "user", "content": f"Please analyze the following research paper and create a detailed implementation plan:\n\n{paper_content}"}
]

def generate_response(messages, model_name="gpt-3.5-turbo", temperature=1.0, max_tokens=4000):
    """Generate response using OpenAI API or fallback to demo mode"""
    
    if client is None:
        # Demo mode
        return f"""Demo Response for {paper_name}:

1. **Project Overview**: This is a demo response for the paper analysis.
2. **Technical Requirements**: Python 3.8+, basic ML libraries
3. **Implementation Plan**: 
   - Phase 1: Data preprocessing
   - Phase 2: Model implementation
   - Phase 3: Training and evaluation
4. **File Structure**: 
   - src/
   - data/
   - config/
   - tests/
5. **Dependencies**: numpy, torch, transformers
6. **Configuration**: config.yaml for parameters
7. **Testing Strategy**: Unit tests and integration tests
8. **Timeline**: 2-3 weeks for complete implementation

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

# Generate planning response
print(f"[INFO] Generating planning for {paper_name}...")
planning_response = generate_response(plan_msg, model_name, temperature, max_tokens)

# Save planning response
os.makedirs(output_dir, exist_ok=True)
with open(f'{output_dir}/planning_response.txt', 'w') as f:
    f.write(planning_response)

# Print response in a simple format
print("============================================")
print(planning_response)
print("============================================\n")

print(f"[INFO] Planning completed for {paper_name}") 