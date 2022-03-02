import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://hashnode.com/community"

def web_wait_time():
    return driver.implicitly_wait(5)

def web_sleep_time():
    return time.sleep(10)

# web_wait_time()
driver.get(url)

blogs = []

def all_blogs():
    data = driver.find_elements(By.CLASS_NAME, "css-2wkyxu")

    # Loop through the different children_elements
    for data_elements in data:
        blog_data = data_elements.find_elements(By.TAG_NAME, "a:first-child")

        for blog in blog_data:
            blogs.append(blog.text)


lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# print(lenOfPage) -8000 +

match = 1
while match < 50:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    web_sleep_time()
    all_blogs()
    web_sleep_time()

    print(f"[+] -- We are on page {match}  out of {lenOfPage} pages of blog! --")
    match += 1


# Pair Blogs in a list of tuples
blog_length = len(blogs)
blog_list = []

for i in range(0, blog_length-1, 2):
    blog_info = blogs[i], blogs[i+1]
    blog_list.append(blog_info)


blog_list = list(set(blog_list))
# print(blog_list)

blogs_dataframe = pd.DataFrame(blog_list, columns=["Blog Title", "Blog_URL"])
blogs_dataframe.to_csv("all_blogs.csv")

driver.quit()
