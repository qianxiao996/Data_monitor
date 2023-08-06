# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1398, 745)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"C:/Users/19190/.designer/main.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.lineEdit_host = QLineEdit(self.centralwidget)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        self.lineEdit_host.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_15.addWidget(self.lineEdit_host)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_15.addWidget(self.label_6)

        self.lineEdit_port = QLineEdit(self.centralwidget)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_15.addWidget(self.lineEdit_port)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBox)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_15.addWidget(self.label_8)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_table_clear = QPushButton(self.centralwidget)
        self.pushButton_table_clear.setObjectName(u"pushButton_table_clear")

        self.horizontalLayout_4.addWidget(self.pushButton_table_clear)

        self.pushButton_set_hidden = QPushButton(self.centralwidget)
        self.pushButton_set_hidden.setObjectName(u"pushButton_set_hidden")

        self.horizontalLayout_4.addWidget(self.pushButton_set_hidden)

        self.pushButton_data_hidden = QPushButton(self.centralwidget)
        self.pushButton_data_hidden.setObjectName(u"pushButton_data_hidden")

        self.horizontalLayout_4.addWidget(self.pushButton_data_hidden)

        self.pushButton_log_hidden = QPushButton(self.centralwidget)
        self.pushButton_log_hidden.setObjectName(u"pushButton_log_hidden")

        self.horizontalLayout_4.addWidget(self.pushButton_log_hidden)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setEnabled(False)
        self.pushButton_stop.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_stop)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_result = QTableWidget(self.centralwidget)
        if (self.tableWidget_result.columnCount() < 4):
            self.tableWidget_result.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_result.setObjectName(u"tableWidget_result")
        self.tableWidget_result.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_result.setTabKeyNavigation(True)
        self.tableWidget_result.setProperty("showDropIndicator", True)
        self.tableWidget_result.setDragDropOverwriteMode(True)
        self.tableWidget_result.setAlternatingRowColors(False)
        self.tableWidget_result.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_result.setSortingEnabled(False)
        self.tableWidget_result.horizontalHeader().setVisible(True)
        self.tableWidget_result.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_result.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_result.horizontalHeader().setHighlightSections(True)
        self.tableWidget_result.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_result.verticalHeader().setVisible(True)
        self.tableWidget_result.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_result.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_result.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_8.addWidget(self.tableWidget_result)

        self.plainTextEdit_logs = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_logs.setObjectName(u"plainTextEdit_logs")
        self.plainTextEdit_logs.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_logs.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_8.addWidget(self.plainTextEdit_logs)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_17.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_all_data = QRadioButton(self.tab_5)
        self.radioButton_all_data.setObjectName(u"radioButton_all_data")
        self.radioButton_all_data.setMinimumSize(QSize(0, 20))
        self.radioButton_all_data.setChecked(False)

        self.horizontalLayout_9.addWidget(self.radioButton_all_data)

        self.radioButton_post_data = QRadioButton(self.tab_5)
        self.radioButton_post_data.setObjectName(u"radioButton_post_data")
        self.radioButton_post_data.setMinimumSize(QSize(0, 20))
        self.radioButton_post_data.setChecked(True)

        self.horizontalLayout_9.addWidget(self.radioButton_post_data)


        self.gridLayout_6.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.json_data = QLabel(self.tab_5)
        self.json_data.setObjectName(u"json_data")
        self.json_data.setStyleSheet(u"color:red\n"
"")

        self.gridLayout_6.addWidget(self.json_data, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.label_9)

        self.comboBox_type = QComboBox(self.tab_5)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.comboBox_type)


        self.gridLayout_6.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.label_10)

        self.lineEdit_value = QLineEdit(self.tab_5)
        self.lineEdit_value.setObjectName(u"lineEdit_value")
        self.lineEdit_value.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.lineEdit_value)


        self.gridLayout_6.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.tab_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.spinBox_timeout = QSpinBox(self.tab_5)
        self.spinBox_timeout.setObjectName(u"spinBox_timeout")
        self.spinBox_timeout.setMinimumSize(QSize(0, 30))
        self.spinBox_timeout.setValue(10)

        self.horizontalLayout_6.addWidget(self.spinBox_timeout)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox_jiange = QComboBox(self.tab_5)
        self.comboBox_jiange.addItem("")
        self.comboBox_jiange.addItem("")
        self.comboBox_jiange.addItem("")
        self.comboBox_jiange.addItem("")
        self.comboBox_jiange.addItem("")
        self.comboBox_jiange.setObjectName(u"comboBox_jiange")
        self.comboBox_jiange.setMinimumSize(QSize(0, 30))
        self.comboBox_jiange.setEditable(True)

        self.horizontalLayout_5.addWidget(self.comboBox_jiange)

        self.label_4 = QLabel(self.tab_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_7 = QGridLayout(self.tab_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.tab_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(56, 0))

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEdit_webhook = QLineEdit(self.tab_6)
        self.lineEdit_webhook.setObjectName(u"lineEdit_webhook")
        self.lineEdit_webhook.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_webhook)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.tab_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(56, 0))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lineEdit_secret = QLineEdit(self.tab_6)
        self.lineEdit_secret.setObjectName(u"lineEdit_secret")
        self.lineEdit_secret.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_secret)


        self.gridLayout_7.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.tab_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.checkBox_enable = QCheckBox(self.tab_6)
        self.checkBox_enable.setObjectName(u"checkBox_enable")
        self.checkBox_enable.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_14.addWidget(self.checkBox_enable)

        self.pushButton_pipei = QPushButton(self.tab_6)
        self.pushButton_pipei.setObjectName(u"pushButton_pipei")
        self.pushButton_pipei.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_14.addWidget(self.pushButton_pipei)

        self.pushButton_tuisong = QPushButton(self.tab_6)
        self.pushButton_tuisong.setObjectName(u"pushButton_tuisong")
        self.pushButton_tuisong.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_14.addWidget(self.pushButton_tuisong)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.plainTextEdit = QPlainTextEdit(self.tab_6)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 90))

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_17.addWidget(self.tabWidget)


        self.gridLayout_8.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_3.addWidget(self.label)

        self.pushButton_send = QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_send)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tabWidget_source = QTabWidget(self.centralwidget)
        self.tabWidget_source.setObjectName(u"tabWidget_source")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_source = QPlainTextEdit(self.tab)
        self.plainTextEdit_source.setObjectName(u"plainTextEdit_source")
        self.plainTextEdit_source.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.plainTextEdit_source, 0, 0, 1, 1)

        self.tabWidget_source.addTab(self.tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget_source)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.pushButtonx_hidden = QPushButton(self.centralwidget)
        self.pushButtonx_hidden.setObjectName(u"pushButtonx_hidden")
        self.pushButtonx_hidden.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButtonx_hidden)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.tabWidget_result = QTabWidget(self.centralwidget)
        self.tabWidget_result.setObjectName(u"tabWidget_result")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_result = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_result.setObjectName(u"plainTextEdit_result")
        self.plainTextEdit_result.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.plainTextEdit_result, 0, 0, 1, 1)

        self.tabWidget_result.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit_pretty = QTextEdit(self.tab_4)
        self.textEdit_pretty.setObjectName(u"textEdit_pretty")
        self.textEdit_pretty.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.textEdit_pretty, 0, 0, 1, 1)

        self.tabWidget_result.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setEnabled(True)
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.browser = QWebEngineView(self.tab_3)
        self.browser.setObjectName(u"browser")
        self.browser.setMinimumSize(QSize(0, 0))
        self.browser.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.browser, 0, 0, 1, 1)

        self.tabWidget_result.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget_result, 1, 0, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_2)


        self.gridLayout_8.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1398, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_source.setCurrentIndex(0)
        self.tabWidget_result.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u76d1\u63a7\u5de5\u5177  By qianxiao996  v1.3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"HOST", None))
        self.lineEdit_host.setText(QCoreApplication.translate("MainWindow", u"www.baidu.com", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PORT", None))
        self.lineEdit_port.setText(QCoreApplication.translate("MainWindow", u"443", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"https", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u6d4b\u72b6\u6001", None))
        self.pushButton_table_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6570\u636e", None))
        self.pushButton_set_hidden.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pushButton_data_hidden.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e(\u9690\u85cf)", None))
        self.pushButton_log_hidden.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7(\u9690\u85cf)", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u76d1\u6d4b", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u76d1\u6d4b", None))
        ___qtablewidgetitem = self.tableWidget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u54cd\u5e94\u957f\u5ea6", None));
        ___qtablewidgetitem3 = self.tableWidget_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u54cd\u5e94\u72b6\u6001\u7801", None));
        self.plainTextEdit_logs.setPlainText("")
        self.plainTextEdit_logs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u65e5\u5fd7", None))
        self.radioButton_all_data.setText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u6570\u636e", None))
        self.radioButton_post_data.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u8fd4\u56de\u6570\u636e", None))
        self.json_data.setText(QCoreApplication.translate("MainWindow", u"Json\u6570\u636e\u53d8\u5316\u793a\u4f8b:response[key][0]", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u6761\u4ef6", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u957f\u5ea6\u53d1\u751f\u53d8\u5316", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u7801\u53d1\u751f\u53d8\u5316", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5305\u542b\u5173\u952e\u5b57", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6b63\u5219\u5339\u914d", None))
        self.comboBox_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u957f\u5ea6\u5927\u4e8e", None))
        self.comboBox_type.setItemText(5, QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u957f\u5ea6\u5c0f\u4e8e", None))
        self.comboBox_type.setItemText(6, QCoreApplication.translate("MainWindow", u"Json\u6570\u636e\u53d8\u5316", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u6570\u636e", None))
        self.lineEdit_value.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u65f6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u95f4\u9694", None))
        self.comboBox_jiange.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_jiange.setItemText(1, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_jiange.setItemText(2, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox_jiange.setItemText(3, QCoreApplication.translate("MainWindow", u"180", None))
        self.comboBox_jiange.setItemText(4, QCoreApplication.translate("MainWindow", u"300", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Webhook", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Secret", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.checkBox_enable.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528", None))
        self.pushButton_pipei.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u9001\u5339\u914d", None))
        self.pushButton_tuisong.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u9001\u6d4b\u8bd5", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6b64\u5904\u4e3a\u63a8\u9001\u6587\u672c\uff0cjson\u6570\u636e\u53ef\u4f7f\u7528respone['data'][0]\u683c\u5f0f\u53d6\u503c\uff01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Dingtalk Webhook ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Requests", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.plainTextEdit_source.setPlainText(QCoreApplication.translate("MainWindow", u"GET / HTTP/1.1\n"
"Host: www.baidu.com\n"
"Upgrade-Insecure-Requests: 1\n"
"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\n"
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\n"
"Accept-Encoding: gzip, deflate\n"
"Accept-Language: zh-CN,zh;q=0.9,en;q=0.8\n"
"Connection: close\n"
"\n"
"", None))
        self.tabWidget_source.setTabText(self.tabWidget_source.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Raw", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Response", None))
        self.pushButtonx_hidden.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.tabWidget_result.setTabText(self.tabWidget_result.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Raw", None))
        self.tabWidget_result.setTabText(self.tabWidget_result.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Pretty", None))
        self.tabWidget_result.setTabText(self.tabWidget_result.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Render", None))
    # retranslateUi

