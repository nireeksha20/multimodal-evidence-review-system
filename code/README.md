# HackerRank Orchestrate June 2026

## Overview

This solution processes damage claims for cars, laptops, and packages using:

- Claim text parsing
- Image validation
- User history risk assessment
- Rule-based output generation

## Setup

Install dependencies:

pip install pandas pillow python-dotenv

## Run

Navigate to the code directory:

python main.py

## Output

The script generates output.csv in the project root directory.

## Components

- claim_parser.py – extracts issue type and object part from claim conversations
- image_analyzer.py – validates images and extracts image metadata
- output_generator.py – generates final claim assessment rows
- evaluation/evaluation_report.md – evaluation and operational analysis

## Dataset

Uses:

- claims.csv
- user_history.csv
- evidence_requirements.csv
- local image files

## Output Schema

Matches the schema defined in the HackerRank Orchestrate problem statement.
