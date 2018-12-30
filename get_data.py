import os
import mechanicalsoup as ms

def main():
    URL = "https://www.ncbi.nlm.nih.gov/nucgss/BH854445.1" # sequence for E. coli EC2029
    
    browser = ms.StatefulBrowser()
    browser.open(URL)
    #print(browser.get_current_page())
    data_lines = browser.get_current_page().find_all(lambda x: x.name == 'src' and x.get('class') == "sequence")
    print(data_lines)
    
    data = ""
    for line in data_lines:
        data += str(line.contents).strip()

    return data

if __name__ == "__main__":
    print(main()) # for testing
    