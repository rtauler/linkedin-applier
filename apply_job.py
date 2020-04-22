#apply.py

class Apply:
    def apply_job(self,driver,sleep):
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