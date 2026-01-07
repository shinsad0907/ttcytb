import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTreeWidget, QTreeWidgetItem, QTextEdit, QGroupBox,
                             QMessageBox, QSplitter)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QColor
from datetime import datetime
import requests
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


class YTB:
    def __init__(self, cookie: str, authorization: str):
        self.cookies = {}
        for item in cookie.split(";"):
            key, value = item.strip().split("=", 1)
            self.cookies[key] = value

        self.headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'authorization': authorization,
            'content-type': 'application/json',
            'origin': 'https://www.youtube.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        }

    def getdata(self, url: str):
        re = requests.get(url, cookies=self.cookies, headers=self.headers).text
        try:
            self.pageid = re.split('"DELEGATED_SESSION_ID":"')[1].split('"')[0]
        except:
            self.pageid = False
        
        self.visitorid = re.split('"VISITOR_DATA":"')[1].split('"')[0]
        try:
            self.chanelid = re.split('"channelId":"')[1].split('"')[0]
        except:
            self.chanelid = ''
        return self.pageid, self.visitorid, self.chanelid

    def follow(self, url: str):
        headers = self.headers.copy()
        pageid, visitorid, chanelid = self.getdata(url)
        if not pageid:
            headers['x-goog-visitor-id'] = visitorid
        else:
            headers['x-goog-visitor-id'] = visitorid
            headers['x-goog-pageid'] = pageid

        params = {'prettyPrint': 'false'}
        json_data = {
            'context': {'client': {'clientName': 'WEB', 'clientVersion': '2.20260105.01.00'}},
            'channelIds': [chanelid],
            'params': 'EgIIAhgA',
        }

        response = requests.post(
            'https://www.youtube.com/youtubei/v1/subscription/subscribe',
            params=params,
            cookies=self.cookies,
            headers=headers,
            json=json_data,
        ).json()
        return response


