from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:

    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_order('list')
        grid_before, grid_after = sortable_page.change_order('grid')
        assert list_before != list_after,'Порядок элементов списка не изменился'
        assert grid_before != grid_after, 'Порядок элементов таблицы не изменился'

    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open()
        item_list = selectable_page.select_list_item('list')
        item_grid = selectable_page.select_list_item('grid')
        assert len(item_list) > 0, 'Элемент в списке не выбран'
        assert len(item_grid) > 0, 'Элемент в таблице не выбран'
