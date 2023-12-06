from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Genes whose cDNA/gDNA/protein sequence files I want to download
genes = ["RPL1A","RPL1B","RPL2A","RPL2B","RPL12A","RPL12B","RPL18A","RPL18B","RPL19A","RPL19B",
         "RPL20A","RPL20B","RPL23A","RPL23B","RPL35A","RPL35B","RPL40A","RPL40B","RPL41A","RPL41B",
         "RPL42A","RPL42B","RPL43A","RPL43B","RPS4A","RPS4B","RPS6A","RPS6B","RPS8A","RPS8B","RPS11A",
         "RPS11B","RPS16A","RPS16B","RPS18A","RPS18B","RPS23A","RPS23B","RPS24A","RPS24B","RPS30A",
         "RPS30B"]


baseurl = "https://www.yeastgenome.org/locus/"

gene_urls = [baseurl + gene for gene in genes]

# Messed up on moving files
# genes_A = [gene for gene in genes if "A" in gene]
# gene_A_urls = [baseurl + gene for gene in genes_A]


# Iterate through each gene and get file from web scraping
for url in gene_urls: 
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/scampione/Downloads/",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })

    chrome_options.add_argument("--headless")  # Driver will run silently/in the background
    chrome_options.add_argument("--window-size=1920,1200") 

    # Initialize driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(url)
    time.sleep(6)

    # Go to downloads dropdown menu
    dropdown_button = driver.find_element(By.XPATH, '//a[@class="button dropdown small secondary multi-sequence-download-button"]')
    dropdown_button.click()
    time.sleep(2)

    # Find and click the button for the desired type of sequence data 
    download_links = driver.find_elements(By.XPATH, '//ul[@class="f-dropdown open"]/li')
    link = download_links[0]  # Change index for seq type (genome [0], coding [2], protein [3])
    link.click()
    
    time.sleep(1)

    driver.quit()