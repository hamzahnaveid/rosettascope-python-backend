import ollama

def generate_phrase(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
You generate short practice phrases for a language learning app.

Word that MUST appear in the phrase:
{translated_word}

Language code:
{target_language}

Phrase rules:
- 2 to 4 words total
- MUST include the given word exactly
- Not a full sentence
- Do NOT use a subject + verb structure
- No punctuation

Forbidden:
- Explanations
- Notes
- Labels
- Quotes
- Extra text before or after

Output format:
Return ONLY the phrase text.

Example format:
green apple tree

Now generate the phrase.
"""
    }])
    
    return {
        "response": response["message"]["content"]
    }

def generate_sentence(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
You generate short practice sentences for a language learning app.

Word that MUST appear in the sentence:
{translated_word}

Language code:
{target_language}

Sentence rules:
- 5 to 12 words
- Must be a complete sentence
- Must contain a verb
- Must include the given word exactly
- End with proper punctuation

Forbidden:
- Explanations
- Notes
- Labels
- Quotes
- Any extra text

Output format:
Return ONLY the sentence.

Example format:
The cat sleeps on the warm chair.

Now generate the sentence.
"""
    }])
    
    return {
        "response": response["message"]["content"]
    }

def generate_feedback(json_result: str):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
You generate pronunciation feedback for a language learning app.

First analyze the pronunciation results internally:
1. Identify the lowest scoring word or syllable.
2. Determine the main pronunciation difficulty.
3. Choose one clear improvement tip.

Then write concise feedback for the learner.

Feedback rules:
- 20 to 40 words
- Maximum 2 sentences
- Focus on the most noticeable pronunciation issue
- Mention the specific word or syllable if helpful
- If pronunciation is mostly correct (score of 90+), acknowledge progress and suggest a small improvement

Forbidden:
- JSON references
- Scores
- Offsets
- Technical analysis
- Explanations of what you are doing
- Headings or bullet points
- Labels such as "Feedback:"

Pronunciation analysis data:
{json_result}

Output format:
Return ONLY the feedback text.
"""
    }])
    
    return response["message"]["content"]

def generate_feedback_aggregate(json_result: str):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
You generate detailed pronunciation feedback for a language learning app.

The learner has practiced the same word multiple times. You are given feedback
from previous attempts. Your task is to identify pronunciation patterns and
give clear guidance that will help the learner improve.

Internal process:
1. Look for pronunciation issues that appear repeatedly.
2. Identify the sound, syllable, or word that causes the most difficulty.
3. Determine what change in articulation would improve pronunciation.
4. Give practical advice the learner can apply when practicing again.

Feedback rules:
- 40 to 80 words
- 3 to 4 sentences
- Focus on the most consistent pronunciation issue
- Mention the relevant sound, syllable, or word when useful
- Provide at least one practical tip for improving pronunciation
- If pronunciation has improved over attempts, briefly acknowledge progress

Tone:
Supportive, clear, and encouraging.

Forbidden:
- Mentioning attempts or previous feedback
- JSON references
- Scores or analysis
- Technical or system explanations
- Headings, bullet points, or labels

User pronunciation feedback data:
{json_result}

Output format:
Return ONLY the feedback text.
"""
    }])
    
    return response["message"]["content"]

