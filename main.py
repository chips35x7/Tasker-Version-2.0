import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QListWidgetItem
)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from main_ui import Ui_MainWindow
from custom_item_list_widget import ItemListWidget
from database_manager import ToDoDatabase
from pyinstaller_resource_path import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.add_task_widget.hide()
        self.ui.icon_menu.hide()
        self.ui.error_label.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.incomplete_tasks_btn_2.setChecked(True)

        self.database = ToDoDatabase()
        self.tasks = list()
        self.task_statuses = list()
        self.load_data()
        self.check_tasks_count()

        self.setMinimumSize(QSize(800, 500))
        self.setWindowTitle("Nigey's ToDo App")
        # self.setWindowIcon(QIcon(resource_path('tasker.ico')))

        self.ui.task_submit.clicked.connect(self.add_task)
        self.ui.tasks_clear.clicked.connect(self.clear_all_tasks)
        self.ui.tasks_clear_2.clicked.connect(self.clear_all_tasks)
        self.ui.incomplete_tasks_btn_1.clicked.connect(self.show_incomplete_tasks)
        self.ui.incomplete_tasks_btn_2.clicked.connect(self.show_incomplete_tasks)
        self.ui.complete_tasks_btn_1.clicked.connect(self.show_completed_tasks)
        self.ui.complete_tasks_btn_2.clicked.connect(self.show_completed_tasks)

    def load_data(self):
        data = self.database.manager.execute("SELECT tasks, is_complete FROM tasks").fetchall()
        for task, status in data:
            self.tasks.append(task)
            self.task_statuses.append(bool(status))
            widget = self.get_task_widget(bool(status))
            self.add_item(task, widget, bool(status))

    def check_tasks_count(self):
        self.ui.empty.setVisible(not bool(self.tasks))

    def reset_form(self):
        self.ui.add_btn_1.setChecked(False)
        self.ui.add_btn_2.setChecked(False)
        self.ui.task_submit.setChecked(False)
        self.ui.task_form.setText('')

    def add_item(self, task, widget, status=False):
        item = QListWidgetItem()
        item.setSizeHint(QSize(100, 100))
        item_widget = ItemListWidget(task, status)
        widget.addItem(item)
        widget.setItemWidget(item, item_widget)
        item_widget.delete_button.clicked.connect(lambda: self.delete_task(widget, item))
        item_widget.item_checkbox.stateChanged.connect(lambda checked: self.update_task(widget, checked, item))

    def add_task(self):
        task = self.ui.task_form.text()
        if task:
            self.ui.error_label.hide()
            widget = self.get_task_widget(False)
            self.add_item(task, widget, False)
            self.tasks.append(task)
            self.task_statuses.append(False)
            self.database.manager.execute("INSERT INTO tasks (tasks, is_complete) VALUES (?, ?)", (task, 0))
            self.database.connection.commit()
            self.check_tasks_count()
            self.reset_form()
        else:
            self.ui.add_task_widget.setVisible(True)
            self.ui.error_label.setVisible(True)

    def delete_task(self, widget, item):
        row = widget.row(item)
        if 0 <= row < len(self.tasks):
            task = self.tasks[row]
            self.database.manager.execute("DELETE FROM tasks WHERE tasks = ?", (task,))
            self.database.connection.commit()
            widget.takeItem(row)
            self.tasks.pop(row)
            self.task_statuses.pop(row)
            self.check_tasks_count()

    def confirm_clear_all(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Clear All Tasks!')
        msg_box.setText('Are you sure you want to delete all tasks?')
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        return msg_box.exec()
    
    def tasks_cleared_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle('All Tasks Cleared!')
        msg_box.setText('All tasks have been successfully cleared!')
        return msg_box.exec()

    def clear_all_tasks(self):
        if self.confirm_clear_all() == QMessageBox.Yes:
            self.ui.incomplete_tasks_list_widget.clear()
            self.ui.complete_tasks_list_widget.clear()
            self.tasks.clear()
            self.task_statuses.clear()
            self.database.manager.execute("DELETE FROM tasks")
            self.database.connection.commit()
            self.check_tasks_count()
            self.tasks_cleared_message()

    def update_task(self, widget, state, item: QListWidgetItem):
        row = widget.row(item)
        if 0 <= row < len(self.tasks):
            task = self.tasks[row]
            new_status = state == 2

            self.database.manager.execute("UPDATE tasks SET is_complete = ? WHERE tasks = ?", (int(new_status), task))
            self.database.connection.commit()

            widget.takeItem(row)
            self.tasks.pop(row)
            self.task_statuses.pop(row)

            target_widget = self.get_task_widget(new_status)
            self.add_item(task, target_widget, new_status)
            self.tasks.append(task)
            self.task_statuses.append(new_status)

            self.check_tasks_count()

    def get_task_widget(self, status=False):
        return self.ui.complete_tasks_list_widget if status else self.ui.incomplete_tasks_list_widget

    def show_incomplete_tasks(self):
        self.ui.logo_3.setText('Incomplete To-dos')
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_completed_tasks(self):
        self.ui.logo_3.setText('Completed To-dos')
        self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('tasker.ico')))
    with open(resource_path('resources/style.qss')) as file:
        style_sheet = file.read()
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    app.exec()
