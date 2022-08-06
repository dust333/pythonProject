from DR_Pages import DRAuth


def test_auth_fault(browser):
    dr_page = DRAuth(browser)
    dr_page.go_to_site()
    dr_page.enter_number('1001000000')
    dr_page.click_on_login()
    assert dr_page.check_fault()


def test_auth_correct(browser):
    dr_page = DRAuth(browser)
    dr_page.go_to_site()
    dr_page.enter_number('9001002903')
    dr_page.click_on_login()
    assert dr_page.check_code_field()


if __name__ == "__main__":
    test_auth_correct()
    test_auth_fault()