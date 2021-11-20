####################################################################
# Skeleton for Appium tests on Sauce Labs Real Devices - Unified Platform
# This is currently in BETA and will only work for private devices
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
import requests
from time import sleep
import os
import urllib3
import json
import random
import sys
from colorama import Fore, Back, Style


androidTest = False
iosTest = True
useApp = False
appLocation = 'storage:db1f085c-dec1-4031-aaee-cdf6e15f9b76'
# appLocation = 'storage:filename=NetworkSpeed 2.zip'

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Pull a random Pokemon name to use as the test name
###################################################################
# pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
# pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
# random_pokemon = random.choice(pokemon_names)

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################
# androidTest = True
# iosTest = True

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
region = 'US'

###################################################################
# Common parameters (desired capabilities)
###################################################################
projectParameters = {
    # 'tags':['Case', 'Investigation',],
    # The following are not required
    # ''tunnelIdentifier': 'exampletunnel'
    # 'app': 'storage:610f9e00-9415-44a2-94f1-a1f418663cd3',
    # 'app': 'storage:8a8b7702-f4fb-4788-93fa-8a8a3e631c74',
    }

androidParameters = {
    'browserName': 'Chrome',
    'platformName': 'Android',
    # 'platformVersion': '11',
    'name': 'Appium Test',

    # 'phoneOnly': 'true',
    # Define Android parameters here
    'deviceName' : 'Google.*',
    # 'deviceName' : 'Samsung Galaxy S10\+',
    # 'deviceName' : '(Samsung.*)|(Huawei.*)|(Xiaomi.*)|(OnePlus.*)|(Google.*)',
    # 'deviceName' : 'Google Pixel 3 .*',
    # 'orientation' : 'LANDSCAPE',
    # 'platformName' : 'Android',
    # 'browserName' : 'Chrome',
    # 'platformVersion' : '11',
    # 'otherApps': 'storage:5471e3e8-5be6-48f7-8968-47ffc574b2f6',
    # 'appiumVersion': '1.14.0',
    # 'deviceOrientation': 'portrait',
}

iosParameters = { # Define iOS Parameters here
    # 'deviceName' : 'iPhone [6-8]',
    'deviceName' : 'iPhone.*',
    # 'platformVersion' : '13',
    'platformName' : 'iOS',
    # 'phoneOnly': 'true',
    'name': 'rolex test',
    # 'autoDismissAlerts': 'true',
    # 'connectHardWareKeyboard' : 'true',
    'browserName' : 'safari',
    # 'newCommandTimeout' : '0',
    # 'nativeWebTap': 'true',
}

###################################################################
# Merge parameters into a single capability dictionary

###################################################################
sauceParameters = {}
if androidTest != True and iosTest != True:
    print('You need to specify a platform to test on!')
    sys.exit()
elif androidTest == True and iosTest == True:
    print('Don\'t be greedy! Only choose one platform!')
    sys.exit()
elif androidTest:
    sauceParameters.update(androidParameters)
    if useApp:
        sauceParameters['app'] = appLocation # Use app if it's specified
    else:
        sauceParameters['browserName'] = 'Chrome' # Otherwise use Chrome
        #Note! Replace 'Chrome' with 'Browser' for older versions of Android to use the stock browser
elif iosTest:
    sauceParameters.update(iosParameters)
    if useApp:
        sauceParameters['app'] = appLocation
    else:
        sauceParameters['browserName'] = 'safari'



# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': 'Investigation'})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print(Fore.MAGENTA + 'You are using the US data center for an RDC test, so a bald eagle is obviously running your tests.' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print (Fore.CYAN + 'You are using the EU data center for an RDC test, you beautiful tropical fish!' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################
# # # Navigating to a website
# driver.get_window_size()
driver.get('https://www.rolex.com/world-of-rolex/rolex-and-cinema.html')
# # #
# # # # Finding an element
driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[1]/div/div[1]/div[4]/div[1]/div[1]/div[1]/section/div[2]/div/div[1]/button').click()
sleep(10)
#
# #
# # # # Using the selected element
# # interact.click()

# # # Saving an extra screenshot
# # driver.save_screenshot('screenshot.png')
# #
# # # Using Action chains
# # # ActionChains(driver).move_to_element(interact).perform()
# #
# # # Sauce Labs specific executors
# # # driver.execute_script('sauce: break')
# # # driver.execute_script('sauce:context=Notes here')
#
#
# # Setting the job status to passed
# driver.execute_script('sauce:job-result=passed')
#
# # Ending the test session
driver.quit()
