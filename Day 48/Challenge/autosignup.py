from selenium import webdriver

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys("Rajdip")
lname = driver.find_element_by_name("lName")
lname.send_keys("Das")
email = driver.find_element_by_name("email")
email.send_keys("raj@gmail.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()
