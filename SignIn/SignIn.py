from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
driver.find_element_by_xpath("//input[@id='firstName']").send_keys("Nikos")
driver.find_element_by_xpath("//input[@id='lastName']").send_keys("Varelas")
radio_button = driver.find_elements_by_xpath("//*[@id='genterWrapper']/div[2]/div[1]/label")
radio_button[0].click()
driver.find_element_by_xpath("//input[@id='userNumber']").send_keys("6912345678")
driver.execute_script("window.scrollBy(0,1000)")
driver.find_element_by_xpath("//*[@id='submit']").click()
submit_text = driver.find_element_by_xpath("//div[@id='example-modal-sizes-title-lg']").text
driver.get_screenshot_as_file("Sheets/ToolsQA_form.png")
assert "Thanks for submitting the form" == submit_text
driver.get_screenshot_as_file("C:/Users/nikos/OneDrive/Υπολογιστής/BootCamps/Github/Python Unittest/files/screeshot.png")
driver.close()
