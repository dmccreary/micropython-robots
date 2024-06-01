def extract_terms_with_definitions(file_path):
    with open(file_path, 'r') as file:
        file_lines = file.readlines()

    terms_dict = {}
    current_term = ""
    for line in file_lines:
        if line.startswith('#### '):  # New term
            current_term = line.strip('#### ').strip()
            terms_dict[current_term] = []  # Initialize the list for the term's definition
        elif current_term:  # If we are within a term's definition
            terms_dict[current_term].append(line)
    return terms_dict

def sort_and_write_glossary(input_file_path, output_file_path):
    terms_with_definitions = extract_terms_with_definitions(input_file_path)

    sorted_terms = sorted(terms_with_definitions.keys())

    with open(output_file_path, 'w') as sorted_file:
        for term in sorted_terms:
            sorted_file.write('#### ' + term + '\n')  # Writing the term
            sorted_file.writelines(terms_with_definitions[term])  # Writing the definition

# Path to the input file
input_file_path = '../../docs/glossary.md'

# Path to the output file
output_file_path = 'glossary-sorted.md'

# Sorting the glossary and writing to a new file
sort_and_write_glossary(input_file_path, output_file_path)
