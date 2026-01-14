from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Open website
        page.goto("https://www.oms.enigmatix.co/login")

        # Interact with elements
        page.fill(".ant-input", "kamran.anwar86@gmail.com")
        page.fill("input[type='password']", "Admin@123")
        page.click("button[type='submit']")

        page.wait_for_timeout(10000)

        # Wait and validate result
        hea_ding = page.locator("text=Muhammad Kamran Anwar")
        # hea_ding.wait_for(state="visible", timeout=10000)
        expect(hea_ding).to_be_visible()
        print("Text found:", hea_ding.text_content())

        

        # Keep browser open for inspection
        input("Press ENTER to close browser...")

        browser.close()

if __name__ == "__main__":
    run()
