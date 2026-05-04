# Skill Seeker Lab

An AI-powered prototype that suggests what skill you should learn next, based on your goal, field of interest, current challenge, and budget. Built with Streamlit, GPT-4, and the Udemy course API.

## Status

Prototype. Single-file Streamlit app, ~50 lines. Working but rough — see "What's next" below for known gaps.

## What it does

1. You enter four inputs: your learning goal, the field that interests you, the biggest challenge you're facing, and your budget.
2. GPT-4 returns a tailored skill recommendation that respects all four constraints.
3. The Udemy API returns up to three related courses for that field.

## Run it locally

```bash
pip install -r requirements.txt
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml and paste your OpenAI API key.
streamlit run skill_seeker_ai.py
```

The Udemy course endpoint is rate-limited; if course results come back empty, that's usually why.

## Why I built it

Most "what skill should I learn next?" advice is generic — "learn Python," "learn AI." It ignores the user's actual constraints: time, money, and the specific point where they're stuck. I wanted the smallest possible tool that takes those constraints seriously and recommends accordingly.

## What's next

- Multi-source course aggregation (Coursera, YouTube, free resources) instead of Udemy only
- Capture follow-through data so the tool can learn which recommendations actually stick
- A "why this skill, not that one" diff so each recommendation is auditable

## Author

Built by `<your name>`. If you'd like a tailored version of this — for an L&D team, a coaching practice, or a career-services product — reach out: `<your email or LinkedIn>`.
