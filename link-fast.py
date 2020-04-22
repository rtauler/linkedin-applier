from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from time import sleep

import decimal
import random
import itertools    
from selenium.webdriver.common.action_chains import ActionChains

#fake user agent to avoid bot detecting
from fake_useragent import UserAgent

#job appliers
import apply_job
#apply job goes here
#create main class, and import inside the apply job class
class LinkBot(apply_job.Apply):
    def __init__(self):
        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        options.add_argument(f'user-agent={userAgent}')
        options.add_argument("user-data-dir=cookies/rtauler") 
        #keep chrome window open to debug html/css
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=options,service_args=["--verbose", "--log-path=/home/rtauler/linkedin-applier/log.log"])
        self.driver.implicitly_wait(15)

    def ran(self):
        rnd_time = decimal.Decimal(random.randrange(10000))/2500
        print("delayed by "+str(rnd_time)+"s")
        return rnd_time

    def login(self):
        #self.driver.get('https://www.linkedin.com/jobs/')
        print("Entering linkedin")
        sleep(self.ran()) 
    
    def input_job(self):
        job_name = self.driver.find_element_by_css_selector('[aria-label="Buscar empleos"]')
        sleep(self.ran()) 
        job_name.send_keys('Frontend')         
        print('Typed name of job')

        job_name = self.driver.find_element_by_css_selector('[aria-label="Buscar ubicación"]')
        sleep(self.ran()) 
        job_name.send_keys('Barcelona')
        print('Typed location')

        search_btn = self.driver.find_element_by_css_selector('[type="submit"]')
        sleep(self.ran()) 
        search_btn.click()
        print('Clicked Search')

    def filter_ea(self):
        ea_dropdown_btn = self.driver.find_element_by_css_selector('[aria-label="Filtro «Funcionalidades de LinkedIn». Al hacer clic en este botón, se muestran todas las opciones del filtro «Funcionalidades de LinkedIn»."]')
        ea_dropdown_btn.click()
        print('clicked on linkeding functionalities filter')
        sleep(self.ran()) 
        ea_filter_btn = self.driver.find_element_by_css_selector('[for="f_LF-f_AL"]')
        ea_filter_btn.click()
        print('clicked on easy apply only')
        sleep(self.ran()) 

        apply_btn = ActionChains(self.driver)
        apply_btn.move_to_element(ea_filter_btn).move_by_offset(200, 100).click().perform()
        print("Display only easy applies")
        sleep(self.ran()) 

    def filter_recent(self):
        rec_dropdown_btn = self.driver.find_element_by_css_selector('[aria-label="Ordenar por"]')
        rec_dropdown_btn.click()
        print('clicked on sort by dropdown')
        sleep(self.ran())

        rec_filter_btn = self.driver.find_element_by_css_selector('[for="sort-by-date"]')
        rec_filter_btn.click()
        print('clicked on sort by date dropdown')
        sleep(self.ran())

        apply_btn = ActionChains(self.driver)
        apply_btn.move_to_element(rec_filter_btn).move_by_offset(200, 100).click().perform()
        print("Sort by most recent applied")
        sleep(self.ran())

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
            sleep(self.ran())

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
            bot.apply_job(self.driver,sleep)
            

bot = LinkBot()
bot.login()
bot.input_job()
bot.filter_ea()
sleep(self.ran())
bot.filter_recent()
bot.auto_clicker()
sleep(10000000)
#bot.apply_job()
#bot.scroll_next()
#bot.click_card()
