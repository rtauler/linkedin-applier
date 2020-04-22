from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from time import sleep

#from secrets import username, password
import decimal
import random
from selenium.webdriver.common.action_chains import ActionChains

class LinkBot():
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=cookies/rtauler") 
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=options)
        self.driver.implicitly_wait(15)

    def login(self):
        self.driver.get('https://www.linkedin.com/jobs/')
        print("Entering linkedin")
        sleep(2)
    
    def input_job(self):
        job_name = self.driver.find_element_by_css_selector('[aria-label="Buscar empleos"]')
        job_name.send_keys('Project Manager')         
        print('Typed name of job')

        job_name = self.driver.find_element_by_css_selector('[aria-label="Buscar ubicación"]')
        job_name.send_keys('Barcelona')
        print('Typed location')

        search_btn = self.driver.find_element_by_css_selector('[type="submit"]')
        search_btn.click()
        print('Clicked Search')

    def filter_ea(self):
        dropdown_btn = self.driver.find_element_by_css_selector('[aria-label="Filtro «Funcionalidades de LinkedIn». Al hacer clic en este botón, se muestran todas las opciones del filtro «Funcionalidades de LinkedIn»."]')
        dropdown_btn.click()

        ea_filter_btn = self.driver.find_element_by_css_selector('[for="f_LF-f_AL"]')
        ea_filter_btn.click()

        apply_btn = ActionChains(self.driver)
        apply_btn.move_to_element(ea_filter_btn).move_by_offset(200, 100).click().perform()

    def apply_job(self):
        sleep(2)
        ea_btn = self.driver.find_element_by_css_selector('[data-control-name="jobdetails_topcard_inapply"]')
        ea_btn.click()

        try:
            sleep(1)
            send_ea = self.driver.find_element_by_css_selector('[aria-label="Enviar solicitud"]')
            send_ea.click()
        except Exception:
            try:
                sleep(1)
                next_step = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
                next_step.click()
                sleep(1)
                next_step = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
                next_step.click()
            except Exception:
                step1_txt_input = self.driver.find_element_by_css_selector('[step="1"]')
                step1_txt_input.send_keys('5')
                try:
                    review_btn = self.driver.find_element_by_css_selector('[aria-label="Revisar tu solicitud"]')
                    review_btn.click()

                    not_follow = self.driver.find_element_by_css_selector('[for="follow-company-checkbox"]')
                    not_follow.click()

                    send_ea = self.driver.find_element_by_css_selector('[aria-label="Enviar solicitud"]')
                    send_ea.click()
                except Exception:
                    pass
        
        sleep(1)
        close_ea = self.driver.find_element_by_css_selector('[aria-label="Dismiss"]')
        close_ea.click()
        print('Job applied')

    def hide_job(self):
        sleep(1)
        hide_job = self.driver.find_element_by_css_selector('[aria-label="Ocultar empleo"]')
        hide_job.click()

bot = LinkBot()
bot.login()
bot.input_job()
bot.filter_ea()
bot.apply_job()
bot.hide_job()
