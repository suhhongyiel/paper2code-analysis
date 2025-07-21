#!/bin/bash

MODEL_NAME="gpt-3.5-turbo"
PAPER_NAME="Transformer"
PDF_PATH="../examples/Transformer.pdf" # .pdf
PDF_JSON_PATH="../examples/Transformer.json" # .json
PDF_JSON_CLEANED_PATH="../examples/Transformer_cleaned.json" # _cleaned.json
OUTPUT_DIR="../outputs/Transformer_alternative"
OUTPUT_REPO_DIR="../outputs/Transformer_alternative_repo"

mkdir -p $OUTPUT_DIR
mkdir -p $OUTPUT_REPO_DIR

echo $PAPER_NAME

echo "------- Preprocess -------"

python ../codes/0_pdf_process.py \
    --input_json_path ${PDF_JSON_PATH} \
    --output_json_path ${PDF_JSON_CLEANED_PATH} \

echo "------- PaperCoder (Alternative) -------"

echo "Running planning stage..."
python ../codes/1_planning_llm_alternative.py \
    --paper_name $PAPER_NAME \
    --model_name ${MODEL_NAME} \
    --pdf_json_path ${PDF_JSON_CLEANED_PATH} \
    --output_dir ${OUTPUT_DIR}

echo "Running analysis stage..."
python ../codes/2_analyzing_llm_alternative.py \
    --paper_name $PAPER_NAME \
    --model_name ${MODEL_NAME} \
    --pdf_json_path ${PDF_JSON_CLEANED_PATH} \
    --output_dir ${OUTPUT_DIR}

echo "Running coding stage..."
python ../codes/3_coding_llm_alternative.py  \
    --paper_name $PAPER_NAME \
    --model_name ${MODEL_NAME} \
    --pdf_json_path ${PDF_JSON_CLEANED_PATH} \
    --output_dir ${OUTPUT_DIR} \
    --output_repo_dir ${OUTPUT_REPO_DIR} \

echo "------- Alternative PaperCoder Completed -------"
echo "Output directory: ${OUTPUT_DIR}"
echo "Repository directory: ${OUTPUT_REPO_DIR}"
echo ""
echo "Note: This is a demo implementation using OpenAI API."
echo "Set OPENAI_API_KEY environment variable for real analysis." 