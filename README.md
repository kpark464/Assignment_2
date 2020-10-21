## Text Analysis of Jung and Freud's Psychology Paper

# Summary
This project aims to analyze texts from Carl Jung's and Freud's psychology papers to find similarities in two different arguments regarding the unconscious mind. 
The team used the Gutenberg Project to extract two books: Freud's "Dream Psychology" and Jung's "Collected Papers on Psychology."
The team later compares the similarity between these two texts with Wikipedia page "Psychology."

# Prerequisites
To run the program, make sure:
* You have installed matplotlib, numpy, pandas, pillow, and wordcloud packages for .
* You have installed scikit-learn for running cosine similarity
* The Freud text is found here: http://www.gutenberg.org/ebooks/15489.txt.utf-8
* The Jung text is found here: http://www.gutenberg.org/files/48225/48225-0.txt
* Files are adjusted to be located under your CPU

Note: To install packages, write "pip install xyz" in the command prompt before running the code. 

# Steps
1. Run "create_local_file-jung.py" and "create_local_file_freud.py" 
2. Run analytics for each ("freud_data_analysis.py" and "jungs-data-analysis.py")
3. Run wordcloud for each files ("word_cloud_freud.py" and "word_cloud_jung.py")
4. Run "cos_similarity.py"
5. Reflection
