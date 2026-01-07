import sys
import json
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTabWidget, QTreeWidget, QTreeWidgetItem,
                             QPushButton, QMenu, QAction, QDialog, QFormLayout,
                             QLineEdit, QLabel, QSpinBox, QGroupBox, QFileDialog,
                             QMessageBox, QCheckBox, QTextEdit, QToolBar, QFrame,
                             QHeaderView, QSplitter, QDoubleSpinBox, QScrollArea,
                             QGridLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize, QTimer
from PyQt5.QtGui import QIcon, QFont, QColor, QPalette


class SettingsDialog(QDialog):
    def __init__(self, current_settings=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("⚙ Cài Đặt Hiển Thị")
        self.setMinimumWidth(500)
        self.setMinimumHeight(350)
        self.current_settings = current_settings or {'tabs_per_row': 3, 'rows_count': 2}
        self.setup_ui()
        self.apply_styles()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(25, 25, 25, 25)
        
        title = QLabel("Cấu Hình Hiển Thị Chrome")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #00bcd4;")
        
        grid_group = QGroupBox("Bố Cục Chrome Trên Màn Hình")
        grid_layout = QFormLayout()
        grid_layout.setSpacing(15)
        
        self.tabs_per_row = QSpinBox()
        self.tabs_per_row.setMinimum(1)
        self.tabs_per_row.setMaximum(10)
        self.tabs_per_row.setValue(self.current_settings['tabs_per_row'])
        self.tabs_per_row.setMinimumHeight(35)
        
        self.rows_count = QSpinBox()
        self.rows_count.setMinimum(1)
        self.rows_count.setMaximum(10)
        self.rows_count.setValue(self.current_settings['rows_count'])
        self.rows_count.setMinimumHeight(35)
        
        grid_layout.addRow("Số Chrome trên 1 hàng:", self.tabs_per_row)
        grid_layout.addRow("Số hàng hiển thị:", self.rows_count)
        grid_group.setLayout(grid_layout)
        
        btn_layout = QHBoxLayout()
        self.btn_save = QPushButton("💾 Lưu Cài Đặt")
        self.btn_save.setMinimumHeight(40)
        self.btn_cancel = QPushButton("✖ Hủy")
        self.btn_cancel.setMinimumHeight(40)
        
        self.btn_save.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)
        
        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_save)
        
        layout.addWidget(title)
        layout.addWidget(grid_group)
        layout.addStretch()
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        
    def apply_styles(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QGroupBox {
                font-weight: 600;
                border: 2px solid #424242;
                border-radius: 8px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: #2d2d2d;
                color: #00bcd4;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px;
            }
            QSpinBox {
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 8px;
                background-color: #2d2d2d;
                color: #e0e0e0;
            }
            QSpinBox:focus {
                border: 2px solid #00bcd4;
            }
            QPushButton {
                background-color: #00bcd4;
                color: #1e1e1e;
                border: none;
                padding: 10px 25px;
                border-radius: 6px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #00acc1;
            }
        """)
        
    def get_settings(self):
        return {
            'tabs_per_row': self.tabs_per_row.value(),
            'rows_count': self.rows_count.value()
        }


class AddAccountDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("➕ Thêm Tài Khoản")
        self.setMinimumWidth(600)
        self.setMinimumHeight(450)
        self.setup_ui()
        self.apply_styles()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)
        
        title = QLabel("Thêm Tài Khoản Hàng Loạt")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #00bcd4;")
        
        instructions = QLabel("📋 Nhập theo định dạng: email|password (mỗi tài khoản 1 dòng)")
        instructions.setStyleSheet("""
            color: #b0b0b0;
            padding: 10px;
            background-color: #2d2d2d;
            border-left: 4px solid #00bcd4;
            border-radius: 4px;
        """)
        
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText(
            "example1@gmail.com|password123\n"
            "example2@gmail.com|mypass456"
        )
        self.text_input.setMinimumHeight(200)
        
        btn_layout = QHBoxLayout()
        self.btn_ok = QPushButton("✔ Thêm Tài Khoản")
        self.btn_ok.setMinimumHeight(45)
        self.btn_cancel = QPushButton("✖ Hủy")
        self.btn_cancel.setMinimumHeight(45)
        
        self.btn_ok.clicked.connect(self.validate_and_accept)
        self.btn_cancel.clicked.connect(self.reject)
        
        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_ok)
        
        layout.addWidget(title)
        layout.addWidget(instructions)
        layout.addWidget(self.text_input)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        
    def apply_styles(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QTextEdit {
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 12px;
                font-family: 'Consolas', 'Courier New', monospace;
                background-color: #2d2d2d;
                color: #e0e0e0;
            }
            QTextEdit:focus {
                border: 2px solid #00bcd4;
            }
            QPushButton {
                background-color: #00bcd4;
                color: #1e1e1e;
                border: none;
                padding: 12px 30px;
                border-radius: 6px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #00acc1;
            }
        """)
        
    def validate_and_accept(self):
        text = self.text_input.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập ít nhất 1 tài khoản!")
            return
            
        lines = text.split('\n')
        valid_count = sum(1 for line in lines if '|' in line)
                
        if valid_count == 0:
            QMessageBox.warning(self, "Cảnh báo", "Không có tài khoản hợp lệ!")
            return
            
        self.accept()
        
    def get_accounts(self):
        text = self.text_input.toPlainText().strip()
        accounts = []
        
        for line in text.split('\n'):
            line = line.strip()
            if '|' in line:
                parts = line.split('|')
                if len(parts) >= 2:
                    email = parts[0].strip()
                    password = parts[1].strip()
                    username = email.split('@')[0]
                    
                    accounts.append({
                        'user': username,
                        'mail': email,
                        'password': password,
                        'cookie': '',
                        'authorization': ''
                    })
        
        return accounts


class AddTTCAccountDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("➕ Thêm TK TuongTacCheo")
        self.setMinimumWidth(600)
        self.setMinimumHeight(450)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)
        
        title = QLabel("Thêm Tài Khoản TuongTacCheo")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #ff9800;")
        
        instructions = QLabel("📋 Định dạng: user|password|cookie (mỗi tài khoản 1 dòng)")
        instructions.setStyleSheet("""
            color: #b0b0b0;
            padding: 10px;
            background-color: #2d2d2d;
            border-left: 4px solid #ff9800;
        """)
        
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText(
            "user123|password123|cookie_value_xxx\n"
            "user456|password456|cookie_value_yyy"
        )
        self.text_input.setMinimumHeight(200)
        self.text_input.setStyleSheet("""
            QTextEdit {
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 12px;
                font-family: 'Consolas';
                background-color: #2d2d2d;
                color: #e0e0e0;
            }
            QTextEdit:focus {
                border: 2px solid #ff9800;
            }
        """)
        
        btn_layout = QHBoxLayout()
        self.btn_ok = QPushButton("✔ Thêm")
        self.btn_ok.setMinimumHeight(45)
        self.btn_cancel = QPushButton("✖ Hủy")
        self.btn_cancel.setMinimumHeight(45)
        
        self.btn_ok.clicked.connect(self.validate_and_accept)
        self.btn_cancel.clicked.connect(self.reject)
        
        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_ok)
        
        layout.addWidget(title)
        layout.addWidget(instructions)
        layout.addWidget(self.text_input)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QPushButton {
                background-color: #ff9800;
                color: #1e1e1e;
                border: none;
                padding: 12px 30px;
                border-radius: 6px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #f57c00;
            }
        """)
        
    def validate_and_accept(self):
        text = self.text_input.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập ít nhất 1 tài khoản!")
            return
        
        valid = sum(1 for line in text.split('\n') if line.count('|') >= 2)
        if valid == 0:
            QMessageBox.warning(self, "Cảnh báo", "Định dạng không hợp lệ!")
            return
            
        self.accept()
        
    def get_accounts(self):
        text = self.text_input.toPlainText().strip()
        accounts = []
        
        for line in text.split('\n'):
            line = line.strip()
            if line.count('|') >= 2:
                parts = line.split('|')
                accounts.append({
                    'user': parts[0].strip(),
                    'password': parts[1].strip(),
                    'cookie': parts[2].strip(),
                    'balance': 0,
                    'status': 'Chờ'
                })
        
        return accounts


class YouTubeManagerTab(QWidget):
    def __init__(self):
        super().__init__()
        self.accounts = []
        self.profile_path = ""
        self.data_file = "youtube_accounts.json"
        self.settings = {'tabs_per_row': 3, 'rows_count': 2}
        self.setup_ui()
        self.load_accounts()
        self.load_settings()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Toolbar
        toolbar = QWidget()
        toolbar.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1a1a1a, stop:1 #2d2d2d);
                border-bottom: 2px solid #00bcd4;
            }
        """)
        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(20, 15, 20, 15)
        
        title = QLabel("🎬 YouTube Manager")
        title.setStyleSheet("color: #00bcd4; font-size: 20px; font-weight: bold;")
        
        self.btn_select_profile = QPushButton("📁 Chọn Profile")
        self.btn_select_profile.setMinimumHeight(40)
        self.btn_select_profile.clicked.connect(self.select_profile_path)
        
        self.btn_settings = QPushButton("⚙ Settings")
        self.btn_settings.setMinimumHeight(40)
        self.btn_settings.clicked.connect(self.show_settings)
        
        for btn in [self.btn_select_profile, self.btn_settings]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #00bcd4;
                    color: #1e1e1e;
                    border: none;
                    padding: 8px 20px;
                    border-radius: 6px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #00acc1;
                }
            """)
        
        toolbar_layout.addWidget(title)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.btn_select_profile)
        toolbar_layout.addWidget(self.btn_settings)
        toolbar.setLayout(toolbar_layout)
        
        # Info panel
        info_widget = QWidget()
        info_layout = QHBoxLayout()
        info_layout.setContentsMargins(20, 10, 20, 10)
        
        self.profile_label = QLabel("📂 Profile: Chưa chọn")
        self.account_count_label = QLabel("👤 Tài khoản: 0")
        
        for lbl in [self.profile_label, self.account_count_label]:
            lbl.setStyleSheet("""
                color: #00bcd4;
                font-weight: 600;
                padding: 5px 15px;
                background-color: #2d2d2d;
                border-radius: 6px;
            """)
        
        info_layout.addWidget(self.profile_label)
        info_layout.addStretch()
        info_layout.addWidget(self.account_count_label)
        info_widget.setLayout(info_layout)
        info_widget.setStyleSheet("background-color: #1e1e1e;")
        
        # TreeView
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(['☑', 'STT', 'Username', 'Email', 'Password', 
                                   'Cookie', 'Authorization', 'Mở Chrome', 'Hành Động'])
        
        header = self.tree.header()
        header.setSectionResizeMode(QHeaderView.Interactive)
        widths = [50, 60, 130, 180, 110, 150, 150, 120, 140]
        for i, w in enumerate(widths):
            self.tree.setColumnWidth(i, w)
        
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.show_context_menu)
        self.tree.setAlternatingRowColors(True)
        self.tree.setSelectionMode(QTreeWidget.ExtendedSelection)
        
        main_layout.addWidget(toolbar)
        main_layout.addWidget(info_widget)
        main_layout.addWidget(self.tree)
        
        self.setLayout(main_layout)
        self.apply_tree_styles()
        
    def apply_tree_styles(self):
        self.tree.setStyleSheet("""
            QTreeWidget {
                border: none;
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
                outline: none;
            }
            QTreeWidget::item {
                padding: 8px 5px;
                border-bottom: 1px solid #2d2d2d;
            }
            QTreeWidget::item:hover {
                background-color: #2d2d2d;
            }
            QTreeWidget::item:selected {
                background-color: #00bcd4;
                color: #1e1e1e;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #00bcd4;
                padding: 10px;
                border: none;
                border-right: 1px solid #424242;
                font-weight: 600;
            }
        """)
        
    def select_profile_path(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Chọn Profile Folder")
        if dir_path:
            self.profile_path = dir_path
            self.profile_label.setText(f"📂 Profile: {os.path.basename(dir_path)}")
            
    def show_settings(self):
        dialog = SettingsDialog(self.settings, self)
        if dialog.exec_():
            self.settings = dialog.get_settings()
            self.save_settings()
            QMessageBox.information(self, "Thành công", "Đã lưu cài đặt!")
            
    def show_context_menu(self, position):
        menu = QMenu()
        menu.setStyleSheet("""
            QMenu {
                background-color: #2d2d2d;
                border: 2px solid #424242;
                border-radius: 6px;
                color: #e0e0e0;
            }
            QMenu::item {
                padding: 10px 30px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #00bcd4;
                color: #1e1e1e;
            }
        """)
        
        add_action = QAction("➕ Thêm Tài Khoản", self)
        add_action.triggered.connect(self.add_accounts)
        menu.addAction(add_action)
        
        selected = self.tree.selectedItems()
        if selected:
            menu.addSeparator()
            delete_action = QAction("🗑 Xóa", self)
            delete_action.triggered.connect(self.delete_selected)
            menu.addAction(delete_action)
        
        menu.exec_(self.tree.viewport().mapToGlobal(position))
        
    def add_accounts(self):
        dialog = AddAccountDialog(self)
        if dialog.exec_():
            new_accounts = dialog.get_accounts()
            self.accounts.extend(new_accounts)
            self.refresh_tree()
            self.save_accounts()
            self.update_account_count()
            QMessageBox.information(self, "Thành công", f"Đã thêm {len(new_accounts)} tài khoản!")
            
    def add_tree_item(self, account, stt):
        item = QTreeWidgetItem(self.tree)
        
        checkbox = QCheckBox()
        checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                background-color: #2d2d2d;
                border: 2px solid #424242;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                background-color: #00bcd4;
                border-color: #00bcd4;
            }
        """)
        self.tree.setItemWidget(item, 0, checkbox)
        
        item.setText(1, str(stt))
        item.setText(2, account['user'])
        item.setText(3, account['mail'])
        item.setText(4, '●' * 8)
        item.setText(5, account['cookie'][:25] + '...' if account['cookie'] else '❌')
        item.setText(6, account['authorization'][:25] + '...' if account['authorization'] else '❌')
        
        btn_chrome = QPushButton("🌐 Mở")
        btn_chrome.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #f57c00;
            }
        """)
        self.tree.setItemWidget(item, 7, btn_chrome)
        
        btn_cookie = QPushButton("🍪 Lấy Cookie")
        btn_cookie.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.tree.setItemWidget(item, 8, btn_cookie)
        
        item.setData(0, Qt.UserRole, stt-1)
        
    def delete_selected(self):
        selected = self.tree.selectedItems()
        if not selected:
            return
            
        reply = QMessageBox.question(self, 'Xác nhận', 
                                    f"Xóa {len(selected)} tài khoản?",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            indices = sorted([item.data(0, Qt.UserRole) for item in selected], reverse=True)
            for idx in indices:
                self.accounts.pop(idx)
            self.refresh_tree()
            self.save_accounts()
            self.update_account_count()
            
    def refresh_tree(self):
        self.tree.clear()
        for i, account in enumerate(self.accounts):
            self.add_tree_item(account, i+1)
            
    def update_account_count(self):
        self.account_count_label.setText(f"👤 Tài khoản: {len(self.accounts)}")
            
    def save_accounts(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.accounts, f, ensure_ascii=False, indent=2)
            
    def load_accounts(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.accounts = json.load(f)
                self.refresh_tree()
                self.update_account_count()
                
    def save_settings(self):
        with open('settings.json', 'w') as f:
            json.dump(self.settings, f, indent=2)
            
    def load_settings(self):
        if os.path.exists('settings.json'):
            with open('settings.json', 'r') as f:
                self.settings = json.load(f)


class TTCManageTab(QWidget):
    def __init__(self):
        super().__init__()
        self.accounts = []
        self.data_file = "ttc_accounts.json"
        self.setup_ui()
        self.load_accounts()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Toolbar
        toolbar = QWidget()
        toolbar.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        toolbar_layout = QHBoxLayout()
        
        self.account_count_label = QLabel("👤 Tài khoản: 0")
        self.account_count_label.setStyleSheet("color: #ff9800; font-weight: bold; font-size: 14px;")
        
        self.btn_check_balance = QPushButton("💰 Check Xu")
        self.btn_check_balance.setMinimumHeight(35)
        self.btn_check_balance.clicked.connect(self.check_balance)
        self.btn_check_balance.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 6px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        toolbar_layout.addWidget(self.account_count_label)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.btn_check_balance)
        toolbar.setLayout(toolbar_layout)
        
        # TreeView
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(['☑', 'STT', 'User', 'Password', 'Cookie', 'Số Dư'])
        
        header = self.tree.header()
        header.setSectionResizeMode(QHeaderView.Interactive)
        widths = [50, 60, 150, 120, 300, 120]
        for i, w in enumerate(widths):
            self.tree.setColumnWidth(i, w)
        
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.show_context_menu)
        self.tree.setAlternatingRowColors(True)
        self.tree.setSelectionMode(QTreeWidget.ExtendedSelection)
        self.tree.setStyleSheet("""
            QTreeWidget {
                border: 2px solid #424242;
                border-radius: 8px;
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
            }
            QTreeWidget::item {
                padding: 8px 5px;
            }
            QTreeWidget::item:hover {
                background-color: #2d2d2d;
            }
            QTreeWidget::item:selected {
                background-color: #ff9800;
                color: #1e1e1e;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #ff9800;
                padding: 10px;
                border: none;
                border-right: 1px solid #424242;
                font-weight: 600;
            }
        """)
        
        # Log
        log_label = QLabel("📋 Log Hoạt Động")
        log_label.setStyleSheet("color: #ff9800; font-weight: bold; font-size: 14px;")
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(120)
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                color: #b0b0b0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 8px;
                font-family: 'Consolas';
            }
        """)
        
        main_layout.addWidget(toolbar)
        main_layout.addWidget(self.tree)
        main_layout.addWidget(log_label)
        main_layout.addWidget(self.log_text)
        
        self.setLayout(main_layout)
        
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")
        
    def check_balance(self):
        checked_items = []
        for i in range(self.tree.topLevelItemCount()):
            item = self.tree.topLevelItem(i)
            checkbox = self.tree.itemWidget(item, 0)
            if checkbox and checkbox.isChecked():
                checked_items.append(item)
        
        if not checked_items:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn tài khoản để check xu!")
            return
        
        self.log(f"⏳ Bắt đầu check xu {len(checked_items)} tài khoản...")
        
        # TODO: Thêm logic check xu thực tế ở đây
        for item in checked_items:
            idx = item.data(0, Qt.UserRole)
            user = self.accounts[idx]['user']
            # Giả lập kết quả
            import random
            balance = random.randint(1000, 50000)
            self.accounts[idx]['balance'] = balance
            item.setText(5, str(balance))
            self.log(f"✔ {user}: {balance} xu")
        
        self.save_accounts()
        QMessageBox.information(self, "Thành công", f"Đã check xu {len(checked_items)} tài khoản!")
        
    def show_context_menu(self, position):
        menu = QMenu()
        menu.setStyleSheet("""
            QMenu {
                background-color: #2d2d2d;
                border: 2px solid #424242;
                border-radius: 6px;
                color: #e0e0e0;
            }
            QMenu::item {
                padding: 10px 30px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #ff9800;
                color: #1e1e1e;
            }
        """)
        
        add_action = QAction("➕ Thêm Tài Khoản", self)
        add_action.triggered.connect(self.add_accounts)
        menu.addAction(add_action)
        
        selected = self.tree.selectedItems()
        if selected:
            menu.addSeparator()
            delete_action = QAction("🗑 Xóa", self)
            delete_action.triggered.connect(self.delete_selected)
            menu.addAction(delete_action)
        
        menu.exec_(self.tree.viewport().mapToGlobal(position))
        
    def add_accounts(self):
        dialog = AddTTCAccountDialog(self)
        if dialog.exec_():
            new_accounts = dialog.get_accounts()
            self.accounts.extend(new_accounts)
            self.refresh_tree()
            self.save_accounts()
            self.update_account_count()
            self.log(f"✔ Đã thêm {len(new_accounts)} tài khoản")
            QMessageBox.information(self, "Thành công", f"Đã thêm {len(new_accounts)} tài khoản!")
            
    def add_tree_item(self, account, stt):
        item = QTreeWidgetItem(self.tree)
        
        checkbox = QCheckBox()
        checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                background-color: #2d2d2d;
                border: 2px solid #424242;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                background-color: #ff9800;
                border-color: #ff9800;
            }
        """)
        self.tree.setItemWidget(item, 0, checkbox)
        
        item.setText(1, str(stt))
        item.setText(2, account['user'])
        item.setText(3, '●' * 6)
        item.setText(4, account.get('cookie', '')[:30] + '...' if account.get('cookie') else '❌')
        item.setText(5, str(account.get('balance', 0)))
        
        item.setData(0, Qt.UserRole, stt-1)
        
    def delete_selected(self):
        selected = self.tree.selectedItems()
        if not selected:
            return
            
        reply = QMessageBox.question(self, 'Xác nhận', 
                                    f"Xóa {len(selected)} tài khoản?",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            indices = sorted([item.data(0, Qt.UserRole) for item in selected], reverse=True)
            for idx in indices:
                self.accounts.pop(idx)
            self.refresh_tree()
            self.save_accounts()
            self.update_account_count()
            self.log(f"🗑 Đã xóa {len(selected)} tài khoản")
            
    def refresh_tree(self):
        self.tree.clear()
        for i, account in enumerate(self.accounts):
            self.add_tree_item(account, i+1)
            
    def update_account_count(self):
        self.account_count_label.setText(f"👤 Tài khoản: {len(self.accounts)}")
            
    def save_accounts(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.accounts, f, ensure_ascii=False, indent=2)
            
    def load_accounts(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.accounts = json.load(f)
                self.refresh_tree()
                self.update_account_count()


class TTCRegTab(QWidget):
    def __init__(self):
        super().__init__()
        self.accounts = []
        self.data_file = "ttc_reg_accounts.json"
        self.setup_ui()
        self.load_accounts()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Settings panel
        settings_widget = QWidget()
        settings_widget.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                border-radius: 8px;
            }
        """)
        settings_layout = QHBoxLayout()
        settings_layout.setContentsMargins(15, 15, 15, 15)
        settings_layout.setSpacing(20)
        
        # Threads
        thread_group = QGroupBox("🔀 Số Luồng")
        thread_group.setStyleSheet("""
            QGroupBox {
                color: #ff9800;
                font-weight: 600;
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 15px;
                background-color: #1e1e1e;
            }
        """)
        thread_layout = QVBoxLayout()
        self.thread_spin = QSpinBox()
        self.thread_spin.setMinimum(1)
        self.thread_spin.setMaximum(20)
        self.thread_spin.setValue(5)
        self.thread_spin.setMinimumHeight(35)
        self.thread_spin.setStyleSheet("""
            QSpinBox {
                background-color: #1a1a1a;
                color: #e0e0e0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 5px;
            }
        """)
        thread_layout.addWidget(self.thread_spin)
        thread_group.setLayout(thread_layout)
        
        # Captcha Key
        captcha_group = QGroupBox("🔑 Key Giải Captcha")
        captcha_group.setStyleSheet("""
            QGroupBox {
                color: #ff9800;
                font-weight: 600;
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 15px;
                background-color: #1e1e1e;
            }
        """)
        captcha_layout = QVBoxLayout()
        self.captcha_key_input = QLineEdit()
        self.captcha_key_input.setPlaceholderText("Nhập API key giải captcha...")
        self.captcha_key_input.setMinimumHeight(35)
        self.captcha_key_input.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a1a;
                color: #e0e0e0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 8px;
            }
            QLineEdit:focus {
                border: 2px solid #ff9800;
            }
        """)
        captcha_layout.addWidget(self.captcha_key_input)
        captcha_group.setLayout(captcha_layout)
        
        # Buttons
        btn_widget = QWidget()
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(10)
        
        self.btn_start_reg = QPushButton("▶ Bắt Đầu Reg")
        self.btn_stop_reg = QPushButton("⏸ Dừng Lại")
        
        for btn in [self.btn_start_reg, self.btn_stop_reg]:
            btn.setMinimumHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ff9800;
                    color: white;
                    border: none;
                    padding: 8px;
                    border-radius: 6px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #f57c00;
                }
                QPushButton:disabled {
                    background-color: #616161;
                }
            """)
        
        self.btn_stop_reg.setEnabled(False)
        
        btn_layout.addWidget(self.btn_start_reg)
        btn_layout.addWidget(self.btn_stop_reg)
        btn_widget.setLayout(btn_layout)
        
        settings_layout.addWidget(thread_group)
        settings_layout.addWidget(captcha_group)
        settings_layout.addStretch()
        settings_layout.addWidget(btn_widget)
        settings_widget.setLayout(settings_layout)
        
        # TreeView
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(['☑', 'STT', 'User', 'Password', 'Token', 'Số Dư'])
        
        header = self.tree.header()
        header.setSectionResizeMode(QHeaderView.Interactive)
        widths = [50, 60, 150, 120, 200, 120]
        for i, w in enumerate(widths):
            self.tree.setColumnWidth(i, w)
        
        self.tree.setAlternatingRowColors(True)
        self.tree.setStyleSheet("""
            QTreeWidget {
                border: 2px solid #424242;
                border-radius: 8px;
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
            }
            QTreeWidget::item {
                padding: 8px 5px;
            }
            QTreeWidget::item:hover {
                background-color: #2d2d2d;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #ff9800;
                padding: 10px;
                border: none;
                border-right: 1px solid #424242;
                font-weight: 600;
            }
        """)
        
        # Log
        log_label = QLabel("📋 Log Đăng Ký")
        log_label.setStyleSheet("color: #ff9800; font-weight: bold; font-size: 14px;")
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(120)
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                color: #b0b0b0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 8px;
                font-family: 'Consolas';
            }
        """)
        
        main_layout.addWidget(settings_widget)
        main_layout.addWidget(self.tree)
        main_layout.addWidget(log_label)
        main_layout.addWidget(self.log_text)
        
        self.setLayout(main_layout)
        
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")
        
    def save_accounts(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.accounts, f, ensure_ascii=False, indent=2)
            
    def load_accounts(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.accounts = json.load(f)


class TuongTacCheoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Sub tabs
        self.sub_tabs = QTabWidget()
        self.sub_tabs.setStyleSheet("""
            QTabWidget::pane {
                border: none;
                background-color: #1e1e1e;
            }
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #b0b0b0;
                padding: 10px 20px;
                margin-right: 2px;
                border-radius: 6px 6px 0 0;
                font-weight: 600;
            }
            QTabBar::tab:selected {
                background-color: #1e1e1e;
                color: #ff9800;
            }
            QTabBar::tab:hover:!selected {
                background-color: #3d3d3d;
            }
        """)
        
        self.manage_tab = TTCManageTab()
        self.reg_tab = TTCRegTab()
        
        self.sub_tabs.addTab(self.manage_tab, "📋 Quản Lý TuongTacCheo")
        self.sub_tabs.addTab(self.reg_tab, "🆕 Reg TuongTacCheo")
        
        main_layout.addWidget(self.sub_tabs)
        self.setLayout(main_layout)


class RunningTab(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = {
            'delay': 5.0,
            'threads': 3,
            'tabs_per_row': 3,
            'row_count': 2
        }
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Toolbar
        toolbar = QWidget()
        toolbar.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1a1a1a, stop:1 #2d2d2d);
                border-bottom: 2px solid #4caf50;
            }
        """)
        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(20, 15, 20, 15)
        
        title = QLabel("▶ Chạy Xu TuongTacCheo")
        title.setStyleSheet("color: #4caf50; font-size: 20px; font-weight: bold;")
        
        self.status_label = QLabel("⏸ Trạng thái: Chờ")
        self.status_label.setStyleSheet("""
            color: #4caf50;
            font-weight: 600;
            padding: 5px 15px;
            background-color: #2d2d2d;
            border-radius: 6px;
        """)
        
        toolbar_layout.addWidget(title)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.status_label)
        toolbar.setLayout(toolbar_layout)
        
        # Settings panel
        settings_widget = QWidget()
        settings_widget.setStyleSheet("background-color: #1e1e1e;")
        settings_layout = QHBoxLayout()
        settings_layout.setContentsMargins(20, 15, 20, 15)
        settings_layout.setSpacing(20)
        
        # Delay
        delay_group = QGroupBox("⏱ Delay (giây)")
        delay_group.setStyleSheet("""
            QGroupBox {
                color: #4caf50;
                font-weight: 600;
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 15px;
                background-color: #2d2d2d;
            }
        """)
        delay_layout = QVBoxLayout()
        self.delay_spin = QDoubleSpinBox()
        self.delay_spin.setMinimum(0.5)
        self.delay_spin.setMaximum(60.0)
        self.delay_spin.setValue(5.0)
        self.delay_spin.setSuffix(" giây")
        self.delay_spin.setMinimumHeight(35)
        self.delay_spin.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 5px;
            }
        """)
        delay_layout.addWidget(self.delay_spin)
        delay_group.setLayout(delay_layout)
        
        # Threads
        thread_group = QGroupBox("🔀 Số Thread")
        thread_group.setStyleSheet("""
            QGroupBox {
                color: #4caf50;
                font-weight: 600;
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 15px;
                background-color: #2d2d2d;
            }
        """)
        thread_layout = QVBoxLayout()
        self.thread_spin = QSpinBox()
        self.thread_spin.setMinimum(1)
        self.thread_spin.setMaximum(20)
        self.thread_spin.setValue(3)
        self.thread_spin.setMinimumHeight(35)
        self.thread_spin.setStyleSheet("""
            QSpinBox {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 5px;
            }
        """)
        thread_layout.addWidget(self.thread_spin)
        thread_group.setLayout(thread_layout)
        
        # Chrome layout
        chrome_group = QGroupBox("🖥 Bố Cục Chrome")
        chrome_group.setStyleSheet("""
            QGroupBox {
                color: #4caf50;
                font-weight: 600;
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 15px;
                background-color: #2d2d2d;
            }
        """)
        chrome_layout = QFormLayout()
        chrome_layout.setSpacing(10)
        
        self.tabs_per_row_spin = QSpinBox()
        self.tabs_per_row_spin.setMinimum(1)
        self.tabs_per_row_spin.setMaximum(10)
        self.tabs_per_row_spin.setValue(3)
        self.tabs_per_row_spin.setMinimumHeight(35)
        
        self.row_count_spin = QSpinBox()
        self.row_count_spin.setMinimum(1)
        self.row_count_spin.setMaximum(10)
        self.row_count_spin.setValue(2)
        self.row_count_spin.setMinimumHeight(35)
        
        for spin in [self.tabs_per_row_spin, self.row_count_spin]:
            spin.setStyleSheet("""
                QSpinBox {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                    border: 2px solid #424242;
                    border-radius: 6px;
                    padding: 5px;
                }
            """)
        
        chrome_layout.addRow("Tab/Hàng:", self.tabs_per_row_spin)
        chrome_layout.addRow("Số Hàng:", self.row_count_spin)
        chrome_group.setLayout(chrome_layout)
        
        # Paste YTB button
        btn_paste_ytb = QPushButton("📋 Paste Cookie & Author YTB")
        btn_paste_ytb.setMinimumHeight(45)
        btn_paste_ytb.clicked.connect(self.paste_ytb_data)
        btn_paste_ytb.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 6px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        
        # Control buttons
        btn_widget = QWidget()
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(10)
        
        self.btn_start = QPushButton("▶ Bắt Đầu")
        self.btn_stop = QPushButton("⏸ Dừng Lại")
        
        for btn in [self.btn_start, self.btn_stop]:
            btn.setMinimumHeight(45)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4caf50;
                    color: white;
                    border: none;
                    padding: 10px;
                    border-radius: 6px;
                    font-weight: 600;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:disabled {
                    background-color: #616161;
                }
            """)
        
        self.btn_stop.setEnabled(False)
        
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        btn_widget.setLayout(btn_layout)
        
        settings_layout.addWidget(delay_group)
        settings_layout.addWidget(thread_group)
        settings_layout.addWidget(chrome_group)
        settings_layout.addWidget(btn_paste_ytb)
        settings_layout.addStretch()
        settings_layout.addWidget(btn_widget)
        settings_widget.setLayout(settings_layout)
        
        # Running accounts tree
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(['STT', 'User', 'Token', 'Số Dư', 
                                   'Cookie YTB', 'Author YTB', 'Trạng Thái'])
        
        header = self.tree.header()
        header.setSectionResizeMode(QHeaderView.Interactive)
        widths = [60, 120, 150, 100, 200, 200, 150]
        for i, w in enumerate(widths):
            self.tree.setColumnWidth(i, w)
        
        self.tree.setAlternatingRowColors(True)
        self.tree.setStyleSheet("""
            QTreeWidget {
                border: none;
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
                outline: none;
            }
            QTreeWidget::item {
                padding: 8px 5px;
                border-bottom: 1px solid #2d2d2d;
            }
            QTreeWidget::item:hover {
                background-color: #2d2d2d;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #4caf50;
                padding: 10px;
                border: none;
                border-right: 1px solid #424242;
                font-weight: 600;
            }
        """)
        
        # Log
        log_widget = QWidget()
        log_layout = QVBoxLayout()
        log_layout.setContentsMargins(10, 5, 10, 10)
        
        log_label = QLabel("📋 Log Chạy Xu")
        log_label.setStyleSheet("color: #4caf50; font-weight: bold; font-size: 14px;")
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(150)
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                color: #b0b0b0;
                border: 2px solid #424242;
                border-radius: 6px;
                padding: 10px;
                font-family: 'Consolas';
            }
        """)
        
        log_layout.addWidget(log_label)
        log_layout.addWidget(self.log_text)
        log_widget.setLayout(log_layout)
        log_widget.setStyleSheet("background-color: #1e1e1e;")
        
        main_layout.addWidget(toolbar)
        main_layout.addWidget(settings_widget)
        main_layout.addWidget(self.tree)
        main_layout.addWidget(log_widget)
        
        self.setLayout(main_layout)
        
    def paste_ytb_data(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("📋 Paste Cookie & Author YTB")
        dialog.setMinimumWidth(650)
        dialog.setMinimumHeight(450)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Paste Dữ Liệu YouTube")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2196F3;")
        
        info = QLabel("📋 Định dạng: user|cookie_ytb|author_ytb (mỗi dòng 1 tài khoản)")
        info.setStyleSheet("""
            color: #b0b0b0;
            padding: 10px;
            background-color: #2d2d2d;
            border-left: 4px solid #2196F3;
        """)
        
        text_input = QTextEdit()
        text_input.setPlaceholderText("user1|cookie_ytb_value1|Bearer_auth_value1\nuser2|cookie_ytb_value2|Bearer_auth_value2")
        text_input.setStyleSheet("""
            QTextEdit {
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 12px;
                font-family: 'Consolas';
                background-color: #1a1a1a;
                color: #e0e0e0;
            }
        """)
        
        btn_layout = QHBoxLayout()
        btn_ok = QPushButton("✔ Thêm")
        btn_cancel = QPushButton("✖ Hủy")
        
        for btn in [btn_ok, btn_cancel]:
            btn.setMinimumHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    border: none;
                    padding: 10px 25px;
                    border-radius: 6px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #1976D2;
                }
            """)
        
        btn_ok.clicked.connect(dialog.accept)
        btn_cancel.clicked.connect(dialog.reject)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(btn_ok)
        
        layout.addWidget(title)
        layout.addWidget(info)
        layout.addWidget(text_input)
        layout.addLayout(btn_layout)
        
        dialog.setLayout(layout)
        dialog.setStyleSheet("QDialog { background-color: #1e1e1e; }")
        
        if dialog.exec_():
            text = text_input.toPlainText().strip()
            added = 0
            
            for line in text.split('\n'):
                if line.count('|') >= 2:
                    parts = line.split('|')
                    
                    # Tìm item tương ứng trong tree
                    for i in range(self.tree.topLevelItemCount()):
                        item = self.tree.topLevelItem(i)
                        if item.text(1) == parts[0].strip():
                            item.setText(4, parts[1].strip()[:30] + '...')
                            item.setText(5, parts[2].strip()[:30] + '...')
                            added += 1
                            break
            
            if added > 0:
                self.log(f"✔ Đã paste {added} cookie & author YTB")
                QMessageBox.information(self, "Thành công", f"Đã cập nhật {added} tài khoản!")
            else:
                QMessageBox.warning(self, "Cảnh báo", "Không tìm thấy user nào khớp!")
        
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Manager Pro - Dark Edition")
        self.setGeometry(100, 100, 1600, 900)
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QTabWidget::pane {
                border: none;
                background-color: #1e1e1e;
            }
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #b0b0b0;
                padding: 12px 25px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                font-weight: 600;
            }
            QTabBar::tab:selected {
                background-color: #1e1e1e;
                color: #00bcd4;
                border-bottom: 3px solid #00bcd4;
            }
            QTabBar::tab:hover:!selected {
                background-color: #3d3d3d;
                color: #e0e0e0;
            }
        """)
        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        
        self.ytb_tab = YouTubeManagerTab()
        self.ttc_tab = TuongTacCheoTab()
        self.running_tab = RunningTab()
        
        self.tabs.addTab(self.ytb_tab, "🎬 YouTube")
        self.tabs.addTab(self.ttc_tab, "💰 TuongTacCheo")
        self.tabs.addTab(self.running_tab, "▶ Chạy Xu")
        
        self.setCentralWidget(self.tabs)


def main():
    app = QApplication(sys.argv)
    
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(224, 224, 224))
    palette.setColor(QPalette.Base, QColor(30, 30, 30))
    palette.setColor(QPalette.AlternateBase, QColor(45, 45, 45))
    palette.setColor(QPalette.Text, QColor(224, 224, 224))
    app.setPalette(palette)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()