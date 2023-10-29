import sys
from transformers import BartForConditionalGeneration, BartTokenizer

def summarize_transcription(text):
    """
    Summarize the given transcription using BART model.

    Parameters:
    - text: str, the transcription text to summarize

    Returns:
    - str, the summarized text
    """
    
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=30, max_length=250, length_penalty=2.0)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarize_transcription.py [path_to_transcription_file]")
        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        transcription = file.read()

    summarized_text = summarize_transcription(transcription)
    # print("Original Transcription:")
    # print(transcription)
    # print("\nSummarized Text:")
    # print(summarized_text)

