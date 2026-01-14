import json

from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()

        profile_captured = False   # 👈 guard flag

        def handle_response(response):
            nonlocal profile_captured

            if profile_captured:
                return

            url = response.url.lower()

            if "https://be.oms.enigmatix.co/api/v1/employee/?login=true" in url:
                data = response.json()
                user = data["user"]
                # print("User:", user)

                print("\n--- Full JSON Body ---")
                print(json.dumps(data, indent=4))

                print("\n===== USER INFO FROM API =====")
                print("URL          :", response.url)
                print("Status       :", response.status)
                print("Full Name    :", user["full_name"])
                print("Email        :", user["email"])
                print("Designation  :", data["designation"]["title"])
                # print("Title        :", user["roles"][0]["title"])
                print("Employee ID  :", data["employee_id"])
                print("Availability :", data["availability"])
                print("Branch       :", data["branch_name"])
                print("Is Active    :", data["is_active"])

                profile_captured = True   # 👈 stop future prints

        page.on("response", handle_response)

        # Open login page
        page.goto("https://www.oms.enigmatix.co/login")

        # Login
        page.fill(".ant-input", "kamran.anwar86@gmail.com")
        page.fill("input[type='password']", "Admin@123")
        page.click("button[type='submit']")

        # Wait for dashboard
        page.locator("text=Muhammad Kamran Anwar").wait_for(timeout=15000)

        # Navigate to Employees
        page.locator("a:has-text('Employees')").click()

        page.wait_for_timeout(3000)

        input("\nPress ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    run()
