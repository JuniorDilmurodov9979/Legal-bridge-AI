import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from ai_engine.ocr import OCRProcessor
from ai_engine.parser import ContractParser

path = 'shartnomalar/Договор (НК)_ 10 от 01.04.2025  (1).pdf'

if __name__ == '__main__':
    text, conf, scanned = OCRProcessor().extract_text_from_file(path)
    print('OCR ok. scanned=', scanned, 'conf=', conf)

    parser = ContractParser()
    sections, meta = parser.parse(text)

    print('party_a_inn:', meta.party_a_inn)
    print('party_b_inn:', meta.party_b_inn)
    print('party_a_name:', meta.party_a_name)
    print('party_b_name:', meta.party_b_name)
    print('amount:', meta.total_amount, meta.currency)
    print('language:', meta.language)
