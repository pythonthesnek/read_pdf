import PyPDF2


pdf_file = open('your_pdf_here.pdf', 'rb') # make sure you copy the name of your pdf correctly and don't remove the .pdf part
pdf_reader = PyPDF2.PdfReader(pdf_file) # Create a PDF reader object

num_pages = len(pdf_reader.pages) # Get the number of pages

words = set() # Create a set to store the words

# Loop through each page and extract the text
for page in pdf_reader.pages:
    page_text = page.extract_text()
    page_words = page_text.split()
    words.update(page_words) 

pdf_file.close()

print(words)
