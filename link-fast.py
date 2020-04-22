from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from time import sleep

import decimal
import random
import itertools    
from selenium.webdriver.common.action_chains import ActionChains

class LinkBot():
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=cookies/rtauler") 
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=options,service_args=["--verbose", "--log-path=/home/rtauler/linkedin/log.log"])
        self.driver.implicitly_wait(15)

    def login(self):
        self.driver.get('https://www.linkedin.com/jobs/')
        print("Entering linkedin")
        sleep(2)
    
    def input_job(self):
        job_name = self.driver.find_element_by_css_selector('[aria-label="Buscar empleos"]')
        job_name.send_keys('Designer')         
        print('Typed name of job')

        job_name = self.driver.find_element_by_css_selector('[aria-label="Buscar ubicación"]')
        job_name.send_keys('Barcelona')
        print('Typed location')

        search_btn = self.driver.find_element_by_css_selector('[type="submit"]')
        search_btn.click()
        print('Clicked Search')

    def filter_ea(self):
        ea_dropdown_btn = self.driver.find_element_by_css_selector('[aria-label="Filtro «Funcionalidades de LinkedIn». Al hacer clic en este botón, se muestran todas las opciones del filtro «Funcionalidades de LinkedIn»."]')
        ea_dropdown_btn.click()

        ea_filter_btn = self.driver.find_element_by_css_selector('[for="f_LF-f_AL"]')
        ea_filter_btn.click()

        apply_btn = ActionChains(self.driver)
        apply_btn.move_to_element(ea_filter_btn).move_by_offset(200, 100).click().perform()

        print("Display only easy applies")

    def filter_recent(self):
        rec_dropdown_btn = self.driver.find_element_by_css_selector('[aria-label="Ordenar por"]')
        rec_dropdown_btn.click()

        rec_filter_btn = self.driver.find_element_by_css_selector('[for="sort-by-date"]')
        rec_filter_btn.click()

        apply_btn = ActionChains(self.driver)
        apply_btn.move_to_element(rec_filter_btn).move_by_offset(200, 100).click().perform()       

        print("Sort by most recent")

    def apply_job(self):
        sleep(0.5)
        try:
            #try to click the easy apply button, if its not there beacuse the job is already applied go to the next
            ea_btn = self.driver.find_element_by_css_selector('[data-control-name="jobdetails_topcard_inapply"]')
            ea_btn.click()
            #best causistic, no next pages, only one page with CV and apply
            try:
                #do not follow company
                not_follow = self.driver.find_element_by_css_selector('[for="follow-company-checkbox"]')
                not_follow.click()
                sleep(1)
                #send appliance
                send_ea = self.driver.find_element_by_css_selector('[aria-label="Enviar solicitud"]')
                send_ea.click()
                #close popup
                sleep(1)
                close_ea = self.driver.find_element_by_css_selector('[aria-label="Dismiss"]')
                close_ea.click()
                print('Job applied')
            except Exception:   
                try:
                    #close popup
                    close_ea = self.driver.find_element_by_css_selector('[aria-label="Dismiss"]')
                    close_ea.click()

                    #locate main logo
                    link_logo = self.driver.find_element_by_class_name('nav-main__inbug-container')

                    #move to logo and click on dismiss
                    discard_btn = ActionChains(self.driver)
                    discard_btn.move_to_element(link_logo).move_by_offset(600, 330).click().perform()
                    print('Job ignored')
                except Exception:
                    pass
        except Exception:
            #this is for the case of in an already filtered screen to display only easy apply there's no 
            #easy apply button in the job card
            pass


    def scroll_next(self,i):           
            #assign id to job list to make it scrollable
            self.driver.execute_script('document.getElementsByClassName("jobs-search-results jobs-search-results--is-two-pane")[0].setAttribute("id", "scroll")')
            
            #scroll the job list by the height of one job offer to make the next one clickable
            self.driver.execute_script('document.getElementById("scroll").scrollTo( 0, 200*'+ str(i) +')')

    def click_card(self):
            #define header logo
            link_logo = self.driver.find_element_by_class_name('nav-main__inbug-container')
            
            #create an actionchains
            job_card = ActionChains(self.driver)

            #click on the scrolled card using as reference the header logo
            job_card.move_to_element(link_logo).move_by_offset(370 , 230).click().perform()

    def ran(self):
        rnd_time = decimal.Decimal(random.randrange(10000))/2000
        print(str(rnd_time)+"s")
        return rnd_time

    def auto_clicker(self):
        #repeta loop to infinite
        for i in itertools.count():
            #scroll to next & wait to behave like a human
            bot.scroll_next(i)
            sleep(self.ran())
            
            #click on card & wait to behave like a human
            bot.click_card()
            sleep(self.ran())

            #apply to a job
            bot.apply_job()

bot = LinkBot()
bot.login()
bot.input_job()
bot.filter_ea()
sleep(1)
bot.filter_recent()
bot.auto_clicker()
#bot.apply_job()
#bot.scroll_next()
#bot.click_card()
