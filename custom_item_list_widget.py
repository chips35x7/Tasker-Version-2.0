from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QCheckBox,
    QScrollArea,
    QApplication
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from pyinstaller_resource_path import resource_path


class ItemListWidget(QScrollArea):
     def __init__(self, task, status):
        QScrollArea.__init__(self)
        self.setObjectName('item_list_widget')
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        container = QWidget()

        self.item_checkbox = QCheckBox(task)
        self.item_checkbox.setChecked(status)
        self.delete_button = QPushButton('Delete Task')
        self.delete_button.setIcon(QIcon(resource_path('resources/trash-2.svg')))
        self.delete_button.setIconSize(QSize(20, 20))

        layout = QVBoxLayout()
        layout.addWidget(self.item_checkbox)
        layout.addWidget(self.delete_button)
        
        container.setLayout(layout)
        
        self.setWidget(container)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = ItemListWidget('hello', True)
    app.exec()
        