import ollama

def generate_phrase(translated_word: str, target_language):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"only generate a simple, very short sentence using this word: {translated_word}. return your response in the target language-code: {target_language}. do not generate any extra lines whatsoever"
    }])
    
    return {
        "response": response["message"]["content"]
    }

def generate_feedback(json_result: str):
    response = ollama.chat(model="llama3.1:8b", messages=[{
        "role": "user",
        "content": f"generate targeted feedback for a user of a language learning app using the following json result for the user's attempt at pronunciation of a word or phrase. the feedback should be short and to the point. do not include a response to this prompt in your response or reference any particular technical details such as offsets, your full response will be displayed to the user in the app: {json_result}"
    }])
    
    return response["message"]["content"]
