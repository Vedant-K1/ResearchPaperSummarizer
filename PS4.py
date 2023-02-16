import PyPDF2
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from gensim.summarization.summarizer import summarize


def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file and returns a string containing the text.
    """
    pdf_file = open(file_path, 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    text = ''
    for i in range(number_of_pages):
        page = read_pdf.getPage(i)
        text += page.extractText()
    pdf_file.close()
    return text


def clean_text(text):
    """
    Cleans the input text by removing special characters and stop words.
    """
    # Remove special characters and digits
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)

    # Tokenize the text
    tokens = sent_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    clean_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Join the clean tokens back into a string
    clean_text = ' '.join(clean_tokens)

    return clean_text


def summarize_text(text, summary_ratio=0.2):
    """
    Uses Gensim's summarizer to create a summary of the input text.
    """
    summary = summarize(text, ratio=summary_ratio)
    return summary


if __name__ == '__main__':
    # Input file path and output file path
    input_file_path = 'Data/PS3.pdf'
    output_file_path = 'Data/summary.txt'

    # Extract text from PDF file
    text = extract_text_from_pdf(input_file_path)

    # Clean the text
    clean_text = clean_text(text)

    # Summarize the text
    summary = summarize_text(clean_text)

    # Save the summary to a file
    with open(output_file_path, 'w') as f:
        f.write(summary)
