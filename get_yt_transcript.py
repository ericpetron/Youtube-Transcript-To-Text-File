import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Getting the URL
get_yt_url = str(input('Please paste the URL here: '))

# Initializing the webdriver
ser = Service(r'/Users/ericpetron/Dropbox/SummerJava/geckodriver')
op = webdriver.FirefoxOptions()
driver = webdriver.Chrome(service=ser, options=op)

# Giving webdriver time to load browser
time.sleep(2)
# Going to the URL
driver.get(get_yt_url)
#
time.sleep(7)
triple_dot_button = driver.find_element(by=By.CSS_SELECTOR, value='ytd-menu-renderer.ytd-video-primary-info-renderer > yt-icon-button:nth-child(3) > button:nth-child(1)')
triple_dot_button.click()
time.sleep(3)
show_tran = driver.find_element(by=By.CSS_SELECTOR, value='tp-yt-paper-item.ytd-menu-service-item-renderer')
show_tran.click()
time.sleep(5)

# MAKE THIS RECURSIVE
def get_the_raw_tran():
    '''
    Purpose: To loop through all of the elements that contain the transcript in it
    Parameters: None
    Return Value: A list of all of the of raw web elements containing the text of the transcript in them
    '''
    elements = []
    n = 1
    while True:
        try:
            
                
            ele = driver.find_element(by=By.CSS_SELECTOR, value=f'ytd-transcript-segment-renderer.style-scope:nth-child({n}) > div:nth-child(1) > yt-formatted-string:nth-child(2)')
            elements.append(ele)
            n += 1
        except:
            print('Done collecting text!')
            return elements
# Let the computer be for a bit        
time.sleep(3)
# Run the function above
raw_list = get_the_raw_tran()



def convert_raw_tran_to_text_tran(raw_ls):
    '''
    Purpose: Converts the class of the web elements into readble text in a list
    Parameters: raw_ls: This list contains all of the raw objects from the 'get_the_raw_tran' function
    Return Value: A list of readable text that contains the transcript
    '''
    text_list = []
    for each_ele in raw_ls:
        
        text_list.append(each_ele.text)
    
    
    return text_list



# Convert the web elements into text
list_of_text_from_tran = convert_raw_tran_to_text_tran(raw_list)

def writing_to_a_text_file(list_of_text):
    
    write_to_file = open('yt_transcipt.txt', 'w')

    for i in range(3):
        # This is used to separate the differences in the transcripts 
        write_to_file.write('\n')

    for iterate in list_of_text:
        write_to_file.write(f'{iterate} ')

writing_to_a_text_file(list_of_text_from_tran)







driver.close()
print('All done!')





# CSS formatting ytd-transcript-segment-renderer.style-scope:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(2)

# ytd-transcript-segment-renderer.style-scope:nth-child(2) > div:nth-child(1) > yt-formatted-string:nth-child(2)

# ytd-transcript-segment-renderer.style-scope:nth-child(3) > div:nth-child(1) > yt-formatted-string:nth-child(2)




