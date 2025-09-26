import pytest

from pages.widgets_page import AccodianPage


class TestWidgets:

    @pytest.mark.parametrize("accordian_num", ["first", "second", "third"])
    def test_accordian(self,driver,accordian_num):
        accordian_page = AccodianPage(driver, 'https://demoqa.com/accordian')
        accordian_page.open()
        section_title, content = accordian_page.check_accordian(accordian_num)
        if accordian_num == "first":
            assert section_title.text == "What is Lorem Ipsum?" and len(content) == 574, 'Ошибка в первом аккордеоне'
        elif accordian_num == "second":
            assert section_title.text == "Where does it come from?" and len(content) == 763, 'Ошибка во втором аккордеоне'
        else:
            assert section_title.text == "Why do we use it?" and len(content) == 613, 'Ошибка в третьем аккордеоне'

