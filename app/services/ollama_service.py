import ollama

def generate_phrase(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
Generate a SHORT PHRASE for a language learning app.

Rules:
- The phrase MUST include this word: {translated_word}
- 2–4 words only
- It must NOT be a full sentence
- Do NOT include a subject + verb structure
- Do NOT use punctuation
- Output ONLY the phrase
- Language code: {target_language}

Return only the phrase text.
"""
    }])
    
    return {
        "response": response["message"]["content"]
    }

def generate_sentence(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"""
Generate a SHORT SENTENCE for a language learning app.

Rules:
- The sentence MUST include this word: {translated_word}
- 5–12 words
- Must be a complete sentence with a verb
- End with proper punctuation
- Output ONLY the sentence
- Language code: {target_language}

Return only the sentence text.
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

Strict rules:
- Output ONLY the feedback text shown to the user.
- Do NOT mention JSON, prompts, analysis, scores, offsets, or technical details.
- Do NOT explain what you are doing.
- No headings, labels, bullet points, or filler text.
- Maximum 2–3 sentences.

Feedback guidelines:
- Focus on the most noticeable pronunciation issues.
- If word-level scores exist, mention the specific word(s) that need improvement.
- If syllable-level scores exist, give targeted advice about the problematic syllable sounds.
- Prioritize the lowest scoring words or syllables.
- If pronunciation is mostly correct, briefly acknowledge it and suggest a small improvement.

User pronunciation analysis:
{json_result}

Return ONLY the feedback text.
"""
    }])
    
    return response["message"]["content"]
