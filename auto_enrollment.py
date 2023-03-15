from selenium.webdriver import Chrome as ch
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from datetime import datetime
from pytz import timezone
import time

ID = "19100586"
PW = "seoulman2000!"

driver = ch("/usr/local/bin/chromedriver")
driver.get("https://for-s.seoultech.ac.kr/view/login.jsp")

time.sleep(2)

ID_INPUT = driver.find_element_by_id("USER_ID")
PW_INPUT = driver.find_element_by_id("PWD")
ID_INPUT.send_keys(ID)
PW_INPUT.send_keys(PW)

SIGNUP_BTN = driver.find_element_by_id("btn_Login")
SIGNUP_BTN.click()

time.sleep(5)

driver.get("https://for-s.seoultech.ac.kr/view/sugang.jsp#tab-dayLess")
Alert(driver).dismiss()

SELECTION = Select(driver.find_element_by_id("cbo_dayLessLess"))
SELECTION.select_by_value("20050109")

COURSE_INPUT = driver.find_element_by_id("edt_dayLessSubjKnm")
COURSE_INPUT.send_keys("english")

SEARCH_BTN = driver.find_element_by_id("btn_dayLessSearch")
SEARCH_BTN.click()

time.sleep(2)

course_list = driver.find_elements_by_class_name("ui-jqgrid-bdiv")[1]


def loop_saver(course_list):
  MY_COURSE = course_list.find_elements_by_tag_name("input")[1]
  MY_COURSE.click()
  time.sleep(1)
  Alert(driver).accept()
  
    
while True:
  cnt = 0
  now = datetime.now(timezone('Asia/Seoul')).strftime("%M:%S")
  cur_time = now.split(":")
  min = int(cur_time[0])
  sec = int(cur_time[1])
  if sec % 10 == 0:
    loop_saver(course_list)
    cnt += 1
    print("registering've been tried!")
    time.sleep(2)
