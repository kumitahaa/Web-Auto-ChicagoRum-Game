# ------------- Import -------------
from selenium import webdriver
import time,yaml, random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = ""
break_interval = random.randrange(start=10,stop=60)
print(f"Will take a break after {break_interval} minutes... :)")
its_break_time = time.time() + 60 * break_interval
city_count = 2
theft_city = 2 # For selecting the city to Steal Car from
oc_time = time.time()


def init():
    global driver
    driver = webdriver.Chrome()


def add_extension(api_key):
    global driver
    options = Options()
    options.add_extension('CaptchaAI-Captcha-Solver.crx')
    driver = webdriver.Chrome(options=options)
    api_url = "chrome-extension://fnnmnnfpdnlkccecmiicejhimhkbolhk/options/options.html"
    driver.get(api_url)
    api(api_key)
    print("Extension Added...")
    print("="*50)


def api(api_key = "13cecaa0db7f9439a9fceef518b9c15d"):
    time.sleep(5)
    try:
        api_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
    "/html/body/div/div/table/tbody/tr[1]/td[2]/div/input")))
        login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
    "/html/body/div/div/table/tbody/tr[1]/td[3]/div/button")))
        time.sleep(4)
        api_input.send_keys(api_key)
        time.sleep(4)
        login_btn.click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
    except:
        print(f"Error in API Key")
        time.sleep(10)

def start():
    # ------------------- Opening WebPage ----------------------------------
    url = "https://www.chicagorum.com/"
    driver.get(url)
    print("Opened webpage...")
    print("="*50)


def login(username, password):
    # ---------------------------- Login User -----------------------------------
    try:
        user_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div/form/input[1]")))
        password_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div/form/input[2]")
        login_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div/form/div[3]/button")
        user_input.send_keys(username)
        password_input.send_keys(password)
        login_btn.click()
        print("Logged In...")
        print("="*50)
    except:
            print(f"Couldn't Find Login Fields..   :/   :(")
            print("=" * 50)
            login()

def play_game(crime_check_box = 9, oc = 3, oc_plan = 1):
    # ----------------------- Main Control Loop --------------------------
    global its_break_time
    global break_interval
    while (True):
        time_now = time.time()
        if time_now > its_break_time:
            take_break_for = random.randrange(start=5,stop=20)
            print(f"{break_interval} Minutes Passed... Taking Break for {take_break_for} minutes...")
            print("=" * 50)
            time.sleep(60 * take_break_for)
            print("Let's Continue...")
            print("=" * 50)
            break_interval = random.randrange(start=10,stop=60)
            print(f"Will take a break after {break_interval} minutes...")
            print("=" * 50)
            its_break_time = time.time() + 60 * break_interval
        captcha_check()
        try:
            crime_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerCrimes")))
            gta_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerGta")))
            travel_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerTravel")))
            organize_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerOC")))
            # ------------------------ Check for Car Theft --------------------------------
            if gta_time.text == "00:00":
                gta_commit()
            # -------------------------- Check for Crime -----------------------------------
            if crime_time.text == "00:00":
                crime_commit(crime_check_box)
            # -------------------------- Check for OC -----------------------------------
            if organize_time.text == "00:00:00":
                organize_crime(oc,oc_plan)
            # -------------------------- Check for Travel -----------------------------------
            if travel_time.text == "00:00:00":
                travel_commit()
        except:
            play_game(crime_check_box, oc, oc_plan)


