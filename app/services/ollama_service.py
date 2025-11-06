import ollama

def generate_phrase(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1", messages=[{
        "role": "user",
        "content": f"generate a simple, very short sentence using this word: {translated_word}. return your response in the target language-code: {target_language}"
    }])
    
    return {
        "response": response["message"]["content"]
    }