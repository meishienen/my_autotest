from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright,username ,pwd) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://fe-dev.xcool.site2e.cn/
    page.goto("http://fe-dev.xcool.site2e.cn/")

    # Go to http://fe-dev.xcool.site2e.cn/#/
    page.goto("http://fe-dev.xcool.site2e.cn/#/")

    # Go to http://fe-dev.xcool.site2e.cn/#/passport/login
    page.goto("http://fe-dev.xcool.site2e.cn/#/passport/login")

    # Click [placeholder="请输入手机号"]
    page.click("[placeholder=\"请输入手机号\"]")

    # Fill [placeholder="请输入手机号"]
    page.fill("[placeholder=\"请输入手机号\"]", str(username))

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", pwd)

    # Click button:has-text("登录")
    page.click("button:has-text(\"登录\")")

    # Click text=手机号或密码错误
    page.click("text=手机号或密码错误")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", pwd)

    # Click button:has-text("登录")
    # with page.expect_navigation(url="http://fe-dev.xcool.site2e.cn/#/project/folder/all"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=新建动态项目 >> img
    page.click("text=新建动态项目 >> img")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click text=请输入项目名称
    page.click("text=请输入项目名称")

    # Click button:has-text("取消")
    page.click("button:has-text(\"取消\")")

    # Click text=回收站
    page.click("text=回收站")
    # assert page.url == "http://fe-dev.xcool.site2e.cn/#/project/delete"

    # Click text=星标项目
    page.click("text=星标项目")
    # assert page.url == "http://fe-dev.xcool.site2e.cn/#/project/favourite"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright,18731138350,"liu123456")
