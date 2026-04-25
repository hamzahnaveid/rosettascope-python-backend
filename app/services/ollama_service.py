import ollama

def generate_beginner_term(translated_word: str, target_language):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "system",
                "content": """
You output only the requested phrase.
Never explain anything.
Never add notes.
Never add labels.
Never add quotation marks.
Never add punctuation.
Never add extra text before or after the phrase.
"""
            },
            {
                "role": "user",
                "content": f"""
Language code: {target_language}

Required word:
{translated_word}

Create ONE useful beginner-level phrase.

Rules:
- Maximum 2 words
- Minimum 1 word
- Must include "{translated_word}" exactly
- Prefer adjective + noun, article + noun, possessive + noun, or simple modifier + word
- If the given word is already best alone, return only the word
- Natural everyday language
- Not a full sentence
- No punctuation
- Output only the phrase

Examples:
big house
my book
red apple
"""
            }
        ],
        options={
            "temperature": 0.3,
            "num_predict": 6,
            "stop": ["\n", ".", ":"]
        }
    )

    return response["message"]["content"].strip().split("\n")[0]
    

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

def generate_challenge_hints(words: list[str]):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
            "content": f"""
You generate scavenger hunt hints for a mobile app.

The player must find real-world objects using their camera.
You are given 5 target words. Each word is the name of a physical object.

Your task:
Create one hint per word that helps the user find the object
by describing how it looks, where it is usually found, or how it is used.

Rules:
- Exactly 5 hints (one per word)
- Do NOT include the word itself or obvious synonyms
- Make hints visual and environment-based (what it looks like, where it is)
- Keep each hint under 18 words
- Make hints moderately challenging (not too obvious, not too vague)

Output format (STRICT):
- Use bullet points
- Each line must start with "- "
- Exactly 5 lines
- No numbering
- No extra text before or after the list
- No blank lines

Example:
- A flat surface where people eat or work, often surrounded by chairs
- Keeps your drinks cold and is usually found in the kitchen
- Something you open to enter a room

Words:
{words}
"""
    }])
    
    return response["message"]["content"]

def generate_fluff(listening_text: str, target_language: str, level: str):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
You are generating distractor words for a Duolingo-style listening exercise.

The learner hears audio of a sentence.
The correct chip words come from the sentence text below.

Your task is to generate ONLY extra incorrect chip words.

INPUTS:
- listening_text: {listening_text}
- target_language: {target_language}
- level: {level}

INSTRUCTIONS:
1. Extract the correct words from listening_text mentally, but DO NOT output them.
2. Generate 5 incorrect distractor words in {target_language}.
3. Do NOT include any exact word already found in listening_text.
4. Use vocabulary suitable for {level} learners.
5. Prefer distractors that are:
   - common words
   - similar sounding to words in listening_text
   - same word type
   - plausible in context
6. Avoid duplicates.
7. Return ONLY a Python list of strings.
"""
    }])
    
    return response["message"]["content"]
