#apply.py

class Apply:
    def next(self,driver,sleep):
        try:
            #jump next step
            next_btn = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
            next_btn.click()
            try:
                #jump next step
                next_btn = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
                next_btn.click()
                try:
                    #find all text inputs
                    txt_inputs = self.driver.find_elements_by_css_selector('[step="1"]')

                    #iterate through text items, clear them and input a generic '5'
                    for i in range(len(txt_inputs)):
                        txt_inputs[i].clear()
                        txt_inputs[i].send_keys('5')
 
                except Exception:
                    pass

            except Exception:
                pass

        except Exception:
            pass

    def apply_job(self,driver,sleep):
            sleep(0.1)
            try:
                #try to click the easy apply button, if its not there beacuse the job is already applied go to the next
                ea_btn = self.driver.find_element_by_css_selector('[data-control-name="jobdetails_topcard_inapply"]')
                ea_btn.click()
                try:
                    #do not follow company
                    not_follow = self.driver.find_element_by_css_selector('[for="follow-company-checkbox"]')
                    not_follow.click()
                    sleep(0.1)
                    #send appliance
                    send_ea = self.driver.find_element_by_css_selector('[aria-label="Enviar solicitud"]')
                    send_ea.click()
                    #close popup
                    sleep(0.1)
                    close_ea = self.driver.find_element_by_css_selector('[aria-label="Dismiss"]')
                    close_ea.click()
                    print('Job applied')
                except Exception:
                    try:
                        self.next(driver,sleep)
                    except Exception:
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