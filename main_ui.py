# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_v2.0.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(875, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#stackedWidget {\n"
"border-radius: 10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.7875, y1:0.607, x2:0.402, y2:0.373136, stop:0.301136 rgba(59, 130, 246, 255), stop:0.954545 rgba(55, 161, 255, 255));\n"
"}\n"
"#stackedWidget QWidget {\n"
"border-radius: 20px;\n"
"background-color:qlineargradient(spread:pad, x1:0.7875, y1:0.607, x2:0.402, y2:0.373136, stop:0.301136 rgba(59, 130, 246, 255), stop:0.954545 rgba(55, 161, 255, 255));;\n"
"}\n"
"\n"
"#stackedWidget QListWidget {\n"
"border-radius: 10px;\n"
"padding: 0 5px;\n"
"}\n"
"\n"
"#MainWindow {\n"
"    background-color: rgba(59, 130, 246, 255);\n"
"}\n"
"\n"
"#MainWindow QPushButton {\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#full_menu, #icon_menu {\n"
"    background-color:qlineargradient(spread:pad, x1:0.7875, y1:0.607, x2:0.402, y2:0.373136, stop:0.301136 rgba(55, 161, 255, 255), stop:0.954545 rgba(59, 130, 246, 255));\n"
"}\n"
"\n"
"#full_menu QLabel, #icon_menu QLabel {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#full_menu QPushButton, #icon_menu"
                        " QPushButton {\n"
"    border: none;\n"
"    font-weight: 600;\n"
"    color: #333;\n"
"}\n"
"\n"
"#full_menu QPushButton:hover, #icon_menu QPushButton:hover {\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"#full_menu QPushButton:checked {\n"
"    color: #3b82f6;\n"
"    background-color: #ced4da;\n"
"}\n"
"\n"
"#icon_menu QPushButton:checked {\n"
"    background-color: #ced4da;\n"
"}\n"
"\n"
"#header_widget {\n"
"    background-color:qlineargradient(spread:pad, x1:0.7875, y1:0.607, x2:0.402, y2:0.373136, stop:0.301136 rgba(59, 130, 246, 255), stop:0.954545 rgba(55, 161, 255, 255));\n"
"}\n"
"\n"
"#header_widget QLabel {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#header_widget QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"#stackedWidget QListWidget {\n"
"    background-color: #e9ecef;\n"
"    border: none;\n"
"}\n"
"\n"
"#stackedWidget QListWidget::item {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    margin-top: 15px;\n"
"}\n"
"\n"
"#item_list_widget {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"  "
                        "  border: none;\n"
"}\n"
"\n"
"#item_list_widget QWidget {\n"
"    border-radius: 10px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"#item_list_widget QCheckBox {\n"
"    border-radius: 5px;\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"#item_list_widget QCheckBox::indicator {\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    margin: 3px;\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#item_list_widget QCheckBox::indicator:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"#item_list_widget QCheckBox::indicator:checked {\n"
"    image: url(resources/check.svg);\n"
"}\n"
"\n"
"#item_list_widget QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(255, 0, 0, 0.6);\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font-weight: 600;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#item_list_widget QPushButton:hover {\n"
"    background-color: rgba(255, 0, 0, 1);\n"
"}\n"
"\n"
"#task_form {\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"    font-size: 20px;\n"
"    b"
                        "ackground-color: #e9ecef;\n"
