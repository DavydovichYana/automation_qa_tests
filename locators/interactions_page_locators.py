from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.ID, 'demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    TAB_GRID = (By.ID, 'demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')

class SelectablePageLocators:
    TAB_LIST = (By.ID, 'demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

    TAB_GRID = (By.ID, 'demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')

class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.ID, 'resizableBoxWithRestriction')

    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.ID, 'resizable')

class DroppablePageLocators:
    SIMPLE_TAB = (By.ID, 'droppableExample-tab-simple')
    SIMPLE_DRAG_ME = (By.ID, 'draggable')
    SIMPLE_DROP_ME = (By.ID, 'droppable')

    TAB_ACCEPT = (By.ID, "droppableExample-tab-accept")
    ACCEPT_DRAG_ACCEPTABLE = (By.ID, "acceptable")
    ACCEPT_DRAG_NOT_ACCEPTABLE = (By.ID, "notAcceptable")
    ACCEPT_DROP = (By.CSS_SELECTOR, "#acceptDropContainer #droppable")

    TAB_PREVENT_PROPAGATION = (By.ID, "droppableExample-tab-preventPropogation")
    PREVENT_DRAG = (By.ID, "dragBox")
    PREVENT_INNER_DROP = (By.ID, "notGreedyInnerDropBox")
    PREVENT_INNER_DROP_TEXT = (By.CSS_SELECTOR, "#notGreedyInnerDropBox p:nth-child(1)")
    PREVENT_OUTER_DROP = (By.ID, "notGreedyDropBox")
    PREVENT_OUTER_DROP_TEXT = (By.CSS_SELECTOR, "#notGreedyDropBox p:nth-child(1)")
    PREVENT_INNER_GREEDY_DROP = (By.ID, "greedyDropBoxInner")
    PREVENT_INNER_GREEDY_DROP_TEXT = (By.CSS_SELECTOR, "#greedyDropBoxInner p:nth-child(1)")
    PREVENT_OUTER_GREEDY_DROP = (By.ID, "greedyDropBox")
    PREVENT_OUTER_GREEDY_DROP_TEXT = (By.CSS_SELECTOR, "#greedyDropBox p:nth-child(1)")

    TAB_REVERT = (By.ID, "droppableExample-tab-revertable")
    REVERT_DRAG = (By.ID, "revertable")
    REVERT_NOT_DRAG = (By.ID, "notRevertable")
    REVERT_DROP = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")
    REVERT_DROP_TEXT = (By.CSS_SELECTOR, "#revertableDropContainer #droppable p")
