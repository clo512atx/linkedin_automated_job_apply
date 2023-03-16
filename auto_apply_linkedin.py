#BH RN auto job apply w/ linkedin easy apply

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
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
        time.sleep(20)

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

    def finish_submission(self):
        try:
            cancel_button = self.driver.find_element(By.XPATH, '//li-icon[contains(@type, "cancel-icon")]')
            cancel_button.click()
            print("finished submitting application, moving to the next one")
        except (ElementNotInteractableException, NoSuchElementException):
            print("application already exited, moving to the next one")

    
    
    def easyApply(self):
        easy_apply_button = self.driver.find_element('xpath','/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[9]/div/button')
        easy_apply_button.click()
        time.sleep(5)
            
        job_cards = self.driver.find_elements(By.XPATH, '//li[contains(@class, "jobs-search-results__list-item")]')

        for job in job_cards:
            submitted = False
            job.click()
            time.sleep(2)
            try:
                apply_now_button = job.find_element(By.XPATH, '//button[contains(@class, "jobs-apply-button")]') 
                apply_now_button.click()
            except NoSuchElementException:
                print("we already applied to this job, going to the next submission")
                continue
            
            while not submitted:
                try:
                    phone_number_input = self.driver.find_element(By.XPATH, '//input[contains(@id, "phoneNumber")]')
                    phone_number_input.clear()
                    phone_number_input.send_keys("2677132751")
                except:
                    print("unable to find phone number input!")

                try:
                    already_uploaded_resume = self.driver.find_element(By.XPATH, '//span[text()="Choose"]')
                    already_uploaded_resume.click()
                    time.sleep(1)
                except:
                    print("nowhere to select resume, trying something else")
        
                # language proficiency
                try:
                    select_proficiency_prompts = self.driver.find_elements(By.XPATH, '//select[@aria-required="true"]/option[text()="Native or bilingual"]')
                    for select_proficiency in select_proficiency_prompts:
                        select_proficiency.click()
                except:
                    print("no language selection")

                # yes/no select
                try:
                    select_yes_prompts = self.driver.find_elements(By.XPATH, '//select[@aria-required="true"]/option[text()="Yes"]')
                    for select_yes in select_yes_prompts:
                        select_yes.click()
                except:
                    print("no yes/no selection")

                # yes/no radio
                try:
                    select_yes_radio_buttons = self.driver.find_elements(By.XPATH, '//input[@type="radio"][@value="Yes"]')
                    for select_yes in select_yes_radio_buttons:
                        select_yes.click()
                except:
                    print("no yes/no radio buttons")

                # years of experience
                try:
                    # years_of_exp_labels = self.driver.find_elements(By.XPATH, '//label[contains(@for, "single-line-text-form-component")]')
                    # for years_of_exp in years_of_exp_labels:
                    #     prompt = years_of_exp.get_attribute('innerHTML').lower()
                    #     if "years" in prompt:
                    #         years_of_exp_input = prompt.find_element(By.XPATH, '//input[contains(@id, "single-line-text-form-component")]')
                    #         years_of_exp_input.send_keys("6")
                    years_of_exp_labels = self.driver.find_elements(By.XPATH, '//input[contains(@for, "single-line-text-form-component")]')
                    for years_of_exp in years_of_exp_labels:
                        years_of_exp.send_keys("6")
                except:
                    print("no years of experience prompts")

                try:
                    follow_company_checkbox = self.driver.find_element(By.XPATH, '//input[contains(@id, "follow-company-checkbox")]')
                    follow_company_checkbox.click()
                except:
                    print("no follow company checkbox available to unclick, trying something else")

                try:
                    submit_application = job.find_element(By.XPATH, '//button[contains(@aria-label, "Submit application")]')
                    submit_application.click()
                    submitted = True
                except:
                    print("unable to find submit button")
                time.sleep(1)

                try:
                    next_button = self.driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')
                    next_button.click()
                except:
                    print("unable to find next button")
                time.sleep(1)

                time.sleep(5)
            time.sleep(2)
            self.finish_submission()
            time.sleep(3)

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

    