def organize_crime(oc = 3, oc_plan=1):
    global oc_time
    # -------------------- OC ------------------
    if time.time() > oc_time:
        try:
            organize_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerOC")))
            time.sleep(4)
            organize_tab.click()
        except:
            print(f"Couldn't Find Organize Crime Tab..   :/   :(")
            print("=" * 50)
            captcha_check()
        try:
            rest_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerOC")))   
            if rest_time.text == "00:00:00":
                try:
                    myOC = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                        By.CLASS_NAME, f"cinematic{str(oc)}")))
                    start_btn = driver.find_element(By.ID, "mcTitle")
                    time.sleep(4)
                    myOC.click()
                    time.sleep(4)
                    start_btn.click()
                    print("OC Started...")
                    print("=" * 50)
                except:
                    print("Can't Get OC, Going Forward...")
                    print("="*50)
                try:
                    master_mind = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 
                    "percent1")))
                    safe_expert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 
                    "percent2")))
                    weapon_experts = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 
                    "percent3")))
                    getaway_driver = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 
                    "percent4")))
                    set_percent_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                        By.CLASS_NAME, "btnLoad")))
                    time.sleep(4)
                    master_mind.send_keys("20")
                    time.sleep(4)
                    safe_expert.send_keys("5")
                    time.sleep(4)
                    weapon_experts.send_keys("15")
                    time.sleep(4)
                    getaway_driver.send_keys("60")
                    time.sleep(4)
                    set_percent_btn.click()
                    print("OC details added....")
                    print("="*50)
                except:
                    print(f"Can't Get Percentages, Going Forward...")
                    print("=" * 50)
                try:
                    yellow_card = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 
                    "yellowCard")))
                    time.sleep(4)
                    yellow_card.click()
                    print("Yellow Card Clicked....")
                    time.sleep(4)
                    try:
                        choose_plan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 
                        f"eq{str(oc_plan)}")))
                        choose_plan.click()
                        print("A Plan Choosen....")
                        time.sleep(4)
                    except:
                        print(f"Choose Plan not available.... :)")
                        print("=" * 50)
                    try:
                        finish_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 
                        "/html/body/div[1]/div/div[6]/div[2]/div[4]/form/table/tbody/tr[7]/td/button")))
                        finish_btn.click()
                        print("Finish OC button clicked...")
                        time.sleep(4)
                        # after clicking Finish if it still appears
                        finish_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 
                        "/html/body/div[1]/div/div[6]/div[2]/div[4]/form/table/tbody/tr[7]/td/button")))
                        print("You can't afford this plan... Going for basic plan.") #if finish appears still
                        print("=" * 50)
                        organize_crime(oc) # Go to basic plan
                    except:
                        print(f"Plan {oc_plan} Choosen.... :)")
                        print("=" * 50)
                except:
                    print(f"Can't Find Yellow Card...   :/   :(")
                    print("=" * 50)
                    captcha_check()
                try:
                    blueCard = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 
                    "blueCard")))
                    time.sleep(4)
                    blueCard.click()
                    print("Blue Card Found, Clicked....")
                    print("=" * 50)
                    time.sleep(4)
                    try:
                        mass_advertise_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 
                        "/html/body/div[1]/div/div[6]/div[2]/div[3]/form/table/tbody/tr[3]/td/button")))
                        mass_advertise_btn.click()
                        print("Mass Advertise Clicked.....")
                        print("=" * 50)
                    except:
                        print("Mass Advertise Not Found....")
                        print("=" * 50)
                except:
                    print(f"Can't Find Blue Card...   :/   :(")
                    print("=" * 50)
                    captcha_check()
        except:
            print(f"Can't Find OC ticker Clock..   :/   :(")
            print("=" * 50)
            captcha_check()
        oc_time = time.time() + 120 * 60
        print("OC Time updated... Will Check OC after 120 minutes.....")
        print("=" * 50)


def travel_commit():
    global city_count # City to steal car from
    # -------------------- GTA ------------------
    try:
        travel_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerTravel")))
        time.sleep(4)
        travel_tab.click()
    except:
        print(f"Couldn't Find Travel Tab..   :/   :(")
        print("=" * 50)
        captcha_check()
    try:
        rest_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerTravel")))   
        if rest_time.text == "00:00:00":
            try:
                city = driver.find_element(By.CLASS_NAME, f"cinematic{str(city_count)}")
                if city_count == 5:
                    city_count = 1
                else:
                    city_count = city_count + 1
                submit_btn = driver.find_element(By.ID, "submit")
                time.sleep(4)
                city.click()
                time.sleep(4)
                submit_btn.click()
                print("Travel Completed...")
                print("=" * 50)
            except:
                print(f"Couldn't Find City to Travel..   :/   :(")
                print("=" * 50)
                captcha_check()
    except:
        print(f"Couldn't Find Travel Ticker Clock..   :/   :(")
        print("=" * 50)
        captcha_check()


