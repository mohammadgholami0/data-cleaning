Cleaning & Fixing Concert Tour Data
The Goal
I found this dataset of top-grossing concert tours, but it was a mess. It had Wikipedia footnotes (like [1]), weird symbols (†), and currency that Excel couldn't actually read. I wanted to clean it up so I could actually see which artists made the most money per show.

What was wrong with the data?
When I first opened this.csv, I couldn't do any math with it because:

Numbers weren't numbers: Every money value had a $ and commas, so Excel/Python saw them as "text."

Footnote Junk: There were brackets everywhere (e.g., 7[2]). I had to strip those out to get the actual rank.

Date ranges: "2023-2024" is hard to sort. I needed just the start year to put the tours in order.

How I fixed it
Instead of deleting things one-by-one (which takes forever), I used a Python script to do the "heavy lifting":

Regex Cleaning: I used a "Regular Expression" to tell the computer: "Find anything inside brackets and delete it." That fixed the names and ranks instantly.

Money Conversion: I stripped out the $ and , and told the computer to treat those columns as "Floats" (numbers).

Splitting Years: I pulled the first four characters from the year column so I could have a clean Start_Year column.

What’s in this Repo?
this.csv: This is the original, messy data I started with.

clean_data.py: The script I wrote to automate the cleanup.

structured_tour_data.csv: The final, perfect version of the data.

Final_Analysis.xlsx: An Excel file where I took the clean data and made a Pivot Table and a Slicer to make it easy to filter by artist.
