# -*- coding: UTF-8 -*-
import json
import re
import sqlite3
import socket
import ssl

import dingtalkchatbot.chatbot as cb
import sys
import threading, time
import winsound
from http.client import HTTPResponse

import urllib3
from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from playsound import playsound
from ui.main import Ui_MainWindow
from io import BytesIO

DATA_TABLE_NAME = 'data'
CONF_TABLE_NAME = 'conf'


class BytesIOSocket:
    def __init__(self, content):
        self.handle = BytesIO(content)

    def makefile(self, mode):
        return self.handle


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):  # 主窗口
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #去掉标题栏
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.Ui.tabWidget.hide()
        # self.setWindowTitle('数据包监控工具。')
        self.setWindowIcon(QtGui.QIcon('conf/main.ico'))
        self.Ui.pushButton_start.clicked.connect(self.start_task)
        self.Ui.pushButton_stop.clicked.connect(self.stop_task)
        self.Ui.tableWidget_result.clicked.connect(self.change_ui)
        self.Ui.pushButton_table_clear.clicked.connect(self.clear_table)
        self.Ui.tableWidget_result.setColumnWidth(0, 80)
        self.Ui.tableWidget_result.setColumnWidth(1, 200)
        self.Ui.tableWidget_result.setColumnWidth(2, 100)
        self.Ui.tableWidget_result.setColumnWidth(3, 100)
        self.Ui.pushButton_data_hidden.clicked.connect(lambda: self.ui_hide(self.Ui.pushButton_data_hidden, "data"))
        self.Ui.pushButton_set_hidden.clicked.connect(lambda: self.ui_hide(self.Ui.pushButton_set_hidden, "set"))
        self.Ui.pushButton_log_hidden.clicked.connect(lambda: self.ui_hide(self.Ui.pushButton_log_hidden, "log"))
        self.Ui.pushButtonx_hidden.clicked.connect(lambda: self.ui_hide(self.Ui.pushButtonx_hidden, "post"))

        self.Ui.comboBox_type.currentIndexChanged.connect(self.change_comboBox_type)  # comboBox事件选中触发刷新
        self.Ui.pushButton_send.clicked.connect(self.single_send)
        self.Ui.pushButton_tuisong.clicked.connect(lambda: self.dingtalk_rss(''))
        self.Ui.pushButton_pipei.clicked.connect(self.dingtalk_rss_data)
        self.temp_lineEdit_value = ''
        self.Ui.browser.setHtml('')
        self.open_sqlite()
        self.read_data()
        self.chongshicishu = 0

    def open_sqlite(self):
        self.con = sqlite3.connect('conf/data.db')
        try:
            create_data = '''
                        CREATE TABLE IF NOT EXISTS %s
                        (id, time, length,code,content);
                        ''' % (DATA_TABLE_NAME)
            # 主要就是上面的语句
            self.con.execute(create_data)
            create_conf = '''
                        CREATE TABLE IF NOT EXISTS %s
                        (id integer 	PRIMARY KEY AUTOINCREMENT,host,port,is_https,request_text,type,type_value,timeout,jiange,rss_url,rss_secret,rss_enable,rss_text);
                        ''' % (CONF_TABLE_NAME)
            # 主要就是上面的语句
            self.con.execute(create_conf)
        except:
            pass
        self.cur = self.con.cursor()

    def single_send(self):
        try:
            self.Ui.pushButton_send.setEnabled(False)
            obj = Start(self)
            raw_response = obj.start_gogogo("手动")[0]
            if raw_response:
                response = self.response_from_bytes(raw_response)
                try:
                    raw_response_no_encode = raw_response.decode('utf-8', 'ignore').split("\r\n\r\n")[
                                                 0] + "\r\n\r\n" + response.data.decode('utf-8', 'ignore')
                    # print(raw_response_no_encode2)
                    # raw_response_no_encode = raw_response.decode('utf-8','ignore')
                except:
                    try:
                        raw_response_no_encode = raw_response.decode('utf-8', 'ignore')
                    except:
                        raw_response_no_encode = raw_response.decode('raw_unicode_escape', 'ignore')
                self.Ui.plainTextEdit_result.setPlainText(raw_response_no_encode)
                self.Ui.browser.setHtml(raw_response_no_encode)
                try:
                    text = json.loads(response.data.decode('utf-8', 'ignore'))
                    text = json.dumps(text, indent=2, sort_keys=True, ensure_ascii=False)
                    self.Ui.textEdit_pretty.setText(
                        raw_response.decode('utf-8', 'ignore').split("\r\n\r\n")[0] + "\r\n\r\n" + text)
                    # text ="<pre><code>" + text+ "</code></pre>"
                except:
                    self.Ui.plainTextEdit_result.setPlainText(raw_response_no_encode)
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Ui.label_8.setText("[%s][%s]本次运行结束" % (now_time, '手动'))
                self.add_logs("[%s]本次运行结束" % ('手动'))

            self.Ui.pushButton_send.setEnabled(True)
        except:
            self.Ui.pushButton_send.setEnabled(True)
            pass

    def change_comboBox_type(self):
        panduan_type = self.Ui.comboBox_type.currentText()
        if self.temp_lineEdit_value:
            self.Ui.lineEdit_value.setText(self.temp_lineEdit_value)
        else:
            if panduan_type == "Json数据变化":
                self.Ui.lineEdit_value.setText("response")
            elif panduan_type == "返回长度小于" or panduan_type == "返回长度大于":
                self.Ui.lineEdit_value.setText("400")
            else:
                self.Ui.lineEdit_value.setText("")

    def ui_hide(self, sourcde_obj, type):
        text = sourcde_obj.text()
        if "隐藏" in text:
            if type == "data":
                sourcde_obj.setText("显示")
                self.Ui.tabWidget_source.setVisible(False)
                self.Ui.pushButton_send.setVisible(False)
                self.Ui.label.hide()
                self.Ui.tabWidget_result.setVisible(False)
                self.Ui.pushButtonx_hidden.setVisible(False)
                self.Ui.label_7.hide()
            elif type == "set":
                sourcde_obj.setText("设置")
                self.Ui.tabWidget.setVisible(False)
            elif type == "log":
                sourcde_obj.setText("日志")
                self.Ui.plainTextEdit_logs.setVisible(False)
            elif type == "post":
                sourcde_obj.setText("显示")
                self.Ui.tabWidget_source.setVisible(False)
                self.Ui.pushButton_send.setVisible(False)
                self.Ui.label.hide()
            else:
                box = QtWidgets.QMessageBox(window)
                box.warning(self, "警告", "别乱搞，小心爆炸！")
        else:
            if type == "data":
                sourcde_obj.setText("数据(隐藏)")
                self.Ui.tabWidget_source.setVisible(True)
                self.Ui.pushButton_send.setVisible(True)
                self.Ui.label.setVisible(True)
                self.Ui.tabWidget_result.setVisible(True)
                self.Ui.pushButtonx_hidden.setVisible(True)
                self.Ui.label_7.setVisible(True)
            elif type == "set":
                sourcde_obj.setText("设置(隐藏)")
                self.Ui.tabWidget.setVisible(True)
            elif type == "log":
                sourcde_obj.setText("日志(隐藏)")
                self.Ui.plainTextEdit_logs.setVisible(True)
            elif type == "post":
                sourcde_obj.setText("隐藏")
                self.Ui.tabWidget_source.setVisible(True)
                self.Ui.pushButton_send.setVisible(True)
                self.Ui.label.setVisible(True)
            else:
                box = QtWidgets.QMessageBox(window)
                box.warning(self, "警告", "别乱搞，小心爆炸！")

    def clear_table(self):
        for i in range(0, self.Ui.tableWidget_result.rowCount()):  # 循环行
            self.Ui.tableWidget_result.removeRow(0)
        delete_sql = "delete from %s;" % (DATA_TABLE_NAME)
        # print(delete_sql)
        self.sqlite_methods(delete_sql, '', 'exec')
        vacuum_sql = "vacuum;"
        self.sqlite_methods(vacuum_sql, '', 'exec')

    def response_from_bytes(self, raw_response):
        sock = BytesIOSocket(raw_response)
        response = HTTPResponse(sock)
        response.begin()
        return urllib3.HTTPResponse.from_httplib(response)

    def change_ui(self):
        try:
            id = self.Ui.tableWidget_result.selectedItems()[0].text()
            time_ = self.Ui.tableWidget_result.selectedItems()[1].text()

            select_Sql = "select * from %s where id='%s' and time ='%s'" % (DATA_TABLE_NAME, str(id), time_)
            select_Data = self.sqlite_methods(select_Sql, '', 'select')
            text = select_Data[0][-1]
            self.Ui.plainTextEdit_result.setPlainText(text)
            text_list = text.split("\r\n\r\n")
            if len(text_list) >= 2:
                aaa_text = "".join(text_list[1:])
                self.Ui.browser.setHtml(aaa_text)
                try:
                    aaa_text = json.loads(aaa_text)
                    aaa_text = json.dumps(aaa_text, indent=2, sort_keys=True, ensure_ascii=False)
                    self.Ui.textEdit_pretty.setText(text_list[0] + "\r\n\r\n" + aaa_text)
                    # text ="<pre><code>" + text+ "</code></pre>"
                except:
                    self.Ui.textEdit_pretty.setText(text)
                # finally:
                # self.Ui.browser.setHtml(text)
                # self.Ui.browser.load(QUrl(respone_list[1]))
        except Exception as e:
            pass
            # print(str(e))

    def alert(self, dict_data):
        box = QtWidgets.QMessageBox(window)
        if dict_data.get("type") == "warning":
            box.warning(self, dict_data.get("title"), dict_data.get("content"))
        elif dict_data.get("type") == "about":
            box.about(self, dict_data.get("title"), dict_data.get("content"))
        elif dict_data.get("type") == "error":
            box.critical(self, dict_data.get("title"), dict_data.get("content"))
        else:
            box.information(self, dict_data.get("title"), dict_data.get("content"))
        self.add_logs('[弹窗信息] ' + dict_data.get("content"))

    def start_task(self):
        self.Ui.plainTextEdit_logs.clear()
        self.clear_table()
        self.task = Start(self)
        self.task.signal.connect(self.alert)
        self.task.signal_add_table.connect(self.add_table)
        self.Ui.pushButton_start.setEnabled(False)
        self.Ui.pushButton_stop.setEnabled(True)
        self.Ui.label_8.setStyleSheet("color:red")
        self.Ui.label_8.setText("开始监测...")
        self.add_logs("开始监测...")
        self.task.start()

    def stop_task(self):
        self.task.stop_task()

    def sqlite_methods(self, sql, value, type):
        data = ''
        if type == "select":
            self.cur.execute(sql)
            data = self.cur.fetchall()
        elif value:
            self.cur.execute(sql, value)
        else:
            self.cur.execute(sql)

        self.con.commit()

        return data

    def add_table(self, data):
        # print(code)
        row = self.Ui.tableWidget_result.rowCount()  # 获取行数
        # self.Ui.tableWidget_result.setRowCount(row + 1)
        self.Ui.tableWidget_result.insertRow(row)
        item_id = QTableWidgetItem(str(data.get('id')))
        aaa_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        now_time = QTableWidgetItem(aaa_time)
        item_conent = QTableWidgetItem(data.get('content')[:30])
        # item_conent = QTableWidgetItem('1')

        item_length = QTableWidgetItem(str(data.get('length')))
        item_code = QTableWidgetItem(str(data.get('code')))
        # self.Ui.tableWidget_result.setSortingEnabled(False)
        self.Ui.tableWidget_result.setItem(row, 0, item_id)
        self.Ui.tableWidget_result.setItem(row, 1, now_time)
        self.Ui.tableWidget_result.setItem(row, 2, item_length)
        self.Ui.tableWidget_result.setItem(row, 3, item_code)
        self.Ui.tableWidget_result.setItem(row, 4, item_conent)
        self.Ui.tableWidget_result.scrollToBottom()
        insert_sql = 'insert into %s(id, time, length,code,content) values(?,?,?,?,?)' % (DATA_TABLE_NAME)
        value = (str(data.get('id')), aaa_time, str(data.get('length')), data.get('code'), data.get('content'))
        self.sqlite_methods(insert_sql, value, 'insert')
        # 自动调节列宽度
        # self.Mainwi.tableWidget_result.setVisible(False)
        # self.Mainwi.tableWidget_result.resizeColumnToContents(0)
        # self.Mainwi.tableWidget_result.resizeColumnToContents(1)
        # self.Mainwi.tableWidget_result.resizeColumnToContents(2)
        # self.Mainwi.tableWidget_result.resizeColumnToContents(3)
        # self.Mainwi.tableWidget_result.setVisible(True)
        # self.Ui.tableWidget_result.setSortingEnabled(True)

    def closeEvent(self, event):
        try:
            self.save_data()
            self.con.close()
        except Exception as e:

            box = QtWidgets.QMessageBox()
            box.warning(self, "Error！", '数据保存失败！')

    def save_data(self):
        host = self.Ui.lineEdit_host.text()
        port = self.Ui.lineEdit_port.text()

        is_https = self.Ui.checkBox.isChecked()

        request_text = self.Ui.plainTextEdit_source.toPlainText()
        type = self.Ui.comboBox_type.currentText()
        type_value = self.Ui.lineEdit_value.text()
        jiange = (self.Ui.comboBox_jiange.currentText())
        timeout = self.Ui.spinBox_timeout.text()
        rss_url = self.Ui.lineEdit_webhook.text()
        rss_secret = self.Ui.lineEdit_secret.text()
        rss_enable = self.Ui.checkBox_enable.isChecked()
        rss_text = self.Ui.plainTextEdit.toPlainText()

        # f = open('data.json', 'wb')
        # f.write(json.dumps(data, indent=2, sort_keys=True).encode())
        # f.close()
        # print(data)
        delete_sql = "delete from %s;" % (CONF_TABLE_NAME)
        # print(delete_sql)
        self.sqlite_methods(delete_sql, '', 'exec')
        insert_sql = 'insert into %s(host,port,is_https,request_text,type,type_value,timeout,jiange,rss_url,rss_secret,rss_enable,rss_text) values(?,?,?,?,?,?,?,?,?,?,?,?)' % (
            CONF_TABLE_NAME)
        value = (
            host, str(port), is_https, request_text, type, type_value, timeout, jiange, rss_url, rss_secret, rss_enable,
            rss_text)
        self.sqlite_methods(insert_sql, value, 'insert')

    def read_data(self):
        try:
            select_Sql = "select * from %s order by id DESC limit 1;" % (CONF_TABLE_NAME)
            select_Data = self.sqlite_methods(select_Sql, '', 'select')[0]
            # print(select_Data)
            # f = open('data.json', 'rb')
            # data = f.read()
            # f.close()
            # dict_Data = json.loads(data)
            # id  host, port, is_https, request_text, type, type_value, timeout, jiange
            self.Ui.lineEdit_host.setText(select_Data[1])
            self.Ui.lineEdit_port.setText(select_Data[2])
            self.Ui.spinBox_timeout.setValue(int(select_Data[7]))
            self.Ui.lineEdit_value.setText(select_Data[6])
            self.temp_lineEdit_value = select_Data[6]
            self.Ui.plainTextEdit_source.setPlainText(select_Data[4])
            self.Ui.plainTextEdit_source.setPlainText(select_Data[4])
            self.Ui.plainTextEdit_source.setPlainText(select_Data[4])
            self.Ui.lineEdit_webhook.setText(select_Data[9])
            self.Ui.lineEdit_secret.setText(select_Data[10])
            if select_Data[11]:
                self.Ui.checkBox_enable.setChecked(True)
            else:
                self.Ui.checkBox_enable.setChecked(False)

            self.Ui.plainTextEdit.setPlainText(select_Data[12])

            if select_Data[3]:
                self.Ui.checkBox.setChecked(True)
            else:
                self.Ui.checkBox.setChecked(False)

            self.Ui.comboBox_type.setCurrentText(select_Data[5])
        except Exception as e:
            error = str(e) + '----' + str(e.__traceback__.tb_lineno) + '行'
            print(str(error))

    def dingtalk_rss_data(self):
        try:
            id = self.Ui.tableWidget_result.selectedItems()[0].text()
            time_ = self.Ui.tableWidget_result.selectedItems()[1].text()
            select_Sql = "select * from %s where id='%s' and time ='%s'" % (DATA_TABLE_NAME, str(id), time_)
            select_Data = self.sqlite_methods(select_Sql, '', 'select')
            _response = select_Data[0][-1].split("\r\n\r\n")[1]
            text = self.dingtalk_rss_data_replace(_response)
            # print(text)
            self.alert({"type": "info", "title": "推送信息！", "content": text})

        except:
            self.alert({"type": "warning", "title": "Error", "content": "请选中一行数据！"})

    def dingtalk_rss_data_replace(self, _response):
        text = self.Ui.plainTextEdit.toPlainText()
        try:
            response = json.loads(_response)
        except:
            response=''
            # self.alert({"type":"warning","title":"Error","content":"json数据解析失败，本次停止推送！"})
            # return
        re_list = re.findall(r'{{(.*?)}}', text)
        for single_bianliang in re_list:
            try:
                aaaa = eval(single_bianliang)
                text = text.replace("{{" + single_bianliang + "}}", str(aaaa))
            except Exception as e:
                print(str(e))
                text = text.replace("{{" + single_bianliang + "}}", "{{" + single_bianliang + "变量获取失败}}")
        return text

    def dingtalk_rss(self, _response):
        try:
            if not _response:
                try:
                    id = self.Ui.tableWidget_result.selectedItems()[0].text()
                except:
                    id = 1
                try:
                    time_ = self.Ui.tableWidget_result.selectedItems()[1].text()
                except:
                    time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                select_Sql = "select * from %s where id='%s' and time ='%s'" % (DATA_TABLE_NAME, str(id), time_)
                select_Data = self.sqlite_methods(select_Sql, '', 'select')
                if len(select_Data) > 0:
                    _response = select_Data[0][-1].split("\r\n\r\n")[1]
                else:
                    _response = ''

            text = self.Ui.plainTextEdit.toPlainText()
            if self.Ui.comboBox_type.currentText() == 'Json数据变化':
                try:
                    text = self.dingtalk_rss_data_replace(_response)
                except Exception as e:
                    pass
            self.dingtalk_rss_send(text)
        except Exception as e:
            error = str(e) + '----' + str(e.__traceback__.tb_lineno) + '行'
            self.Ui.label_8.setText(str(error))
            self.add_logs(str(error))

    def dingtalk_rss_send(self, text):
        try:
            webhook = self.Ui.lineEdit_webhook.text()
            secret = self.Ui.lineEdit_secret.text()
            ding = cb.DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            info = '''%s''' % ('[' + str(now_time) + ' 监控提示]\n' + text)
            success = ding.send_text(msg=info, is_at_all=False)
            if success['errmsg'] == 'ok' or success['errcode'] == 0:
                self.Ui.label_8.setStyleSheet("color:green")
                self.Ui.label_8.setText("钉钉推送成功")
                self.add_logs(str("钉钉推送成功"))
            else:
                self.Ui.label_8.setStyleSheet("color:red")
                self.Ui.label_8.setText(str(success))
                self.add_logs(str(success))
        except Exception as  e:
            box = QtWidgets.QMessageBox(window)
            box.warning(self, "钉钉推送失败", str(e))

    def add_logs(self, logs):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # set the cursor position to 0
        cursor = QTextCursor(self.Ui.plainTextEdit_logs.document())
        # set the cursor position (defaults to 0 so this is redundant)
        cursor.setPosition(0)
        self.Ui.plainTextEdit_logs.setTextCursor(cursor)
        # insert text at the cursor
        self.Ui.plainTextEdit_logs.insertPlainText("[%s] %s\n" % (now_time, logs))
        # self.Ui.plainTextEdit_logs.appendPlainText("【%s】 %s"%(now_time,logs))
