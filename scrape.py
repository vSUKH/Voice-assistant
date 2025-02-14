from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_d809c831-zone-scraping_browser:tuuca35nkbjs'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    print("Launching chrome browser....")

    with Remote(command_executor=SBR_WEBDRIVER, options=ChromeOptions()) as driver:
        driver.get(website)

        print("Waiting for captcha to solve....")
        solve_res = driver.execute_cdp_cmd(
            "Captcha.waitForSolve", {"detectTimeout": 10000}
        )

        print("Captcha solve status:", solve_res.get("status", "Unknown"))
        print("Navigated! Scraping page content....")

        html = driver.page_source
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup.find_all(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
