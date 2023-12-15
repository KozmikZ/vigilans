import bs4
import re
from random import choice
def rndhead()->dict:
    headers_list = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'},
    {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1'},
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'},
    {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14900'}
    ]
    return choice(headers_list)

def clean_paragraphs(paragraphs, threshold=0.5):
    cleaned_paragraphs = []
    for paragraph in paragraphs:
        total_chars = len(paragraph)
        special_chars = len(re.findall('[^a-zA-Z0-9\s]', paragraph))

        # If the percentage of special characters exceeds the threshold, ignore the paragraph
        if total_chars==0:
            continue
        elif special_chars / total_chars > threshold:
            continue

        # Otherwise, remove the special characters and add the cleaned paragraph to the list
        cleaned_paragraph = re.sub('[^a-zA-Z0-9\s]', '', paragraph)
        cleaned_paragraphs.append(cleaned_paragraph)
        
    return cleaned_paragraphs

def clean_soup(soup:bs4.BeautifulSoup): # only returns tags that might have valuable information
    new_soup = bs4.BeautifulSoup('','html.parser')
    info_tags = [
            'h1',        # Heading 1
            'h2',        # Heading 2
            'h3',        # Heading 3
            'h4',        # Heading 4
            'h5',        # Heading 5
            'h6',        # Heading 6
            'p',         # Paragraph
            'a',         # Anchor (links)
            'ul',        # Unordered list
            'ol',        # Ordered list
            'li',        # List item
            'table',     # Table
            'tr',        # Table row
            'td',        # Table data
            'th',        # Table header
            'blockquote',# Blockquote
            'title',     # Page title
            'figure',    # Figure (images, diagrams)
            'figcaption' # Figure caption
            ]
    # unfortunately, we want to keep the structure of the html file
    for tag in soup.find_all():
        if tag in info_tags:
            new_soup.append(bs4.Tag(name=tag.name,attrs=tag.attrs))
    return new_soup



