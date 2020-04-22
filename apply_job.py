#apply.py

class Apply:
    def next(self,driver,sleep):
        try:
            #jump next step
            next_btn = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
            next_btn.click()
            print('clicked next step')            
            sleep(self.ran())
            try:
                #jump next step
                next_btn = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
                next_btn.click()
                print('clicked next step')
                sleep(self.ran())
                try:
                    #find all text inputs
                    txt_inputs = self.driver.find_elements_by_css_selector('[step="1"]')

                    #iterate through text items, clear them and input a generic '5'
                    for i in range(len(txt_inputs)):
                        txt_inputs[i].clear()
                        txt_inputs[i].send_keys('5')
                        print('filled all inputs with 5')
                        sleep(self.ran())

                    #jump next step
                    next_btn = self.driver.find_element_by_css_selector('[aria-label="Ir al siguiente paso"]')
                    next_btn.click()
                    print('clicked next step')
                    sleep(self.ran())
 
                except Exception:
                    pass

            except Exception:
                pass

        except Exception:
            pass

    def dismiss_job(self,driver,sleep):
        #close popup
        close_ea = self.driver.find_element_by_css_selector('[aria-label="Dismiss"]')
        close_ea.click()
        sleep(self.ran())

        #locate main logo
        link_logo = self.driver.find_element_by_class_name('nav-main__inbug-container')

        #move to logo and click on dismiss
        discard_btn = ActionChains(self.driver)
        discard_btn.move_to_element(link_logo).move_by_offset(600, 330).click().perform()
        sleep(self.ran())


    def apply_job(self,driver,sleep):
            sleep(self.ran())
            try:
                #try to click the easy apply button, if its not there beacuse the job is already applied go to the next
                ea_btn = self.driver.find_element_by_css_selector('[data-control-name="jobdetails_topcard_inapply"]')
                ea_btn.click()
                print('clicked on easy apply btn')
                try:
                    #do not follow company
                    not_follow = self.driver.find_element_by_css_selector('[for="follow-company-checkbox"]')
                    not_follow.click()
                    print('Not follow company')
                    sleep(self.ran())
                    #send appliance
                    send_ea = self.driver.find_element_by_css_selector('[aria-label="Enviar solicitud"]')
                    print('Appliance sent')
                    send_ea.click()
                    #close popup
                    sleep(self.ran())
                    close_ea = self.driver.find_element_by_css_selector('[aria-label="Dismiss"]')
                    close_ea.click()
                    print('Popup closed')
                except Exception:
                    try:
                        self.next(driver,sleep)
                    except Exception:
                        self.dismiss_job(driver,sleep)
            except Exception:
                pass




