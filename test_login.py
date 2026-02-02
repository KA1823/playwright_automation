from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

from login_page import LoginPage

def test_login():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Open your website
        page.goto("https://www.oms.enigmatix.co/login")  # Replace with your URL
        
        # Initialize the Page Object
        login_page = LoginPage(page)
        
        # Perform login
        login_page.login("kamran.anwar86@gmail.com", "Admin@123")
        
        # Optional: Assert successful login
        # Example: check if dashboard is visible
        # expect(page.get_by_text("Muhammad Kamran Anwar")).to_be_visible()
        hea_ding = page.locator("text=Muhammad Kamran Anwar")
        expect(hea_ding).to_be_visible()
        print("Text Found:", hea_ding.text_content())

        # user_label = page.locator("text='Muhammad Kamran Anwar'")
        # user_label.wait_for(timeout=10000)  # Wait for element
        # assert user_label.is_visible(), "Login failed!"
        # assert page.is_visible("text=Muhammad Kamran Anwar"), "Login failed!"
        
        # Close browser
        browser.close()

if __name__ == "__main__":
    test_login()