def gta_commit():
    global theft_city # City to steal car from
    # -------------------- GTA ------------------
    try:    
        gta_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerGta")))
        time.sleep(4)
        gta_tab.click()
    except:
        print(f"Couldn't Find GTA Tab..   :/   :(")
        print("=" * 50)
        captcha_check()
    try:
        rest_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerGta")))   
        if rest_time.text == "00:00":
            print(f"Clicking on: city{str(theft_city)}")
            try:
                city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, f"city{str(theft_city)}")))
                if theft_city == 3:
                    theft_city = 1
                else:
                    theft_city = theft_city + 1
                submit_btn = driver.find_element(By.ID, "gta_submit")
                time.sleep(4)
                city.click()
                time.sleep(4)
                submit_btn.click()
                print("Car Theft Committed...")
                print("=" * 50)
            except:
                print(f"Can't Click GTA city..   :/   :(")
                print("=" * 50)
                captcha_check()
    except:
        print(f"Couldn't Find GTA Ticker Clock..   :/   :(")
        print("=" * 50)
        captcha_check()


def crime_commit(crime_check_box = 9):
    # ---------------- Commiting a Crime ---------------------
    try:    
        crime_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerCrimes")))
        time.sleep(4)
        crime_tab.click()
    except:
        print(f"Can't find Crime tab..   :/   :(")
        print("=" * 50)
        captcha_check()
    try:
        rest_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tickerCrimes"))        )
        if rest_time.text == "00:00":
            try:
                check_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, f"textland{str(crime_check_box)}")))
                submit_btn = driver.find_element(By.ID, "crime_submit")
                time.sleep(4)
                check_box.click()
                time.sleep(4)
                submit_btn.click()
                print("Crime Committed...")
                print("=" * 50)
            except:
                print(f"Can't Find Crime to Commit..   :/   :(")
                print("=" * 50)
                captcha_check()
    except:
        print(f"Can't Find Crime Ticker Clock..   :/   :(")
        print("=" * 50)
        captcha_check()


def captcha_check():
    try:
        bot_verify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "h-captcha")))
        print("Captcha Appeared, Waiting for 150 Seconds...")
        print("=" * 50)
        time.sleep(150)
        captcha_check()
    except:
        pass


def load_config(file_path = "config.yaml"):
    # --------------------- Getting User Input Details --------------------------------
    with open (file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def driver():
    # ------------------ Driver Function ---------------------
    crime_check_box = 9
    config = load_config()
    user = config.get("user", None)
    password = config.get("password", None)
    crime_check_box = config.get("crime_check_box", None)
    oc = config.get("oc", None)
    oc_plan = config.get("oc_plan", None)
    with_extension = config.get("with_extension", None)
    api_key = config.get("api_key", None)
    print(f"""
    User:   "{user}"  ... 
    Password:   "{password}"  ...
    Crime Check Box: "{crime_check_box}"
    Oragnized Crime: "{oc}"
    OC Plan: "{oc_plan}"
    With Extension: "{with_extension}"
""")
    print("=" * 50)
    if (with_extension.lower() == "true"):
        add_extension(api_key)  # Before start() funciton    
    else:
        init()
    time.sleep(4)
    start()
    login(user, password)
    time.sleep(4)
    play_game(crime_check_box,oc,oc_plan)
    # organize_crime(oc,oc_plan)
    print("Out of Main Loop")
    print("=" * 50)
    time.sleep(50)

# -------------- Driver Call --------------
driver()