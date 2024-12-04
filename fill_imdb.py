import pandas as pd
import random

# Enhanced OCR error types
ocr_variations = {
    # Letter Substitutions
    'a': ['@', '4', 'A', 'α', 'λ', 'д'],
    'b': ['6', 'B', 'β', '8', 'Ь'],
    'c': ['C', '(', '©', 'с'],
    'd': ['D', 'Ь', 'ð', 'cl'],
    'e': ['3', 'E', 'ε', '€', 'є'],
    'f': ['F', 'ƒ', 'Ғ'],
    'g': ['G', '9', 'ǥ', 'б'],
    'h': ['H', '#', 'Ң', 'һ'],
    'i': ['1', '!', 'I', '|', 'ί', 'ı'],
    'j': ['J', 'ј', 'ʝ'],
    'k': ['K', 'Κ', 'к'],
    'l': ['1', 'L', '|', 'І'],
    'm': ['M', 'Μ', 'м'],
    'n': ['N', 'η', 'п'],
    'o': ['0', 'O', 'θ', 'σ', 'о'],
    'p': ['P', 'Р', 'р'],
    'q': ['Q', 'φ', 'գ'],
    'r': ['R', 'г', 'Я'],
    's': ['5', 'S', '$', 'δ', 'ѕ'],
    't': ['7', 'T', '+', 'τ'],
    'u': ['U', 'μ', 'υ'],
    'v': ['V', 'ν', 'ѵ'],
    'w': ['W', 'ω', 'ш'],
    'x': ['X', '×', 'х'],
    'y': ['Y', 'γ', 'у'],
    'z': ['Z', '2', 'ζ'],
    
    # Space and Punctuation
    ' ': ['_', '-', '.', '', '  '],
    '.': [',', ' ', '·'],
    '-': ['_', ' ', ''],
    
    # Numbers
    '0': ['O', 'o', 'Q'],
    '1': ['l', 'I', '|'],
    '2': ['Z', 'z'],
    '5': ['S', 's'],
    '8': ['B', 'b'],
}

def generate_ocr_variation(title):
    errors = [
        'substitution',    # Replace character with similar looking one
        'deletion',        # Remove character
        'insertion',       # Add extra character
        'transposition',   # Swap adjacent characters
        'spacing',         # Add/remove/modify spaces
        'casing',         # Change case
        'duplication',    # Duplicate characters
        'noise'           # Add random noise characters
    ]
    
    new_title = title
    num_errors = random.randint(1, 3)  # Apply 1-3 random errors
    
    for _ in range(num_errors):
        error_type = random.choice(errors)
        
        if error_type == 'substitution':
            if len(new_title) > 0:
                pos = random.randint(0, len(new_title)-1)
                char = new_title[pos].lower()
                if char in ocr_variations:
                    new_title = new_title[:pos] + random.choice(ocr_variations[char]) + new_title[pos+1:]
        
        elif error_type == 'deletion':
            if len(new_title) > 3:
                pos = random.randint(0, len(new_title)-1)
                new_title = new_title[:pos] + new_title[pos+1:]
        
        elif error_type == 'insertion':
            pos = random.randint(0, len(new_title))
            new_title = new_title[:pos] + random.choice('abcdefghijklmnopqrstuvwxyz0123456789') + new_title[pos:]
        
        elif error_type == 'transposition':
            if len(new_title) > 1:
                pos = random.randint(0, len(new_title)-2)
                new_title = new_title[:pos] + new_title[pos+1] + new_title[pos] + new_title[pos+2:]
        
        elif error_type == 'spacing':
            if ' ' in new_title:
                new_title = new_title.replace(' ', random.choice(['_', '-', '', '  ']))
        
        elif error_type == 'casing':
            new_title = ''.join(c.swapcase() if random.random() < 0.3 else c for c in new_title)
        
        elif error_type == 'duplication':
            if len(new_title) > 0:
                pos = random.randint(0, len(new_title)-1)
                new_title = new_title[:pos] + new_title[pos] * 2 + new_title[pos+1:]
        
        elif error_type == 'noise':
            noise_chars = ['#', '@', '*', '&', '%', '$']
            pos = random.randint(0, len(new_title))
            new_title = new_title[:pos] + random.choice(noise_chars) + new_title[pos:]
    
    return new_title

def main():
    # Load the filtered movies TSV file
    data = pd.read_csv('filtered_movies.tsv', sep='\t', header=None, dtype=str)
    titles = data[2].dropna().tolist()
    
    # Generate OCR variations
    num_variants = 5  # Number of variants to generate per title
    dataset = []
    
    for title in titles:
        for _ in range(num_variants):
            ocr_variant = generate_ocr_variation(title)
            dataset.append({
                'ocr_generated_title': ocr_variant,
                'original_title': title
            })
    
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(dataset)
    df.to_csv('imdb_title_ocr_variations.csv', index=False)
    print(f"OCR variations dataset saved to 'imdb_title_ocr_variations.csv', with {num_variants} variants per title, total {len(df)} rows")

if __name__ == "__main__":
    main()