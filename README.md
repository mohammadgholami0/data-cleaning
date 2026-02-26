I found a dataset of top-grossing concert tours online and wanted to analyze which artists made the most money per show. The problem was that the data was very messy and not usable for analysis in its original form.

The dataset contained Wikipedia-style footnotes, special symbols, and currency values that Excel and Python could not treat as numbers. Before doing any analysis, the data needed to be cleaned and structured properly.

What was wrong with the data?

When I first opened the CSV file, I couldn’t do any calculations because of several issues:

Numbers weren’t numbers
All revenue values included $ signs and commas, so they were read as text instead of numeric values.

Footnote junk
Many columns contained brackets and references like 7[2] or symbols such as †, which made sorting and ranking unreliable.

Date ranges instead of years
Years were written as ranges like 2023–2024, which are difficult to sort or compare. I needed a clean start year for each tour.

How I fixed it

Instead of cleaning the data manually in Excel, I wrote a Python script to automate the process. but after i opened the file with excel still data wasnot in order in excel so i  organize data in excel also 

Regex cleaning
I used regular expressions to remove anything inside brackets and to strip out special symbols. This cleaned names, rankings, and text fields in one step.

Money conversion
I removed $ signs and commas from revenue columns and converted them to numeric values so they could be used in calculations.

Splitting years
I extracted the first four characters from the year column to create a new Start_Year column that could be sorted correctly.

What’s in this repository?

this.csv
The original raw dataset with all the formatting issues.

clean_data.py
The Python script used to clean and structure the data.

structured_tour_data.csv
The final cleaned version of the dataset, ready for analysis.

Final_Analysis.xlsx
An Excel file where I used pivot tables and a slicer to explore revenue per show by artist.

Result

After cleaning the data, it became possible to sort, filter, and analyze the tours properly. The dataset can now be used in Excel, Python, or other tools to compare artists and understand revenue patterns.

This project focuses on data cleaning and preparation, which is often the most important step before any real analysis.
