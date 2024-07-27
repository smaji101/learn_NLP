from transformers import pipeline
from difflib import HtmlDiff

#function to extract the text
def extract_translation_text(data):
    # Extract the text from the dictionary
    extracted_text = data[0]['translation_text']
    return extracted_text

#Translates the input text to another language using a model in the Hugging Face transformers library
en_fr_translator = pipeline("translation_en_to_fr")
input_text = "She bought the red lipstick from the beauty store"
fr_txt = extract_translation_text(en_fr_translator(input_text))


#Translates the input text to that same language again using a different transformers model
model_c = "Helsinki-NLP/opus-mt-fr-en"
translator = pipeline("translation", model=model_c)

en_txt = extract_translation_text(translator(fr_txt))

print("Input text :: " + input_text)
print("French translation :: " + fr_txt)
print("English translation :: " + en_txt)

#Outputs to a file the difference between the two translated texts (e.g. using Python's difflib)
d = HtmlDiff()
html_diff = d.make_file(input_text.splitlines(), str(en_txt).splitlines())
with open("diff.html", "w", encoding="utf-8") as f:
    f.write(html_diff)
