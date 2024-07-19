import csv

def clean_csv(file_path, output_path):
    cleaned_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Add your cleaning logic here
            # For example, you can remove or fix rows with issues
            if row.count('"') % 2 == 0:  # Ensure even number of quotes
                cleaned_data.append(row)
            else:
                # Fix or skip problematic row
                pass

    # Write cleaned data to a new file
    with open(output_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_data)

clean_csv('intents.csv', 'intents_cleaned.csv')