"}\n"
"\n"
"#task_form:focus {\n"
"    border: 4px solid rgba(90, 192, 255, 0.4);\n"
"}\n"
"\n"
"#task_submit {\n"
"    background-color:  orange;\n"
"    color: #fff;\n"
"    padding: 7px;\n"
"    font-weight: 600;\n"
"    font-size: 20px;\n"
"	border-radius: 70px;\n"
"}\n"
"\n"
"#task_submit:hover {\n"
"    background-color: orangered;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#error_label {\n"
"    font: 15pt \"Trebuchet MS\";\n"
"    color: rgba(255, 0, 0, 1);\n"
"}\n"
"\n"
"#empty {\n"
"    color: #000;\n"
"    font: 15pt \"Trebuchet MS\";\n"
"    padding: 30px;\n"
"}\n"
"#task_status {\n"
"    font: 12pt \"Trebuchet MS\";\n"
"}\n"
"\n"
"#add_task_widget {\n"
"	background-color:qlineargradient(spread:pad, x1:0.7875, y1:0.607, x2:0.402, y2:0.373136, stop:0.301136 rgba(59, 130, 246, 255), stop:0.954545 rgba(55, 161, 255, 255));\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"	background-color:qlineargradient(spread:pad, x1:0.7875, y1:0.607, x2:0.402, y2:0.373136, stop:0.301136 rgba(59, 130, 246, 255), stop:0.954545 rgba(55, 161, 255, 255));\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 10, 10)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.incomplete_tasks_list_widget = QListWidget(self.page)
        self.incomplete_tasks_list_widget.setObjectName(u"incomplete_tasks_list_widget")

        self.gridLayout.addWidget(self.incomplete_tasks_list_widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.complete_tasks_list_widget = QListWidget(self.page_2)
        self.complete_tasks_list_widget.setObjectName(u"complete_tasks_list_widget")
        self.complete_tasks_list_widget.setWordWrap(True)

        self.gridLayout_5.addWidget(self.complete_tasks_list_widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 2, 0, 1, 1)

        self.header_widget = QWidget(self.widget_2)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 150))
        self.header_widget.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.header_widget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.header = QFrame(self.header_widget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_toggler = QPushButton(self.header)
        self.sidebar_toggler.setObjectName(u"sidebar_toggler")
        icon = QIcon()
        icon.addFile(u":/feather icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sidebar_toggler.setIcon(icon)
        self.sidebar_toggler.setIconSize(QSize(30, 30))
        self.sidebar_toggler.setCheckable(True)
        self.sidebar_toggler.setChecked(True)

        self.horizontalLayout.addWidget(self.sidebar_toggler)

        self.horizontalSpacer_3 = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.logo_3 = QLabel(self.header)
        self.logo_3.setObjectName(u"logo_3")
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setPointSize(30)
        self.logo_3.setFont(font)
        self.logo_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.logo_3)


        self.gridLayout_6.addWidget(self.header, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.header_widget, 0, 0, 1, 1)

        self.add_task_widget = QWidget(self.widget_2)
        self.add_task_widget.setObjectName(u"add_task_widget")
        self.add_task_widget.setMinimumSize(QSize(0, 120))
        self.gridLayout_3 = QGridLayout(self.add_task_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 5, -1, 10)
        self.task_form = QLineEdit(self.add_task_widget)
        self.task_form.setObjectName(u"task_form")
        self.task_form.setMinimumSize(QSize(50, 50))
        self.task_form.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.task_form)

        self.task_submit = QPushButton(self.add_task_widget)
        self.task_submit.setObjectName(u"task_submit")
        icon1 = QIcon()
        icon1.addFile(u":/feather icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.task_submit.setIcon(icon1)
        self.task_submit.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.task_submit)

        self.error_label = QLabel(self.add_task_widget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.error_label)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.add_task_widget, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout_4.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 2, 1, 1)

        self.full_menu = QWidget(self.centralwidget)
        self.full_menu.setObjectName(u"full_menu")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo_2 = QLabel(self.full_menu)
        self.logo_2.setObjectName(u"logo_2")
        font1 = QFont()
        font1.setFamilies([u"Trebuchet MS"])
        font1.setPointSize(40)
        self.logo_2.setFont(font1)
        self.logo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.logo_2)

        self.incomplete_tasks_btn_2 = QPushButton(self.full_menu)
        self.incomplete_tasks_btn_2.setObjectName(u"incomplete_tasks_btn_2")
        self.incomplete_tasks_btn_2.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(13)
        font2.setWeight(QFont.DemiBold)
        self.incomplete_tasks_btn_2.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/feather icons/feather icons/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.incomplete_tasks_btn_2.setIcon(icon2)
        self.incomplete_tasks_btn_2.setIconSize(QSize(20, 20))
        self.incomplete_tasks_btn_2.setCheckable(True)
        self.incomplete_tasks_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.incomplete_tasks_btn_2)

        self.complete_tasks_btn_2 = QPushButton(self.full_menu)
        self.complete_tasks_btn_2.setObjectName(u"complete_tasks_btn_2")
        self.complete_tasks_btn_2.setMinimumSize(QSize(0, 35))
        self.complete_tasks_btn_2.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/feather icons/feather icons/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.complete_tasks_btn_2.setIcon(icon3)
        self.complete_tasks_btn_2.setIconSize(QSize(20, 20))
        self.complete_tasks_btn_2.setCheckable(True)
        self.complete_tasks_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.complete_tasks_btn_2)

        self.line = QFrame(self.full_menu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.add_btn_2 = QPushButton(self.full_menu)
        self.add_btn_2.setObjectName(u"add_btn_2")
        self.add_btn_2.setMinimumSize(QSize(0, 35))
        self.add_btn_2.setFont(font2)
        self.add_btn_2.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/feather icons/feather icons/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn_2.setIcon(icon4)
        self.add_btn_2.setIconSize(QSize(20, 20))
        self.add_btn_2.setCheckable(True)

        self.verticalLayout.addWidget(self.add_btn_2)

        self.task_status = QLabel(self.full_menu)
        self.task_status.setObjectName(u"task_status")
        self.task_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.task_status)

        self.verticalSpacer_2 = QSpacerItem(20, 358, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tasks_clear_2 = QPushButton(self.full_menu)
        self.tasks_clear_2.setObjectName(u"tasks_clear_2")
        self.tasks_clear_2.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        font3.setPointSize(11)
        font3.setWeight(QFont.DemiBold)
        self.tasks_clear_2.setFont(font3)
        self.tasks_clear_2.setStyleSheet(u"#tasks_clear_2:hover {\n"
"background-color: rgba(255, 0, 0, 0.7)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/feather icons/feather icons/x-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tasks_clear_2.setIcon(icon5)
        self.tasks_clear_2.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.tasks_clear_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.gridLayout_2.addWidget(self.full_menu, 0, 1, 1, 1)

        self.icon_menu = QWidget(self.centralwidget)
        self.icon_menu.setObjectName(u"icon_menu")
        self.verticalLayout_5 = QVBoxLayout(self.icon_menu)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.logo_1 = QLabel(self.icon_menu)
        self.logo_1.setObjectName(u"logo_1")
        font4 = QFont()
        font4.setFamilies([u"Trebuchet MS"])
        font4.setPointSize(45)
        self.logo_1.setFont(font4)
        self.logo_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_1.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.logo_1)

        self.verticalSpacer_3 = QSpacerItem(20, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.incomplete_tasks_btn_1 = QPushButton(self.icon_menu)
        self.incomplete_tasks_btn_1.setObjectName(u"incomplete_tasks_btn_1")
        self.incomplete_tasks_btn_1.setMinimumSize(QSize(50, 50))
        self.incomplete_tasks_btn_1.setIcon(icon2)
        self.incomplete_tasks_btn_1.setIconSize(QSize(30, 30))
        self.incomplete_tasks_btn_1.setCheckable(True)
        self.incomplete_tasks_btn_1.setAutoExclusive(True)
        self.incomplete_tasks_btn_1.setAutoRepeatDelay(300)

        self.verticalLayout_2.addWidget(self.incomplete_tasks_btn_1)

        self.complete_tasks_btn_1 = QPushButton(self.icon_menu)
        self.complete_tasks_btn_1.setObjectName(u"complete_tasks_btn_1")
        self.complete_tasks_btn_1.setMinimumSize(QSize(50, 50))
        self.complete_tasks_btn_1.setIcon(icon3)
        self.complete_tasks_btn_1.setIconSize(QSize(30, 30))
        self.complete_tasks_btn_1.setCheckable(True)
        self.complete_tasks_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.complete_tasks_btn_1)

        self.line_2 = QFrame(self.icon_menu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.add_btn_1 = QPushButton(self.icon_menu)
        self.add_btn_1.setObjectName(u"add_btn_1")
        self.add_btn_1.setMinimumSize(QSize(50, 50))
        self.add_btn_1.setStyleSheet(u"")
        self.add_btn_1.setIcon(icon4)
        self.add_btn_1.setIconSize(QSize(30, 30))
        self.add_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.add_btn_1)

        self.verticalSpacer_4 = QSpacerItem(20, 308, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.tasks_clear = QPushButton(self.icon_menu)
        self.tasks_clear.setObjectName(u"tasks_clear")
        self.tasks_clear.setMinimumSize(QSize(50, 50))
        self.tasks_clear.setStyleSheet(u"#tasks_clear:hover {\n"
"background-color: rgba(255, 0, 0, 0.7)\n"
"}")
        self.tasks_clear.setIcon(icon5)
        self.tasks_clear.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.tasks_clear)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addWidget(self.icon_menu, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.add_btn_2.toggled.connect(self.add_btn_1.setChecked)
        self.add_btn_1.toggled.connect(self.add_btn_2.setChecked)
        self.add_btn_2.toggled.connect(self.add_task_widget.setVisible)
        self.add_btn_1.toggled.connect(self.add_task_widget.setVisible)
        self.incomplete_tasks_btn_2.toggled.connect(self.incomplete_tasks_btn_1.setChecked)
        self.incomplete_tasks_btn_1.toggled.connect(self.incomplete_tasks_btn_2.setChecked)
        self.complete_tasks_btn_1.toggled.connect(self.complete_tasks_btn_2.setChecked)
        self.complete_tasks_btn_2.toggled.connect(self.complete_tasks_btn_1.setChecked)
        self.sidebar_toggler.toggled.connect(self.full_menu.setVisible)
        self.sidebar_toggler.toggled.connect(self.icon_menu.setHidden)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sidebar_toggler.setText("")
        self.logo_3.setText(QCoreApplication.translate("MainWindow", u"Incomplete To-dos", None))
        self.task_form.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a new task...", None))
        self.task_submit.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.error_label.setText(QCoreApplication.translate("MainWindow", u"Input field cannot be empty!", None))
        self.logo_2.setText(QCoreApplication.translate("MainWindow", u"NIGEY", None))
        self.incomplete_tasks_btn_2.setText(QCoreApplication.translate("MainWindow", u"INCOMPLETE", None))
        self.complete_tasks_btn_2.setText(QCoreApplication.translate("MainWindow", u"COMPLETED", None))
        self.add_btn_2.setText(QCoreApplication.translate("MainWindow", u"ADD TASK", None))
        self.task_status.setText(QCoreApplication.translate("MainWindow", u"There are currently no tasks", None))
        self.tasks_clear_2.setText(QCoreApplication.translate("MainWindow", u"CLEAR ALL ", None))
        self.logo_1.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.incomplete_tasks_btn_1.setText("")
        self.complete_tasks_btn_1.setText("")
        self.add_btn_1.setText("")
        self.tasks_clear.setText("")
    # retranslateUi

