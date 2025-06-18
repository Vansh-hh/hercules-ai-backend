# Hercules AI Titan Ultra Edition - Backend

This backend powers the ultra AI features like GPT-4, memory, voice, and OCR for Hercules AI.

## Endpoints

- `/gpt4`: Ask anything to GPT-4
- `/ocr`: Extract text from uploaded image

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```