# cu-unis

### Overview
Added functionality to get all the unis and information of everyone at Columbia using Cunix. In a nut shell, every uni at columbia has a home directory within the cunix cloud. Scraping all the directory names returns all the unis that are in use at Columbia. This will **only work if run from cunix**

### Implementation
This is a continuation of the research done by @fabiodesousa. His original work utilized the find command in order to list all the buckets but I improved performance by just using ```ls */*``` from the top level directory to get all the directory names and hence unis. From there, a lookup is done on every uni to grab the information on the individual from cunix. Some of the folder names are not valid unis and so will either return No information from the lookup or will open shell prompts which I automatically pass. 

### Running
Just run ```python ingest.py [format]``` with format being ```-csv``` or ```-json``` in order to output the data to a specific format. The default format with no flag is csv.

### Notes
* Not every field exists for every uni. Columbia undergrads tend to have departments while staff like maintenance does not. 
* Don't use this for spam, it was made for research purposes
