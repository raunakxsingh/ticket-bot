from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.irctc.co.in/nget/
    page.goto("https://www.irctc.co.in/nget/")

    # Go to https://www.irctc.co.in/nget/train-search
    page.goto("https://www.irctc.co.in/nget/train-search")

    # Click text=OK
    page.click("text=OK")

    # Click input[role="searchbox"]
    page.click("input[role=\"searchbox\"]")

    # Fill input[role="searchbox"]
    page.fill("input[role=\"searchbox\"]", "ltt")

    # Click text=LOKMANYATILAK T - LTT
    page.click("text=LOKMANYATILAK T - LTT")

    # Click [aria-label="Enter To station. Input is Mandatory."] input[role="searchbox"]
    page.click("[aria-label=\"Enter To station. Input is Mandatory.\"] input[role=\"searchbox\"]")

    # Fill [aria-label="Enter To station. Input is Mandatory."] input[role="searchbox"]
    page.fill("[aria-label=\"Enter To station. Input is Mandatory.\"] input[role=\"searchbox\"]", "bsb")

    # Click li[role="option"]:has-text("VARANASI JN - BSB")
    page.click("li[role=\"option\"]:has-text(\"VARANASI JN - BSB\")")

    # Click [aria-label="Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory."] input[type="text"]
    page.click("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]")

    # Press ArrowLeft
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowLeft")

    # Press ArrowRight
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowRight")

    # Fill [aria-label="Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory."] input[type="text"]
    page.fill("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "25/12/2021")

    # Press ArrowLeft
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowLeft")

    # Press ArrowLeft
    page.press("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "ArrowLeft")

    # Fill [aria-label="Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory."] input[type="text"]
    page.fill("[aria-label=\"Enter Journey Date. Formate D.D./.M.M./.Y.Y.Y.Y. Input is Mandatory.\"] input[type=\"text\"]", "21/12/2021")

    # Click text=Search
    # with page.expect_navigation(url="https://www.irctc.co.in/nget/booking/train-list"):
    with page.expect_navigation():
        page.click("text=Search")

    # Click text=AVAILABLE-0023
    page.click("text=AVAILABLE-0023")

    # Click button:has-text("Book Now")
    page.click("button:has-text(\"Book Now\")")

    # Click button:has-text("I Agree")
    page.click("button:has-text(\"I Agree\")")

    # Click [placeholder="User Name"]
    page.click("[placeholder=\"User Name\"]")

    # Fill [placeholder="User Name"]
    page.fill("[placeholder=\"User Name\"]", "Rickytechy")

    # Click [placeholder="Password"]
    page.click("[placeholder=\"Password\"]")

    # Fill [placeholder="Password"]
    page.fill("[placeholder=\"Password\"]", "Raunak01")

    # Click [placeholder="Type Here:"]
    page.click("[placeholder=\"Type Here:\"]")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
