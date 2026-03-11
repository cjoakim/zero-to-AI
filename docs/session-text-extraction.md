# Part 3, Session 14 - Text Extraction, Markdown, Chunking, and Vectorization

<br><br>

## Text Data

- It's messy and unstructured, other than natural language syntax 
- It exists in multiple natural language formats: English, Spanish, French, German, etc.
- It's not clean and delimited like CSV or JSON
- It exists in great quantity and variety
- It can contain extremely valuable information

<br><br><br>
---
<br><br><br>

## Where does it exist?

In **multiple filetypes**: 

- General types: pdf, html, txt 
- Image types: jpeg, jpg, png, bmp, heif, tiff
- MS Office types: docx, xlsx, pptx

<br><br><br>
---
<br><br><br>

## LLMs and Text Data

- Prompts are expressed with simple text content (not PDF, Word, Excel, etc.)
- They generally don't understand these file formats 
- They prefer the **markdown format** instead
- Therefore, for AI applications, we need to convert the text data into markdown format

<br><br><br>
---
<br><br><br>

## Markdown Format 

- This is a simple text format with very few "markup" functionality 
- md file suffix
- The README.md file and all zero-to-AI presentation content is in markdown format
- [John Gruber's original Markdown spec](https://daringfireball.net/projects/markdown/)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [Markdown Guide Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

<br><br><br>
---
<br><br><br>

## Typical Azure AI Workflow for Text Data 

- **Land the raw data into Azure Storage** 
  - Word documents, Excel spreadsheets, PowerPoint presentations, Images, etc.
  - Per the "Medallion Architecture" pattern described in the Azure Storage session
- **Extract the text from the raw data using Azure Document Intelligence**
  - This converts the raw data into markdown format
  - Land the markdown data into Azure Storage silver layer of the Medallion Architecture
  - This will be demonstrated in this session
- **Chunk the Markdown data into smaller pieces/chunks**
  - To fit LLM context window limits
  - Chunking Strageties: page, character count, sentence count, etc.
  - Overlapping chunks are common 
    - For example, pages [40,41,42] is one chunk, pages [41,42,43] is another chunk, etc.
  - Land these chunks into the Silver layer of the Medallion Architecture
- **Vectorize the chunks**
  - Create an embedding/vector value for each chunk using Azure OpenAI
  - Add these chunks with vectors into a **Vector Database** for **semantic search** 
    - For example: **Azure Cosmos DB**, **Azure AI Search**, **Azure PostgreSQL**, etc.
    - The [DiskANN](xxx) algorithm is very efficient for vector search
- **Solve the problem at hand with a LLM, RAG, semantic search, etc.**

> Azure DiskANN is a high-performance, disk-based vector indexing and search algorithm
> developed by Microsoft Research for efficiently searching through massive, 
>billion-point datasets

- See https://devblogs.microsoft.com/cosmosdb/diskann-for-azure-cosmos-db-now-in-open-public-preview/
- See https://docs.azure.cn/en-us/cosmos-db/vector-search
- See https://techcommunity.microsoft.com/blog/adforpostgresql/introducing-diskann-vector-index-in-azure-database-for-postgresql/4261192

<br><br><br>
---
<br><br><br>

## Azure Document Intelligence

- Previously known as **Azure Form Recognizer**, rebranded in 2023 to **Azure Document Intelligence**
- It can extract text from a wide variety of filetypes
  - bmp, docx, heif, html, jpeg, jpg, md, pdf, png, pptx, tiff, xlsx
- It can extract text from **images**. Including, for example, **PDFs** with images
- Output formats include: JSON, PDF, and **markdown**

### References

- https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/
- [azure-ai-documentintelligence SDK @ pypi](https://pypi.org/project/azure-ai-documentintelligence/)

### Example Extracted Markdown 


```
...

Before he enter on the Execution of his Office, he shall
take the following Oath or Affirmation :- "I do solemnly
swear (or affirm) that I will faithfully execute the Office of
President of the United States, and will to the best of my
Ability, preserve, protect and defend the Constitution of
the United States."

<!-- PageFooter="CONSTITUTION OF THE UNITED STATES" -->
<!-- PageBreak -->

### SECTION. 2

The President shall be Commander in Chief of the Army
and Navy of the United States, and of the Militia of the
...
```

Notice how Azure Document Intelligence nicely adds the **<!-- PageBreak -->**
markers to the extracted markdown content.  This is very useful for chunking.

<br><br><br>
---
<br><br><br>

## Demonstration of Text Extraction, Chunking, and Vectorization

See **docintel-demo.ps1** and **docintel-demo.sh** in the **python** directory.

This demo uses the input file **python/data/documents/US_Constitution.pdf** in this repository.

### Extracted Text Chunk 

```
<!-- PageBreak -->

# We the People of the United States

We the People of the United States, in Order to form a
more perfect Union, establish Justice, insure domestic
Tranquility, provide for the common defence, promote
the general Welfare, and secure the Blessings of Liberty to
ourselves and our Posterity, do ordain and establish this
Constitution for the United States of America


## Article. I.


### SECTION. 1

All legislative Powers herein granted shall be vested in a
Congress of the United States, which shall consist of a Sen-
ate and House of Representatives.


### SECTION. 2

The House of Representatives shall be composed of Mem-
bers chosen every second Year by the People of the several
States, and the Electors in each State shall have the Qualifi-
cations requisite for Electors of the most numerous Branch
of the State Legislature.

No Person shall be a Representative who shall not have
attained to the Age of twenty five Years, and been seven
Years a Citizen of the United States, and who shall not,
when elected, be an Inhabitant of that State in which he
shall be chosen.

[Representatives and direct Taxes shall be apportioned
among the several States which may be included within
this Union, according to their respective Numbers, which
shall be determined by adding to the whole Number of
free Persons, including those bound to Service for a Term
of Years, and excluding Indians not taxed, three fifths of
all other Persons.]* The actual Enumeration shall be made

within three Years after the first Meeting of the Congress
of the United States, and within every subsequent Term of
ten Years, in such Manner as they shall by Law direct. The
Number of Representatives shall not exceed one for every
thirty Thousand, but each State shall have at Least one
Representative; and until such enumeration shall be made,
the State of New Hampshire shall be entitled to chuse
three, Massachusetts eight, Rhode-Island and Providence
Plantations one, Connecticut five, New-York six, New
Jersey four, Pennsylvania eight, Delaware one, Maryland
six, Virginia ten, North Carolina five, South Carolina five,
and Georgia three.

When vacancies happen in the Representation from any
State, the Executive Authority thereof shall issue Writs of
Election to fill such Vacancies.

The House of Representatives shall chuse their
Speaker and other Officers; and shall have the sole
Power of Impeachment.


### SECTION. 3

The Senate of the United States shall be composed of two
Senators from each State, [chosen by the Legislature there-
of,]* for six Years; and each Senator shall have one Vote.

Immediately after they shall be assembled in Consequence
of the first Election, they shall be divided as equally as may
be into three Classes. The Seats of the Senators of the first
Class shall be vacated at the Expiration of the second Year,
of the second Class at the Expiration of the fourth Year, and
of the third Class at the Expiration of the sixth Year, so that
one third may be chosen every second Year; [and if Vacan-
cies happen by Resignation, or otherwise, during the Recess
of the Legislature of any State, the Executive thereof may
make temporary Appointments until the next Meeting of
the Legislature, which shall then fill such Vacancies.]*

<!-- PageFooter="CONSTITUTION OF THE UNITED STATES" -->
```

### Extracted Chunk Document With embedding

```
{
  "file": "US_Constitution",
  "chunk_idx": 1,
  "length": 3240,
  "text": "# We the People of the United States\n\nWe the People of the United States, in Order to form a\nmore perfect Union, establish Justice, insure domestic\nTranquility, provide for the common defence, promote\nthe general Welfare, and secure the Blessings of Liberty to\nourselves and our Posterity, do ordain and establish this\nConstitution for the United States of America\n\n\n## Article. I.\n\n\n### SECTION. 1\n\nAll legislative Powers herein granted shall be vested in a\nCongress of the United States, which shall consist of a Sen-\nate and House of Representatives.\n\n\n### SECTION. 2\n\nThe House of Representatives shall be composed of Mem-\nbers chosen every second Year by the People of the several\nStates, and the Electors in each State shall have the Qualifi-\ncations requisite for Electors of the most numerous Branch\nof the State Legislature.\n\nNo Person shall be a Representative who shall not have\nattained to the Age of twenty five Years, and been seven\nYears a Citizen of the United States, and who shall not,\nwhen elected, be an Inhabitant of that State in which he\nshall be chosen.\n\n[Representatives and direct Taxes shall be apportioned\namong the several States which may be included within\nthis Union, according to their respective Numbers, which\nshall be determined by adding to the whole Number of\nfree Persons, including those bound to Service for a Term\nof Years, and excluding Indians not taxed, three fifths of\nall other Persons.]* The actual Enumeration shall be made\n\nwithin three Years after the first Meeting of the Congress\nof the United States, and within every subsequent Term of\nten Years, in such Manner as they shall by Law direct. The\nNumber of Representatives shall not exceed one for every\nthirty Thousand, but each State shall have at Least one\nRepresentative; and until such enumeration shall be made,\nthe State of New Hampshire shall be entitled to chuse\nthree, Massachusetts eight, Rhode-Island and Providence\nPlantations one, Connecticut five, New-York six, New\nJersey four, Pennsylvania eight, Delaware one, Maryland\nsix, Virginia ten, North Carolina five, South Carolina five,\nand Georgia three.\n\nWhen vacancies happen in the Representation from any\nState, the Executive Authority thereof shall issue Writs of\nElection to fill such Vacancies.\n\nThe House of Representatives shall chuse their\nSpeaker and other Officers; and shall have the sole\nPower of Impeachment.\n\n\n### SECTION. 3\n\nThe Senate of the United States shall be composed of two\nSenators from each State, [chosen by the Legislature there-\nof,]* for six Years; and each Senator shall have one Vote.\n\nImmediately after they shall be assembled in Consequence\nof the first Election, they shall be divided as equally as may\nbe into three Classes. The Seats of the Senators of the first\nClass shall be vacated at the Expiration of the second Year,\nof the second Class at the Expiration of the fourth Year, and\nof the third Class at the Expiration of the sixth Year, so that\none third may be chosen every second Year; [and if Vacan-\ncies happen by Resignation, or otherwise, during the Recess\nof the Legislature of any State, the Executive thereof may\nmake temporary Appointments until the next Meeting of\nthe Legislature, which shall then fill such Vacancies.]*",
  "embedding": [
    -0.0005618606228381395,
    0.0063864691182971,
    -0.00553557276725769,

    ...

    -0.00854059774428606,
    -0.003333996282890439,
    -0.027000941336154938
  ]
}
```

<br><br><br>
---
<br><br><br>

# Homework 

- Run the demo on your computer 
- Try a different input file (a small file, 10 pages or less)
  - Copy the python/docintel-demo.ps1 or python/docintel-demo.sh to your computer
  - Edit the script to use your input file
  - Run the script
  - Observe the outputs

<br><br><br>
---
<br><br><br>

[Home](../README.md)
