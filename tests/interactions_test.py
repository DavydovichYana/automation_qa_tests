from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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

    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        max_size_resizable_box, min_size_resizable_box = resizable_page.change_size_resizable_box()
        max_size_resizable, min_size_resizable = resizable_page.change_size_resizable()
        assert ('500px', '300px') == max_size_resizable_box, 'Неверный максимальный размер изменяемого окна'
        assert ('150px', '150px') == min_size_resizable_box, 'Неверный минимальный размер изменяемого окна'
        assert max_size_resizable != min_size_resizable, 'Окно не изменилось по размеру'

    def test_drop_simple(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!', 'Элемент не перемещен'

    def test_drop_accept(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        drop_text_not_accept, drop_text_accept = droppable_page.drop_accept()
        assert drop_text_not_accept == 'Drop here' and drop_text_accept == 'Dropped!', 'Элемент не перемещен или ошибка при перемещении'

    def test_drop_prevent(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box = droppable_page.drop_prevent()
        assert text_not_greedy_box == 'Dropped!' and text_not_greedy_inner_box == 'Dropped!', 'Элемент не перемещен или ошибка при перемещении'
        assert text_greedy_box == 'Outer droppable' and text_greedy_inner_box == 'Dropped!', 'Элемент не перемещен или ошибка при перемещении'

    def test_drop_revert(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_graggable('will')
        assert position_after_move != position_after_revert, 'Элемент не вернулся на свое место после перетаскивания'
        position_after_move, position_after_revert = droppable_page.drop_revert_graggable('not_will')
        assert position_after_move == position_after_revert, 'Элемент не остался на месте после перетаскивания'



