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
            # print(url)

            if "https://be.emp.oms.enigmatix.co/api/v1/employee/all_employees_list/" in url:
                data = response.json()
                # print(data)
                # print(json.dumps(data, indent=4))

                for employee in data:
                    name = employee.get('full_name')
                    if name == "Muhammad Kamran Anwar":
                        print("Name       :", name)
                        print("status     :", employee.get('status'))
                        print("Employee ID:", employee.get("employee_id"))

        page.on("response", handle_response)  

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
        # input("\nPress ENTER to close browser...")
        browser.close()

if __name__ == "__main__":
    run()