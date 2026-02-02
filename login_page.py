from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.email_input = "input[data-testid='email']"  # Replace with your actual selector
        self.password_input = "input[data-testid='password']"
        self.login_button = "button:has-text('LOGIN')"

    def login(self, email: str, password: str):
        # Fill username
        self.page.fill(self.email_input, email)
        # Fill password
        self.page.fill(self.password_input, password)
        # Click login
        self.page.click(self.login_button)