class Start(QThread):
    signal = Signal(dict)  # 更新弹窗
    signal_add_table = Signal(dict)  # 更新弹窗

    def __init__(self, Main, stop_flag=0, parent=None):
        super(Start, self).__init__(parent)
        self.Mainwi = Main.Ui
        self.Windows = Main
        self.stop_flag = stop_flag
        self.last_len = ''
        self.last_code = ''
        self.last_json = ''
        self.alert_json = 1

    def get_jiange(self):
        try:
            jiange = int(self.Mainwi.comboBox_jiange.currentText())
            return jiange
        except:
            self.signal.emit({"type": "warning", "title": "警告！", "content": "请输入正确的间隔时间!"})
            return None

    def get_host_port(self):
        try:
            host = self.Mainwi.lineEdit_host.text()
            port = int(self.Mainwi.lineEdit_port.text())
            return host, port
        except:
            self.signal.emit({"type": "warning", "title": "警告！", "content": "请输入正确的HOST和PORT!"})
            return None, None

    def run(self):
        thread = threading.Thread(target=self.start_jiance, args=())
        thread.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
        thread.start()

    def start_jiance(self):
        if self.Mainwi.checkBox_enable.isChecked():
            self.Windows.dingtalk_rss_send('开始监测...')
        id = 1
        while not self.stop_flag:
            response, error = self.start_gogogo(id)
            # print(response)
            if response:
                self.return_result(response, id)
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.Mainwi.label_8.setStyleSheet("color:green")
                self.Mainwi.label_8.setText("[%s][%s]本次运行结束" % (now_time, id))
                self.Windows.add_logs("[%s]本次运行结束" % (id))
                self.Windows.chongshicishu = 0
                time_jiange = int(self.Mainwi.comboBox_jiange.currentText())
                time.sleep(time_jiange)
                id += 1
            else:
                self.Windows.chongshicishu += 1
                if self.Windows.chongshicishu >= 3:
                    self.signal.emit({"type": "warning", "title": "提示！", "content": "数据返回失败，请检查！\n【错误信息】:\n" + error})
                    self.stop_task("【发生内部错误】:\n。" + error)
                # self.signal.emit({"type": "warning", "title": "警告！", "content": "响应数据为空！停止运行！"})
                # self.stop_task('响应数据为空！停止运行！')

    def start_gogogo(self, id):
        jiange = self.get_jiange()
        host, port = self.get_host_port()
        request_text = self.Mainwi.plainTextEdit_source.toPlainText()
        if jiange and host and port:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.Mainwi.label_8.setStyleSheet("color:blue")
            self.Mainwi.label_8.setText("[%s][%s]已发送请求，等待响应..." % (now_time, id))
            self.Windows.add_logs("[%s]已发送请求，等待响应..." % (id))
            is_https = self.Mainwi.checkBox.isChecked()
            try:
                if is_https:
                    sock = ssl.wrap_socket(socket.socket(), cert_reqs=ssl.CERT_NONE)
                else:
                    sock = socket.socket()  # 建立socket
                timeout = 20
                try:
                    timeout = int(self.Mainwi.spinBox_timeout.text())
                except:
                    self.signal.emit({"type": "warning", "title": "警告！", "content": "超时时间设置错误！"})
                    self.stop_task('超时时间设置错误')
                sock.settimeout(timeout)
                sock.connect((host, port))  # 远程连接
                sock.send(request_text.encode())  # 向socket发送数据
                response = b''
                chunk = sock.recv(4096)  # 从socket接收数据
                while chunk:
                    response += chunk
                    chunk = sock.recv(4096)
                self.Mainwi.label_8.setText("[%s][%s]获取响应成功!" % (now_time, id))
                self.Windows.add_logs(str("[%s]获取响应成功!" % (id)))

                return response, ''
            except Exception as e:
                error = str(e) + '----' + str(e.__traceback__.tb_lineno) + '行'
                # self.signal.emit({"type": "warning", "title": "提示！", "content": "数据返回失败，请检查！【错误信息】:\n" + error})
                return None, error
        else:
            self.stop_task('参数设置错误！')
            return None

    def return_result(self, raw_response, id):
        # print(raw_response.decode())
        if raw_response:
            response = self.response_from_bytes(raw_response)
            try:
                raw_response_no_encode = raw_response.decode('utf-8', 'ignore').split("\r\n\r\n")[
                                             0] + "\r\n\r\n" + response.data.decode('utf-8', 'ignore')
                # print(raw_response_no_encode2)
                # raw_response_no_encode = raw_response.decode('utf-8','ignore')
            except:
                try:
                    raw_response_no_encode = raw_response.decode('utf-8', 'ignore')
                except:
                    raw_response_no_encode = raw_response.decode('raw_unicode_escape', 'ignore')
            _response = ''
            if self.Mainwi.radioButton_all_data.isChecked():
                _response = raw_response_no_encode

            elif self.Mainwi.radioButton_post_data.isChecked():
                _response = response.data.decode('utf-8', 'ignore')
            else:
                _response = raw_response_no_encode

            self.signal_add_table.emit(
                {"id": id, "content": raw_response_no_encode, "length": len(_response), "code": response.status})

            # print(response.headers['Content-Length'])
            # print(response.data.decode())
            panduan_type = self.Mainwi.comboBox_type.currentText()
            panduan_value = self.Mainwi.lineEdit_value.text()

            if panduan_type == "长度发生变化":
                if self.last_len and self.last_len != len(_response):
                    self.last_len = len(_response)
                    self.dingdingding(str(id), _response)
                else:
                    self.last_len = len(_response)
            elif panduan_type == "状态码发生变化":
                if self.last_code and response.status != self.last_code:
                    self.last_code = response.status
                    self.dingdingding(str(id), _response)
                else:
                    self.last_code = response.status

            elif panduan_type == "数据包含关键字":
                # print(response.data)
                if panduan_value in _response:
                    self.dingdingding(str(id), _response)
            elif panduan_type == "数据正则匹配":
                match_Result = re.findall(panduan_value, _response)
                if match_Result:
                    self.dingdingding(str(id), _response)


            elif panduan_type == "返回长度大于":
                try:
                    num = int(panduan_value)
                    if len(_response) > num:
                        self.dingdingding(str(id), _response)
                except:
                    self.signal.emit({"type": "info", "title": "提示！", "content": "请输入一个数字!"})
                    return
            elif panduan_type == "返回长度小于":
                try:
                    num = int(panduan_value)
                    if len(_response) < num:
                        self.dingdingding(str(id), _response)
                except:
                    self.signal.emit({"type": "warning", "title": "提示！", "content": "请输入一个数字!"})
                    return
            elif panduan_type == "Json数据变化":
                if not self.Mainwi.radioButton_post_data.isChecked():
                    self.signal.emit({"type": "warning", "title": "提示！", "content": "此判断条件仅限“仅返回数据”选项!"})
                    self.stop_task('此判断条件仅限“仅返回数据”选项!')
                else:
                    try:
                        response = json.loads(_response)
                    except Exception as  e:
                        error = str(e) + '----' + str(e.__traceback__.tb_lineno) + '行'
                        print(error)
                        self.signal.emit({"type": "warning", "title": "提示！", "content": "json数据解析失败!"})
                        self.stop_task("json数据解析失败!")

                        return
                    try:
                        match_data = (eval(panduan_value))
                        match_data = str(match_data)
                        if self.alert_json:
                            if len(match_data) > 200:
                                alert_match_data = match_data[:200] + '...'
                            else:
                                alert_match_data = match_data
                            self.signal.emit(
                                {"type": "success", "title": "Success！",
                                 "content": "数据匹配成功！匹配结果:\n" + alert_match_data})
                            self.alert_json = 0
                        if self.last_json and self.last_json != match_data:
                            self.last_json = match_data
                            self.dingdingding(str(id), _response)
                        else:
                            self.last_json = match_data
                    except Exception as  e:
                        self.signal.emit({"type": "warning", "title": "提示！", "content": "数据匹配失败!"})
                        error = str(e) + '----' + str(e.__traceback__.tb_lineno) + '行'
                        self.stop_task("数据匹配失败!")
                        print(error)
            else:
                self.signal.emit({"type": "warning", "title": "提示！", "content": "请选择匹配规则!"})
        else:
            self.signal.emit({"type": "warning", "title": "警告！", "content": "返回数据为空!"})

    def dingdingding(self, id, _response):
        try:
            self.signal.emit({"type": "info", "title": "提示！", "content": "匹配成功,数据包编号:" + str(id)})
            if self.Mainwi.checkBox_enable.isChecked():
                self.Windows.dingtalk_rss(_response)
        except Exception as  e:
            print(str(e))
        try:
            playsound('conf/a.mp3', True)
        except Exception as  e:
            try:
                playsound('conf/b.mp3', True)
            except Exception as  e:
                winsound.Beep(800, 800)
            # self.alert({"type": "warning", "title": "警告！", "content": "音频文件不存在或被损坏!"})

    def response_from_bytes(self, raw_response):
        sock = BytesIOSocket(raw_response)
        response = HTTPResponse(sock)
        response.begin()
        return urllib3.HTTPResponse.from_httplib(response)

    def stop_task(self, stop_info=''):
        self.stop_flag = 1
        self.Mainwi.pushButton_start.setEnabled(True)
        self.Mainwi.pushButton_stop.setEnabled(False)
        self.Mainwi.label_8.setStyleSheet("color:red")
        self.Mainwi.label_8.setText("停止监测！")
        if stop_info:
            self.Windows.add_logs("停止监测，异常信息:\n" + stop_info)
            if self.Mainwi.checkBox_enable.isChecked():
                self.Windows.dingtalk_rss_send(stop_info)
        else:
            self.Windows.add_logs("停止监测")
            if self.Mainwi.checkBox_enable.isChecked():
                self.Windows.dingtalk_rss_send('停止监测')


# 读取方法
class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, "r", encoding='utf-8') as f:
            return f.read()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    # styleFile = './Qss/mac.qss'
    # qssStyle = CommonHelper.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    # qr = window.frameGeometry()
    # cp = QDesktopWidget().availableGeometry().center()
    # qr.moveCenter(cp)
    # window.move(qr.topLeft())
    sys.exit(app.exec())
