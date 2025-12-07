#!/bin/bash
echo "=========================================="
echo "   Setting up Tensor-Yield Environment"
echo "=========================================="

# Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Register Kernel for Jupyter
python -m ipykernel install --user --name=tensor-yield --display-name "Python (Tensor-Yield)"

echo "------------------------------------------"
echo "Setup Complete. Activate with: source venv/bin/activate"
echo "Then run: jupyter notebook"
echo "=========================================="
