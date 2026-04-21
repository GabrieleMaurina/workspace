#!/usr/bin/env python3.9


import pypdf
import re
import requests
import sys


URL = 'https://api.zerogpt.com/api/detect/detectText'
HEADERS = headers = {
        'Origin': 'https://zerogpt.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

BIB_WORDS = 'bibliography', 'references', 'citations'
BIB_RE = re.compile(f'({"|".join(BIB_WORDS)})', re.IGNORECASE)


def ai_percent(text):
    response = requests.post(URL, json={'input_text': text}, headers=headers)
    if response.status_code != 200 or not response.json()['success']:
        raise Exception('Failed to get AI percent', response.status_code, response.json())

    return float(response.json()['data']['fakePercentage'])


def read_pdf(path):
    pdf = pypdf.PdfReader(path)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    text = text.replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text


def remove_references(text):
    match = None
    for m in BIB_RE.finditer(text):
        match = m
    if match:
        text = text[:match.start()]
    text = text.strip()
    return text


def main():
    path = sys.argv[1]
    text = read_pdf(path)
    text = remove_references(text)
    print(text)
    score = ai_percent(text)
    print(score)


if __name__ == '__main__':
    main()
