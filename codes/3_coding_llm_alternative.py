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
parser.add_argument('--output_repo_dir',type=str, default="")

args = parser.parse_args()

paper_name = args.paper_name
paper_format = args.paper_format
pdf_json_path = args.pdf_json_path
pdf_latex_path = args.pdf_latex_path
output_dir = args.output_dir
output_repo_dir = args.output_repo_dir

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

code_msg = [
    {'role': "system", "content": f"""You are an expert software engineer and machine learning practitioner with extensive experience in implementing research papers.
You will receive a research paper in {paper_format} format. 
Your task is to generate complete, production-ready Python code that implements the methodology described in the paper.

Your response should include:

1. **Complete Python Implementation**: Full code with all necessary imports, classes, and functions
2. **Configuration Files**: YAML or JSON config files for parameters
3. **Requirements File**: requirements.txt with all dependencies
4. **README**: Documentation explaining how to use the implementation
5. **Example Usage**: Sample code showing how to run the implementation
6. **File Structure**: Organized code with proper separation of concerns

The code should be:
- Well-documented with clear comments
- Modular and reusable
- Following Python best practices
- Ready to run with minimal setup
- Include error handling and logging

Please provide complete, executable code that can be directly used to reproduce the paper's results."""},
    {'role': "user", "content": f"Please implement the methodology described in the following research paper:\n\n{paper_content}"}
]

def generate_response(messages, model_name="gpt-3.5-turbo", temperature=1.0, max_tokens=4000):
    """Generate response using OpenAI API or fallback to demo mode"""
    
    if client is None:
        # Demo mode
        return f"""# Demo Implementation for {paper_name}

## main.py
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import numpy as np
import yaml
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DemoModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DemoModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def train_model(model, train_loader, optimizer, criterion, epochs):
    model.train()
    for epoch in range(epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            if batch_idx % 100 == 0:
                logger.info(f'Epoch: {{epoch}}, Batch: {{batch_idx}}, Loss: {{loss.item():.4f}}')

def main():
    # Load configuration
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    # Initialize model
    model = DemoModel(
        input_size=config['input_size'],
        hidden_size=config['hidden_size'],
        output_size=config['output_size']
    )
    
    # Setup training
    optimizer = optim.Adam(model.parameters(), lr=config['learning_rate'])
    criterion = nn.CrossEntropyLoss()
    
    # Training loop (demo)
    logger.info("Starting training...")
    # train_model(model, train_loader, optimizer, criterion, config['epochs'])
    logger.info("Training completed!")

if __name__ == "__main__":
    main()
```

## config.yaml
```yaml
# Model configuration
input_size: 784
hidden_size: 128
output_size: 10

# Training configuration
learning_rate: 0.001
batch_size: 32
epochs: 10

# Data configuration
data_path: "./data"
```

## requirements.txt
```
torch>=1.9.0
numpy>=1.21.0
pyyaml>=5.4.0
```

## README.md
```markdown
# {paper_name} Implementation

This is a demo implementation of the {paper_name} paper.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Configuration
Edit `config.yaml` to modify model parameters and training settings.
```

Note: This is a demo response. Set OPENAI_API_KEY for real implementation."""
    
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

# Generate coding response
print(f"[INFO] Generating code for {paper_name}...")
coding_response = generate_response(code_msg, model_name, temperature, max_tokens)

# Save coding response
os.makedirs(output_dir, exist_ok=True)
with open(f'{output_dir}/coding_response.txt', 'w') as f:
    f.write(coding_response)

# Print response in a simple format
print("============================================")
print(coding_response)
print("============================================\n")

print(f"[INFO] Code generation completed for {paper_name}")

# Create demo repository structure
if output_repo_dir:
    os.makedirs(output_repo_dir, exist_ok=True)
    
    # Create demo files
    demo_files = {
        'main.py': '''import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import yaml
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DemoModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DemoModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def main():
    logger.info("Demo implementation of {} paper".format("{}"))
    logger.info("This is a placeholder implementation")
    logger.info("Set OPENAI_API_KEY for real code generation")

if __name__ == "__main__":
    main()
'''.format(paper_name, paper_name),
        
        'config.yaml': '''# Demo configuration for {}
model:
  input_size: 784
  hidden_size: 128
  output_size: 10

training:
  learning_rate: 0.001
  batch_size: 32
  epochs: 10

data:
  data_path: "./data"
'''.format(paper_name),
        
        'requirements.txt': '''torch>=1.9.0
numpy>=1.21.0
pyyaml>=5.4.0
''',
        
        'README.md': '''# {} Implementation

This is a demo implementation of the {} paper.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Configuration
Edit `config.yaml` to modify model parameters and training settings.

## Note
This is a demo implementation. Set OPENAI_API_KEY environment variable for real code generation.
'''.format(paper_name, paper_name)
    }
    
    for filename, content in demo_files.items():
        with open(os.path.join(output_repo_dir, filename), 'w') as f:
            f.write(content)
    
    print(f"[INFO] Demo repository created at {output_repo_dir}") 