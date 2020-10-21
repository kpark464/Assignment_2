# Project Reflection

## Project Overview

[Maximum 100 words] What data source(s) did you use and what technique(s) did you use analyze/process them? What did you hope to learn/create?

This project aims to analyze texts from Carl Jung's and Freud's psychology papers. The team used Gutenberg Project to extract two books: Freud's "Dream Psychology" and Jung's "Collected Papers on Psychology." These two sources are used in the text analysis for frequency and finding the total of meaningful words. Additionally, the team extraded data from Wikipedia article page of "Psychology" to condust similarity anlysis with cosine approach among data sources. The team hope to learn data scientist approach of analyzinig texts from an online source and interpreting the result to create insights. Furthermore, the team hope to create visual representatives of the data that is easy to comprehend. 

## Implementation

[~2-3 paragraphs] Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.
  
Step 1: we extracted data from Gutenberg and saved it as local files for further processing 
Step 2: We processed the raw data by filtering out meaningless words first. Afterwards, we computed the total number of words included in each book and the total number of non-repetitive words.
Step 3: Comparing only word frequencies cannot give us an objective conclusion of paper similarities between Freud and Jung, since the 
We decided to test text similarity through cosine method rather than comparing the number text 

## Results

[~2-3 paragraphs + figures/examples] Present what you accomplished:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

Cosine: similarity of words
compared to wiki
Freud is compared to Jung's and wikipedia psychology

## Reflection

 [~1 paragraph] From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by task, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

The team had bi-daily meetings to work on the project. Each membr of the team read the assignment instructions before the meeting and 