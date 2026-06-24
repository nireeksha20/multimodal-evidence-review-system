# Multimodal Evidence Review System

## Overview

An AI-assisted claim assessment system designed to analyze damage claims for cars, laptops, and packages using multimodal evidence from customer conversations and images.

The system combines claim text parsing, image validation, user history assessment, and automated decision generation to support evidence-based claim evaluation.

## Features

* Claim text parsing and information extraction
* Image validation and metadata analysis
* User history risk assessment
* Evidence sufficiency evaluation
* Automated claim assessment generation
* Structured output generation for claim processing

## Tech Stack

* Python
* Pandas
* Pillow
* Environment Variables (.env)
* Rule-Based Decision Engine

## Project Structure

```text
code/
├── claim_parser.py
├── image_analyzer.py
├── output_generator.py
├── vision_analyzer.py
├── main.py

dataset/
├── claims.csv
├── user_history.csv
├── evidence_requirements.csv
├── images/
```

## Workflow

1. Parse customer claim conversations.
2. Extract damage details and affected components.
3. Validate supporting images.
4. Analyze historical user information.
5. Evaluate evidence sufficiency.
6. Generate claim assessment results.

## Use Cases

* Insurance claim assessment
* Product damage verification
* Evidence review automation
* Decision support systems

## Project Context

Developed as part of the HackerRank Orchestrate Challenge (June 2026), focusing on multimodal evidence analysis and automated claim review workflows.
