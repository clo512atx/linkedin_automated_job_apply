#BH RN auto job apply w/ linkedin easy apply

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import time



class ApplyLinkedin:

    def __init__(self,data) -> None:
        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        self.driver = webdriver.Chrome(data['driver_path'])
        

    def login(self):
        
        self.driver.get('https://www.linkedin.com/login')
        self.driver.maximize_window()
        
        
#enter in our email/password and submit
        login_email = self.driver.find_element('name', 'session_key')
        login_email.send_keys(self.email)
        time.sleep(2)

        password = self.driver.find_element('name', 'session_password')
        password.send_keys(self.password)
        time.sleep(2)
        
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def jobSearch(self):
#keyword and location on jobs tab
        jobs_link = self.driver.find_element('link text','Jobs')
        jobs_link.click()
        time.sleep(2)
        
#insert keyword and location
        keyword_search = self.driver.find_element('xpath','/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
        keyword_search.clear()
        keyword_search.send_keys(self.keywords)
        time.sleep(2)

        location_search = self.driver.find_element('xpath','/html/body/div[5]/header/div/div/div/div[2]/div[3]/div/div/input[1]')
        location_search.clear()
        location_search.send_keys(self.location)
        time.sleep(2)
        
        location_search.send_keys(Keys.RETURN)
        time.sleep(2)

#filter selections/criterias (PRN,part time, other, and fulltime jobs.) 
#Add beh hosp. to network (Georgetown, Acadia, HCS, Rock springs, Ascension)
#Most relevant, and job type=Nurse

    def exit_application(self):
        cancel_button = self.driver.find_element(By.XPATH, '//li-icon[contains(@type, "cancel-icon")]')
        cancel_button.click()
        time.sleep(1)
        discard_button = self.driver.find_element(By.XPATH, '//button[contains(@data-control-name, "discard_application_confirm_btn")]')
        discard_button.click()
        print("exited out of this application, moving to the next one")
    
    
    def easyApply(self):
        easy_apply_button = self.driver.find_element('xpath','/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[9]/div/button')
        easy_apply_button.click()
        time.sleep(2)
            
        # job_cards = self.driver.find_elements(By.XPATH, '//li[contains(@class, "jobs-search-results__list-item")]')
        job_cards = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//a[contains(@class, "base-card__full-link")]')))
        print("found " + str(len(job_cards)) + " jobs")
        for job in job_cards:
            print(job)
        
        job_number = 1
        for job in job_cards:
            print("looking at job " + str(job_number) + " out of " + str(len(job_cards)))
            apply_now_button = job.find_element(By.XPATH, '//button[contains(@class, "jobs-apply-button")]') 
            apply_now_button.click()
            try:
                phone_number_input = self.driver.find_element(By.XPATH, '//input[contains(@id, "phoneNumber")]')
                phone_number_input.send_keys("2677132751")
            except:
                print("unable to find phone number input!")
                # need to change this so it clicks out of the Easy Apply form
                continue
            
            try:
                # next_button = self.driver.find_element(By.XPATH, '//button[@contains(@class, "artdeco-button--primary")]')
                next_button = job.find_element(By.CSS_SELECTOR, "button span[class='artdeco-button__text']").click()
                next_button.click()
                try:
                    upload_resume = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Upload resume')]")))
                    upload_resume.click()
                except:
                    print("can't upload resume")
            except:
                print("unable to find next button, exiting application")
                self.exit_application()
            time.sleep(3)
            job_number += 1

        # allfilter_button = self.driver.find_element('xpath','/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/div/div/button')
        # allfilter_button.click()
        # time.sleep(2)
    

        # most_relevant = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[2]/input')
        # most_relevant.click()
        # time.sleep(2)

        # anytime_button = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[1]/input')
        # anytime_button.click()
        # time.sleep(5)

        # fulltime_button = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[1]/input')
        # fulltime_button.click()
        # time.sleep(5)
        # parttime_button = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[2]/input')
        # parttime_button.click()
        # time.sleep(5)
        # contract_button = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[3]/input')
        # contract_button.click()
        # time.sleep(5)
        # other_button = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[4]/input')
        # other_button.click()
        # time.sleep(5)

        # show_results = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[3]/div/button[2]')
        # show_results.click()
        # time.sleep(2)



'''
#adding in hospitals that are not on general search field
        add_companies = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[5]/fieldset/div/ul/li[19]/button/span')
        add_companies.click()
        time.sleep(5)

        add_companies.send_keys(self.companyone)
        rocksprings = self.driver.find_element('xpath','/html/body/div[3]/div/div/div[2]/ul/li[5]/fieldset/div/ul/li[19]')
        rocksprings.click()
'''        



        



if __name__ =="__main__":

    with open(r'data.json') as user_data:
        data = json.load(user_data)
    bot = ApplyLinkedin(data)
    bot.login()
    time.sleep(5)
    bot.jobSearch()
    time.sleep(5)
    bot.easyApply()
    time.sleep(5)

    
