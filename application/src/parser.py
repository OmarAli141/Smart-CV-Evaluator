from typing import List
import pypdf
import docx

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from all pages of a PDF file."""
    try:    
        with open(file_path, 'rb') as pdf_file_obj:
            pdf_reader = pypdf.PdfReader(pdf_file_obj)
            
            # Initialize an empty list to hold the text from each page.
            text_parts: List[str] = []
            
            # Loop through each page in the PDF.
            for page in pdf_reader.pages:
                # Extract the text from the current page.
                page_text = page.extract_text()
                # Append the extracted text to our list.
                if page_text:
                    text_parts.append(page_text)
            
            # Join all the text parts into a single string.
            full_text = "\n".join(text_parts)
            return full_text
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return ""

def extract_text_from_docx(file_path: str) -> str:
    """Extracts Text From a Signle DOCX File."""
    try:
        doc = docx.Document(file_path)
        full_text = [para.text for para in doc.paragraphs]
        return "\n".join(full_text)
    except Exception as e:
        print(f"An error occurred while reading the DOCX file: {e}")
        return ""

def parse_cv(file_path: str) -> str:
    """
    Parses a CV file (.pdf or .docx) and extracts its text content.

    This function acts as a dispatcher, checking the file extension and
    calling the appropriate helper function to perform the text extraction.

    Args:
        file_path: The full path to the CV file.

    Returns:
        A string containing the extracted text from the document.
        Returns an empty string if the file format is not supported,
        the file is not found, or an error occurs during parsing.
        
    Raises:
        ValueError: If the file extension is not '.pdf' or '.docx'.
        FileNotFoundError: If the file at file_path does not exist.
    """
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Only .pdf and .docx are supported.")
