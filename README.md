# Text-Justification

# Text-Justification

Implemented an automated justification program (in C/C++/Java/Python/Go)
which can reformat a text document by justifying (i.e., both left alignment and right
alignment) the document to a different width for printing/displaying (e.g., adjust
margins of the same size paper, change orientation of paper between portrait and
landscape, change paper size, etc.) To make your task easier, assume all characters
(letters, digits, punctuations, spaces, etc.) have the same size. In order to justify,
I used multiple spaces roughly evenly between words. However, too many
spaces between words make the document unpleasant to read, so I need to split
the word with hyphens at line breaks.

Example Input:
40
Your program should scan the input pre-justified
text and divide it into words, merge splittingwords
(by removing hyphens or “\n”) and reformat
to different width with justification and splitting.

Example Output:
Your program should scan the input pre-
justified  text and divide into  words,
merge  splitting-words (by removing hy-
phens or “\n”) and reformat to different
width with justification and splitting.
