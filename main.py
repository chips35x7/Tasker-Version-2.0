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
        self.complete_task_ids = []
        self.incomplete_task_ids = []
        self.load_data()
        self.check_tasks_count()

        self.setMinimumSize(QSize(800, 500))
        self.setWindowTitle("Nigey's ToDo App")

        self.ui.task_submit.clicked.connect(self.add_task)
        self.ui.task_form.returnPressed.connect(self.add_task)
        self.ui.tasks_clear.clicked.connect(self.clear_all_tasks)
        self.ui.tasks_clear_2.clicked.connect(self.clear_all_tasks)
        self.ui.incomplete_tasks_btn_1.clicked.connect(self.show_incomplete_tasks)
        self.ui.incomplete_tasks_btn_2.clicked.connect(self.show_incomplete_tasks)
        self.ui.complete_tasks_btn_1.clicked.connect(self.show_completed_tasks)
        self.ui.complete_tasks_btn_2.clicked.connect(self.show_completed_tasks)

    def load_data(self):
        data = self.database.manager.execute("SELECT * FROM tasks").fetchall()
        for task_id, task, status in data:
            if status:
                self.complete_task_ids.append(task_id)
                widget = self.get_complete_tasks_list_widget(True)
                self.add_item(task, widget, task_id=task_id, status=True)
                continue
            self.incomplete_task_ids.append(task_id)
            widget = self.get_complete_tasks_list_widget(False)
            self.add_item(task, widget, task_id=task_id)

    def check_tasks_count(self):
        if not bool(self.incomplete_task_ids or self.complete_task_ids):
            self.ui.task_status.setText('You currently have no tasks 😕🤷‍♂️')
        elif not self.incomplete_task_ids:
            self.ui.task_status.setText('You have completed all your tasks\nKeep up the good work 👍')
        else:
            self.ui.task_status.setText('You have pending tasks\nGet to work ❗')
    
    def reset_form(self):
        self.ui.add_btn_1.setChecked(False)
        self.ui.add_btn_2.setChecked(False)
        self.ui.task_submit.setChecked(False)
        self.ui.task_form.setText('')

    def add_item(self, task, widget, task_id:int, status=False):
        item = QListWidgetItem()
        item.setSizeHint(QSize(100, 100))
        item_widget = ItemListWidget(task, status)
        widget.addItem(item)
        widget.setItemWidget(item, item_widget)
        item_widget.delete_button.clicked.connect(lambda: self.delete_task(widget, task_id, item))
        item_widget.item_checkbox.stateChanged.connect(lambda checked: self.update_task_status(widget, checked, task_id, item))

    def add_task(self):
        task = self.ui.task_form.text()
        tasks = self.database.manager.execute("SELECT tasks FROM tasks").fetchall()
        tasks_lists = [task[0] for task in tasks]
        if task in tasks_lists:
            if self.duplicate_task_message() == QMessageBox.No:
                return
        
        if task:
            self.ui.error_label.hide()
            self.database.manager.execute("INSERT INTO tasks (tasks, is_complete) VALUES (?, ?)", (task, 0))
            query = self.database.manager.execute("SELECT id FROM tasks").fetchall()
            task_id = query[-1][0]
            widget = self.get_complete_tasks_list_widget(False)
            self.add_item(task, widget, task_id)
            self.incomplete_task_ids.append(task_id)
            self.database.connection.commit()
            self.check_tasks_count()
            self.reset_form()
            return
        self.ui.add_task_widget.setVisible(True)
        self.ui.error_label.setVisible(True)

    def update_task_status(self, widget, state, id:int, item:QListWidgetItem):
        row = widget.row(item)
        task_id = id
        query = self.database.manager.execute("SELECT tasks FROM tasks WHERE id=?", (task_id,)).fetchall()
        task = query[0][0]

        if widget == self.ui.complete_tasks_list_widget:
            self.complete_task_ids.remove(task_id)
            widget.takeItem(row)
            self.incomplete_task_ids.append(task_id)
            self.add_item(task, self.get_complete_tasks_list_widget(False), task_id=task_id)
            self.database.manager.execute("UPDATE tasks SET is_complete = ? WHERE id = ?", (0, task_id))
            self.database.connection.commit()
            self.check_tasks_count()
            return
        self.incomplete_task_ids.remove(task_id)
        widget.takeItem(row)
        self.complete_task_ids.append(task_id)
        self.add_item(task, self.get_complete_tasks_list_widget(True), task_id, True)
        self.database.manager.execute("UPDATE tasks SET is_complete = ? WHERE id = ?", (1, task_id))
        self.database.connection.commit()
        self.check_tasks_count()

    def delete_task(self, widget, id:int, item:QListWidgetItem):
        row = widget.row(item)
        task_id = id

        if widget == self.ui.complete_tasks_list_widget:
            self.complete_task_ids.remove(task_id)
            widget.takeItem(row)
            self.database.manager.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            self.database.connection.commit()
            self.check_tasks_count()
            return
        self.incomplete_task_ids.remove(task_id)
        widget.takeItem(row)
        self.database.manager.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.database.connection.commit()
        self.check_tasks_count()

    def clear_all_tasks(self):
        if self.confirm_clear_all() == QMessageBox.Yes:
            self.ui.incomplete_tasks_list_widget.clear()
            self.ui.complete_tasks_list_widget.clear()
            self.incomplete_task_ids.clear()
            self.complete_task_ids.clear()
            self.database.manager.execute("DELETE FROM tasks")
            self.database.connection.commit()
            self.check_tasks_count()
            self.tasks_cleared_message()

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
    
    def duplicate_task_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Duplicate Task!')
        msg_box.setText('This task already exists!\nAre you sure you want to repeat it again?')
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        return msg_box.exec()

    def get_complete_tasks_list_widget(self, status:bool):
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
    window = MainWindow()
    app.exec()