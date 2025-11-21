# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #4 Parse wikipage and extract the headers of the page.
#  * BeautifulSoup + Requests Library
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Import Libraries
import requests
from bs4 import BeautifulSoup

# Function
def header_finder(soup, header_name, header_num_list, header_dic):
    ''' Extract any possible headers in div from the page '''
    for div in soup:
        for idx in range(len(header_num_list)):
            heading = div.find("h" + header_num_list[idx])
            if heading is not None:
                header_dic[header_name].append(heading.text)
    return header_dic

# Variables
header_num = ["1", "2", "3", "4", "5", "6", "7"]    # possible header numbers
headerdic = {"div Header": [], "body Header": []}   # Dictionary to store headers for div and body
URL_Taiwan_wiki = "https://en.wikipedia.org/wiki/Taiwan"

# Obtain the html code using requests
page_info_response = requests.get(URL_Taiwan_wiki)

# Parse Html info using BeautifulSoup
html_soup = BeautifulSoup(page_info_response.text, "html.parser")

# Find all lines that start with 'div' and 'body'
div_result = html_soup.find_all('div')
body_content = html_soup.find_all('body')

# Call function header_finder to get all header info and store in the dictionary
div_header = header_finder(div_result, "div Header", header_num, headerdic)
body_header = header_finder(body_content, "body Header", header_num, headerdic)

# Output the results for 'div' and 'body'
print("< 'div' Headers >")
print(headerdic["div Header"])
print("----------------------------------------------------------------------------------------------")
print("< 'body' Headers >")
print(headerdic["body Header"])
