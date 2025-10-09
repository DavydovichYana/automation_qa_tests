import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_order(self, tab):
        tabs = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'item': self.locators.LIST_ITEM,
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'item': self.locators.GRID_ITEM,
            }
        }
        self.element_is_visible(tabs[tab]['tab']).click()
        order_before = self.get_sortable_items(tabs[tab]['item'])
        item_list = random.sample(self.elements_are_visible(tabs[tab]['item']), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(tabs[tab]['item'])
        print(order_before, order_after)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self, tab):
        tabs = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'item': self.locators.LIST_ITEM,
                'item_active': self.locators.LIST_ITEM_ACTIVE,
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'item': self.locators.GRID_ITEM,
                'item_active': self.locators.GRID_ITEM_ACTIVE,
            }
        }
        self.element_is_visible(tabs[tab]['tab']).click()
        self.click_selectable_items(tabs[tab]['item'])
        active_element = self.element_is_visible(tabs[tab]['item_active']).text
        return active_element



