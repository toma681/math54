import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as A
import random

# Leetcode yayyy
def subsets(nums):
        def backtrack(start, curList, subsets):
            if start >= len(nums):
                subsets.append(curList[:])
                return
            
            curList.append(nums[start])
            backtrack(start+1, curList, subsets)
            del curList[-1]
            
            backtrack(start+1, curList, subsets)
                
        s = []
        backtrack(0, [], s)
        return s

questionNum = int(input("Question"))
numOptions0 = int(input("Options0: "))
if questionNum == 1:
    numOptions1 = int(input("Options1: "))

# excludeNums = []
# ask = True
# while ask:
#     exclude = input("Exclude? No if none, input number if yes")
    
#     excludeNums.append(int(exclude))

nums = []
if questionNum == 0:
    for num in range(numOptions0):
        nums.append(num)
elif questionNum == 1:
    for num in range(numOptions1):
        nums.append(num + numOptions0)

subsetLst = subsets(nums)

# Uncomment either of these :)
random.shuffle(subsetLst)
# subsetLst.sort()

driver = webdriver.Chrome()

driver.get("https://www.gradescope.com/courses/290863")

gscope = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Save All Answers']")))

time.sleep(1)

buttons = driver.find_elements_by_class_name('form--choice')

# Fix
submitButtons = driver.find_elements_by_class_name('btnv7')

prevCorrect = driver.find_elements_by_class_name('question--correctness-positive')

for i, subset in enumerate(subsetLst):
    
    for num in subset:
        buttons[num].click()

    submitButtons[questionNum].click()

    # print("Current Iteration: %s, Subset: %s") % (str(i), str(subset))
    print(i, subset)

    # Sleep required, otherwise it will skip correct ans :(
    # .4 can work too, .5 is safer
    time.sleep(.5)

    correctAns = driver.find_elements_by_class_name('question--correctness-positive')
    
    if len(correctAns) > len(prevCorrect):
        break

    for num in subset:
        buttons[num].click()

print("Completed")