class WorkerThread(QThread):
    log_signal = pyqtSignal(str, str, str)  # status, message, detail
    finished_signal = pyqtSignal()
    
    def __init__(self, cookie, authorization):
        super().__init__()
        self.cookie = cookie
        self.authorization = authorization
        self.running = True
        self.index_job = 0
        self.index_button = 1
        self.idpost = ''
        
        self.cookies = {
            '_fbp': 'fb.1.1761508765559.516195470818743635',
            'PHPSESSID': 'dlr4jh5pvm9s4tkb9h39a7m4s0',
            '_gid': 'GA1.2.242056569.1767635360',
        }
        
        self.headers = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://tuongtaccheo.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }

    def wait_and_click(self, locator, driver, timeout=60):
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.click()
        sleep(random.uniform(1, 2))

    def getcoin(self, idpost):
        print(f'Gửi idpost: {idpost}')
        data = {'id': idpost}
        response = requests.post(
            'https://tuongtaccheo.com/youtube/kiemtien/subcheo/nhantien.php',
            cookies=self.cookies,
            headers=self.headers,
            data=data,
        ).json()
        return response

    def run(self):
        try:
            self.log_signal.emit("INFO", "Khởi tạo trình duyệt...", "")
            
            options = Options()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            
            driver.get("https://tuongtaccheo.com/youtube/kiemtien/subcheo/")
            self.log_signal.emit("INFO", "Đã mở TuongTacCheo", "Vui lòng đăng nhập thủ công")
            
            # Chờ user đăng nhập
            time.sleep(30)
            
            wait = WebDriverWait(driver, 15)
            main_tab = driver.current_window_handle
            old_tabs = driver.window_handles
            
            while self.running:
                try:
                    button = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div/div/div/div[{self.index_button}]/div/div/button')
                    onclick_value = button.get_attribute('onclick')
                    
                    match = re.search(r"like\('([^']+)','([^']+)'\)", onclick_value)
                    if not match:
                        continue
                        
                    job_id = match.group(1)
                    youtube_url = match.group(2)
                    
                    self.log_signal.emit("INFO", f"Job #{self.index_job + 1}", youtube_url)
                    
                    # Click button
                    self.wait_and_click(f'/html/body/div/div/div[3]/div/div/div/div[{self.index_button}]/div/div/button', driver)
                    
                    # Đợi tab mới
                    wait.until(lambda d: len(d.window_handles) > len(old_tabs))
                    new_tab = [t for t in driver.window_handles if t not in old_tabs][0]
                    
                    # Chuyển qua tab mới và đóng
                    driver.switch_to.window(new_tab)
                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(main_tab)
                    time.sleep(3)
                    
                    # Follow YouTube
                    ytb = YTB(self.cookie, self.authorization)
                    ytb.follow(youtube_url)
                    
                    self.log_signal.emit("SUCCESS", f"Đã follow job {job_id}", "")
                    sleep(10)
                    self.idpost += f'{job_id},'
                    self.index_job += 1
                    self.index_button += 1
                    
                    # Nhận coin sau 4 jobs
                    if self.index_job == 4:
                        idpost = self.idpost.rstrip(',')
                        self.log_signal.emit("INFO", "Đang nhận coin...", idpost)
                        
                        result = self.getcoin(idpost)
                        self.log_signal.emit("SUCCESS", "Đã nhận coin", str(result))
                        
                        self.index_job = 0
                        self.idpost = ''
                    
                    sleep(5)
                    
                except Exception as e:
                    self.log_signal.emit("ERROR", "Lỗi xử lý job", str(e))
                    sleep(5)
                    
        except Exception as e:
            self.log_signal.emit("ERROR", "Lỗi nghiêm trọng", str(e))
        finally:
            try:
                driver.quit()
            except:
                pass
            self.finished_signal.emit()

    def stop(self):
        self.running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("YouTube Auto Sub Tool - TuongTacCheo")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QLabel {
                color: #cdd6f4;
                font-size: 12px;
            }
            QLineEdit, QTextEdit {
                background-color: #313244;
                color: #cdd6f4;
                border: 2px solid #45475a;
                border-radius: 5px;
                padding: 8px;
                font-size: 12px;
            }
            QLineEdit:focus, QTextEdit:focus {
                border: 2px solid #89b4fa;
            }
            QPushButton {
                background-color: #89b4fa;
                color: #1e1e2e;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #74c7ec;
            }
            QPushButton:pressed {
                background-color: #89dceb;
            }
            QPushButton:disabled {
                background-color: #45475a;
                color: #6c7086;
            }
            QGroupBox {
                color: #cdd6f4;
                border: 2px solid #45475a;
                border-radius: 5px;
                margin-top: 10px;
                font-weight: bold;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QTreeWidget {
                background-color: #313244;
                color: #cdd6f4;
                border: 2px solid #45475a;
                border-radius: 5px;
                font-size: 12px;
            }
            QTreeWidget::item:selected {
                background-color: #585b70;
            }
            QHeaderView::section {
                background-color: #45475a;
                color: #cdd6f4;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("🎥 YouTube Auto Subscribe Tool")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #89b4fa; padding: 10px;")
        main_layout.addWidget(title)
        
        # Input Group
        input_group = QGroupBox("🔑 Cấu Hình YouTube")
        input_layout = QVBoxLayout()
        
        # Cookie input
        cookie_layout = QHBoxLayout()
        cookie_label = QLabel("Cookie:")
        cookie_label.setMinimumWidth(100)
        self.cookie_input = QLineEdit()
        self.cookie_input.setPlaceholderText("Nhập cookie YouTube...")
        cookie_layout.addWidget(cookie_label)
        cookie_layout.addWidget(self.cookie_input)
        input_layout.addLayout(cookie_layout)
        
        # Authorization input
        auth_layout = QHBoxLayout()
        auth_label = QLabel("Authorization:")
        auth_label.setMinimumWidth(100)
        self.auth_input = QLineEdit()
        self.auth_input.setPlaceholderText("Nhập authorization YouTube...")
        auth_layout.addWidget(auth_label)
        auth_layout.addWidget(self.auth_input)
        input_layout.addLayout(auth_layout)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)
        
        # Control Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.start_btn = QPushButton("▶️ Bắt Đầu")
        self.start_btn.clicked.connect(self.start_automation)
        self.start_btn.setMinimumHeight(40)
        
        self.stop_btn = QPushButton("⏹️ Dừng Lại")
        self.stop_btn.clicked.connect(self.stop_automation)
        self.stop_btn.setEnabled(False)
        self.stop_btn.setMinimumHeight(40)
        self.stop_btn.setStyleSheet("""
            QPushButton {
                background-color: #f38ba8;
            }
            QPushButton:hover {
                background-color: #eba0ac;
            }
        """)
        
        self.clear_btn = QPushButton("🗑️ Xóa Log")
        self.clear_btn.clicked.connect(self.clear_logs)
        self.clear_btn.setMinimumHeight(40)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #fab387;
            }
            QPushButton:hover {
                background-color: #f9e2af;
            }
        """)
        
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        button_layout.addWidget(self.clear_btn)
        main_layout.addLayout(button_layout)
        
        # Log TreeView
        log_group = QGroupBox("📋 Nhật Ký Hoạt Động")
        log_layout = QVBoxLayout()
        
        self.log_tree = QTreeWidget()
        self.log_tree.setHeaderLabels(["Thời Gian", "Trạng Thái", "Thông Báo", "Chi Tiết"])
        self.log_tree.setColumnWidth(0, 150)
        self.log_tree.setColumnWidth(1, 100)
        self.log_tree.setColumnWidth(2, 300)
        self.log_tree.setAlternatingRowColors(True)
        
        log_layout.addWidget(self.log_tree)
        log_group.setLayout(log_layout)
        main_layout.addWidget(log_group)
        
        # Status Bar
        self.statusBar().setStyleSheet("""
            QStatusBar {
                background-color: #313244;
                color: #cdd6f4;
                border-top: 2px solid #45475a;
            }
        """)
        self.statusBar().showMessage("⏸️ Sẵn sàng")
    
    def add_log(self, status, message, detail):
        timestamp = datetime.now().strftime("%H:%M:%S")
        item = QTreeWidgetItem([timestamp, status, message, detail])
        
        # Set colors based on status
        if status == "SUCCESS":
            item.setForeground(1, QColor("#a6e3a1"))
        elif status == "ERROR":
            item.setForeground(1, QColor("#f38ba8"))
        elif status == "INFO":
            item.setForeground(1, QColor("#89b4fa"))
        else:
            item.setForeground(1, QColor("#cdd6f4"))
        
        self.log_tree.addTopLevelItem(item)
        self.log_tree.scrollToBottom()
    
    def start_automation(self):
        cookie = self.cookie_input.text().strip()
        auth = self.auth_input.text().strip()
        
        if not cookie or not auth:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ Cookie và Authorization!")
            return
        
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.cookie_input.setEnabled(False)
        self.auth_input.setEnabled(False)
        self.statusBar().showMessage("▶️ Đang chạy...")
        
        self.add_log("INFO", "Bắt đầu tự động hóa", f"Cookie: {cookie[:50]}...")
        
        self.worker = WorkerThread(cookie, auth)
        self.worker.log_signal.connect(self.add_log)
        self.worker.finished_signal.connect(self.on_finished)
        self.worker.start()
    
    def stop_automation(self):
        if self.worker:
            self.worker.stop()
            self.add_log("INFO", "Đang dừng...", "Chờ hoàn tất công việc hiện tại")
    
    def on_finished(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.cookie_input.setEnabled(True)
        self.auth_input.setEnabled(True)
        self.statusBar().showMessage("⏹️ Đã dừng")
        self.add_log("INFO", "Đã dừng tự động hóa", "")
    
    def clear_logs(self):
        self.log_tree.clear()
        self.add_log("INFO", "Đã xóa log", "")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())