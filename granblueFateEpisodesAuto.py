from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open granblue and wait for it to load
driver.get("https://game.granbluefantasy.jp")
wait = WebDriverWait(driver, 30)

# Press Log in
logIn = wait.until(EC.element_to_be_clickable((By.ID, "login-auth")))
driver.execute_script("arguments[0].scrollIntoView(true);", logIn)
logIn.click()

# Wait for the Mobage login button to be clickable and click it
mobage = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-auth-login")))
mobage.click()

# Wait for the user to log in
input("Please log in manually on the webpage and then get to your Granblue Home Page. Press Enter when you're done...")

# Navigate to your fate quests
driver.get("https://game.granbluefantasy.jp/#quest/fate")

while True:
    # Find the element you want to click
    fate = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-quest-list lis-quest-list fate ico-new']")))

    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", fate)

    # Find the cover element
    cover = WebDriverWait(fate, 10).until(EC.visibility_of_element_located((By.XPATH, "./div[@class='prt-button-cover']")))

    # Modify the cover element to make it non-interfering
    driver.execute_script("arguments[0].style.pointerEvents = 'none';", cover)

    # Find the coordinates of the element
    location = fate.location
    size = fate.size
    x = location['x'] + size['width'] / 2
    y = location['y'] + size['height'] / 2

    # Click on the element at the calculated coordinates
    ActionChains(driver).move_to_element_with_offset(fate, x, y).click().perform()

    input("Please accept manually and/or wait until the next page has loaded fully. Press Enter when ready.")

        
    # Skip
    print("skipping beginning...")
    # Wait for the skip1 button to be clickable after scrolling into view
    skipOne = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-skip']")))

    # initiate a top point to scroll back up to
    top = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-header logView']")))

    # Scroll the skip1 button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", skipOne)

    # Use Action Chains to move to the skip1 button and click it
    actions = ActionChains(driver)
    actions.move_to_element(skipOne).click().perform()
    print("skip1 clicked...")

    # Scroll back up
    driver.execute_script("arguments[0].scrollIntoView(true);", top)
    print("scrolled back up")

    # Hide the interfering elements
    synopsis = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='prt-pop-synopsis']")))
    script = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-scenario-all-read']")))
    driver.execute_script("arguments[0].style.display = 'none';", synopsis)
    driver.execute_script("arguments[0].style.display = 'none';", script)

    # Wait for the skip2 button to be clickable after scrolling into view
    skipTwo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn-scene-skip']")))

    # Find the coordinates of the element
    location = skipTwo.location
    size = skipTwo.size
    x = location['x'] + size['width'] / 2
    y = location['y'] + size['height'] / 2

    # Click on the element at the calculated coordinates
    ActionChains(driver).move_to_element_with_offset(skipTwo, x, y).click().perform()
    print("skip2 clicked...")

    time.sleep(3)
    print("continuing loop")
    # Navigate back to fate quests
    driver.get("https://game.granbluefantasy.jp/#quest/fate")
