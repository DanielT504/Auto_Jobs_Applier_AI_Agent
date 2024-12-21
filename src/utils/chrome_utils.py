import os
<<<<<<< HEAD
from selenium import webdriver
from src.logging import logger

chromeProfilePath = os.path.join(os.getcwd(), "chrome_profile", "linkedin_profile")

def ensure_chrome_profile():
    logger.debug(f"Ensuring Chrome profile exists at path: {chromeProfilePath}")
    profile_dir = os.path.dirname(chromeProfilePath)
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
        logger.debug(f"Created directory for Chrome profile: {profile_dir}")
    if not os.path.exists(chromeProfilePath):
        os.makedirs(chromeProfilePath)
        logger.debug(f"Created Chrome profile directory: {chromeProfilePath}")
    return chromeProfilePath

def chrome_browser_options():
    logger.debug("Setting Chrome browser options")
    ensure_chrome_profile()
    options = webdriver.ChromeOptions()
=======
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Import webdriver_manager
import urllib
from src.logging import logger

def chrome_browser_options():
    logger.debug("Setting Chrome browser options")
    options = Options()
>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
<<<<<<< HEAD
    options.add_argument("--disable-gpu")
=======
    options.add_argument("--disable-gpu")  # Opzionale, utile in alcuni ambienti
>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320
    options.add_argument("window-size=1200x800")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-autofill")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-cache")
<<<<<<< HEAD
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    prefs = {
        "profile.default_content_setting_values.images": 2,
        "profile.managed_default_content_settings.stylesheets": 2,
    }
    options.add_experimental_option("prefs", prefs)

    if len(chromeProfilePath) > 0:
        initial_path = os.path.dirname(chromeProfilePath)
        profile_dir = os.path.basename(chromeProfilePath)
        options.add_argument('--user-data-dir=' + initial_path)
        options.add_argument("--profile-directory=" + profile_dir)
        logger.debug(f"Using Chrome profile directory: {chromeProfilePath}")
    else:
        options.add_argument("--incognito")
        logger.debug("Using Chrome in incognito mode")

    return options


=======
    options.add_argument("--incognito")
    options.add_argument("--allow-file-access-from-files")  # Consente l'accesso ai file locali
    options.add_argument("--disable-web-security")         # Disabilita la sicurezza web
    logger.debug("Using Chrome in incognito mode")
    
    return options

def init_browser() -> webdriver.Chrome:
    try:
        options = chrome_browser_options()
        # Use webdriver_manager to handle ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        logger.debug("Chrome browser initialized successfully.")
        return driver
    except Exception as e:
        logger.error(f"Failed to initialize browser: {str(e)}")
        raise RuntimeError(f"Failed to initialize browser: {str(e)}")



def HTML_to_PDF(html_content, driver):
    """
    Converte una stringa HTML in un PDF e restituisce il PDF come stringa base64.

    :param html_content: Stringa contenente il codice HTML da convertire.
    :param driver: Istanza del WebDriver di Selenium.
    :return: Stringa base64 del PDF generato.
    :raises ValueError: Se l'input HTML non è una stringa valida.
    :raises RuntimeError: Se si verifica un'eccezione nel WebDriver.
    """
    # Validazione del contenuto HTML
    if not isinstance(html_content, str) or not html_content.strip():
        raise ValueError("Il contenuto HTML deve essere una stringa non vuota.")

    # Codifica l'HTML in un URL di tipo data
    encoded_html = urllib.parse.quote(html_content)
    data_url = f"data:text/html;charset=utf-8,{encoded_html}"

    try:
        driver.get(data_url)
        # Attendi che la pagina si carichi completamente
        time.sleep(2)  # Potrebbe essere necessario aumentare questo tempo per HTML complessi

        # Esegue il comando CDP per stampare la pagina in PDF
        pdf_base64 = driver.execute_cdp_cmd("Page.printToPDF", {
            "printBackground": True,          # Includi lo sfondo nella stampa
            "landscape": False,               # Stampa in verticale (False per ritratto)
            "paperWidth": 8.27,               # Larghezza del foglio in pollici (A4)
            "paperHeight": 11.69,             # Altezza del foglio in pollici (A4)
            "marginTop": 0.8,                  # Margine superiore in pollici (circa 2 cm)
            "marginBottom": 0.8,               # Margine inferiore in pollici (circa 2 cm)
            "marginLeft": 0.5,                 # Margine sinistro in pollici (circa 1.27 cm)
            "marginRight": 0.5,                # Margine destro in pollici (circa 1.27 cm)
            "displayHeaderFooter": False,      # Non visualizzare intestazioni e piè di pagina
            "preferCSSPageSize": True,         # Preferire le dimensioni della pagina CSS
            "generateDocumentOutline": False,  # Non generare un sommario del documento
            "generateTaggedPDF": False,        # Non generare PDF taggato
            "transferMode": "ReturnAsBase64"   # Restituire il PDF come stringa base64
        })
        return pdf_base64['data']
    except Exception as e:
        logger.error(f"Si è verificata un'eccezione WebDriver: {e}")
        raise RuntimeError(f"Si è verificata un'eccezione WebDriver: {e}")
>>>>>>> cc15a9d1f8869d5ead7f7c45482c7e730699a320
