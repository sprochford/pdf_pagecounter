import PyPDF2
import os
import csv

def count_pages_in_directory(directory_path):
    """Counts the pages in all PDF files within a given directory, logs errors, and outputs results to a CSV file in the directory.

    Args:
        directory_path (str): The path to the directory containing PDFs.

    Returns:
        None
    """

    # Create the CSV file path
    csv_file_path = os.path.join(directory_path, 'pdf_page_counts.csv')

    # Open the CSV file and write the header row
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Filename', 'Page Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Initialize counters for total pages and PDFs
        total_pages = 0
        total_pdfs = 0

        # Iterate through each file in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".pdf"):
                # Increment the total PDF count
                total_pdfs += 1

                # Construct the full path to the PDF file
                pdf_path = os.path.join(directory_path, filename)

                try:
                    # Open the PDF file in binary read mode
                    with open(pdf_path, 'rb') as file:
                        # Create a PDF reader object
                        pdf_reader = PyPDF2.PdfReader(file)
                        # Get the number of pages in the PDF
                        page_count = len(pdf_reader.pages)

                        # Add the page count to the total
                        total_pages += page_count

                        # Write the filename and page count to the CSV file
                        writer.writerow({'Filename': filename, 'Page Count': page_count})

                        # Print a message to the console
                        print(f"{filename} has {page_count} pages.")

                except PyPDF2.errors.PdfReadError as e:
                    # Handle PDF reading errors
                    print(f"Error reading {filename}: {str(e)}")
                except Exception as e:
                    # Handle unexpected errors
                    print(f"Unexpected error processing {filename}: {str(e)}")

        # Add rows for total PDFs and total pages to the CSV file
        writer.writerow({'Filename': 'Total PDFs', 'Page Count': total_pdfs})
        writer.writerow({'Filename': 'Total Pages', 'Page Count': total_pages})

        # Print the total counts to the console
        print(f"Total PDFs processed: {total_pdfs}")
        print(f"Total pages in all PDFs: {total_pages}")

# Replace with your actual directory path
directory_path = "/Volumes/DLC13/Backup_Projects/2024_11_WWII/ErikaMilam-EThomas_MargaretFitzellTifftGilliard"

count_pages_in_directory(directory_path)