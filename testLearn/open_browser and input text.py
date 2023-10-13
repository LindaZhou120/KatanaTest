from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Find the email and password input fields and enter your credentials
email_field = driver.find_element_by_id("username")
email_field.send_keys("your_email@example.com")

password_field = driver.find_element_by_id("password")
password_field.send_keys("your_password")

# Press Enter to submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load and then find an element on the home page
driver.implicitly_wait(10)
element = driver.find_element_by_xpath("//input[@placeholder='Search']")

# Perform a search by entering a keyword and pressing Enter
element.send_keys("Python Developer")
element.send_keys(Keys.RETURN)

# Extract and print the names of the search results
results = driver.find_elements_by_xpath("//span[@class='name actor-name']")
for result in results:
    print(result.text)

# Close the browser window
driver.quit()
