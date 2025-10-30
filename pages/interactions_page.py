import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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

class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        handle = self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE)
        self.go_to_element(handle)
        self.action_drag_and_drop_by_offset(handle,400,200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(handle,-400,-200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        handle = self.element_is_visible(self.locators.RESIZABLE_HANDLE)
        self.go_to_element(handle)
        self.action_drag_and_drop_by_offset(handle,random.randint(0,300),random.randint(0,300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(handle,random.randint(-200,-1),random.randint(-200,-1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP_ME)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPT_DRAG_ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.ACCEPT_DRAG_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.ACCEPT_DROP)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    def drop_prevent(self):
        self.element_is_visible(self.locators.TAB_PREVENT_PROPAGATION).click()
        drag_div = self.element_is_visible(self.locators.PREVENT_DRAG)
        not_greedy_inner_box = self.element_is_visible(self.locators.PREVENT_INNER_DROP)
        greedy_inner_box = self.element_is_visible(self.locators.PREVENT_INNER_GREEDY_DROP)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.PREVENT_OUTER_DROP_TEXT).text
        text_not_greedy_inner_box = self.element_is_visible(self.locators.PREVENT_INNER_DROP_TEXT).text

        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.PREVENT_OUTER_GREEDY_DROP_TEXT).text
        text_greedy_inner_box = self.element_is_visible(self.locators.PREVENT_INNER_GREEDY_DROP_TEXT).text

        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_revert_graggable(self, type_drag):
        drags = {
            'will': {
                'revert': self.locators.REVERT_DRAG,
            },
            'not_will': {
                'revert': self.locators.REVERT_NOT_DRAG,
            }
        }
        self.element_is_visible(self.locators.TAB_REVERT).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.REVERT_DROP)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert











