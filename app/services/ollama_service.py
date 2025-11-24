import ollama

def generate_phrase(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"only generate a simple, very short sentence using this word: {translated_word} and its translation in english. return your response in the target language-code: {target_language}. do not generate any extra lines except only for the translation of the sentence in english whatsoever"
    }])
    
    return {
        "response": response["message"]["content"]
    }