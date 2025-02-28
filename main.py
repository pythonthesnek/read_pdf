import PyPDF2

# Open the PDF file
pdf_file = open('test.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Get the number of pages in the PDF
num_pages = pdf_reader.numPages

# Initialize an empty list to store the words
words = []

# Iterate over each page in the PDF
for page in range(num_pages):
    # Extract the text from the current page
    page_text = pdf_reader.getPage(page).extractText()
    
    # Split the text into individual words
    page_words = page_text.split()
    
    # Add the words to the list
    words.extend(page_words)

# Close the PDF file
pdf_file.close()

# Print the list of words
print(words)