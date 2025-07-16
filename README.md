LLM Fine-Tuning for Verilog Code Generation
Overview

This project fine-tunes a quantized LLaMA 3B large language model to generate Verilog HDL code from natural language prompts. The model is trained on a custom dataset of Verilog modules and FSM templates using QLoRA and parameter-efficient fine-tuning techniques.
Features

    Fine-tunes an 8-bit quantized LLaMA 3B model with LoRA adapters using QLoRA.

    Curated a dataset of Verilog modules and FSM/ASM templates formatted for instruction tuning.

    Uses HuggingFace’s SFTTrainer for efficient supervised fine-tuning with constrained GPU memory.

    Generates synthesizable Verilog RTL code based on text prompts.
