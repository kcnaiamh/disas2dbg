from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QGridLayout,
    QPushButton,
    QLineEdit,
)


class MainWindow(QMainWindow):
    disas_base_addr = None

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

        self.disas_base_le = QLineEdit()
        self.disas_base_le.textEdited.connect(self.update_disas_base_addr)
        self.disas_base_le.setPlaceholderText("Disassembler's Base Address")

        self.dbg_base_le = QLineEdit()
        self.dbg_base_le.textEdited.connect(self.update_dbg_base_addr)
        self.dbg_base_le.setPlaceholderText("Debugger's Base Address")

        self.disas_cur_le = QLineEdit()
        self.disas_cur_le.returnPressed.connect(self.disas_return_pressed)
        self.disas_cur_le.textEdited.connect(self.update_disas_cur_addr)
        self.disas_cur_le.setPlaceholderText("Disassembler's Current Address")

        self.dbg_cur_le = QLineEdit()
        self.dbg_cur_le.returnPressed.connect(self.dbg_return_pressed)
        self.dbg_cur_le.textEdited.connect(self.update_dbg_cur_addr)
        self.dbg_cur_le.setPlaceholderText("Debugger's Current Address")

        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_btn_clicked)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.disas_base_le, 0, 0, 1, 4)
        grid_layout.addWidget(self.dbg_base_le, 0, 4, 1, 4)
        grid_layout.addWidget(self.disas_cur_le, 1, 0, 1, 4)
        grid_layout.addWidget(self.dbg_cur_le, 1, 4, 1, 4)
        grid_layout.addWidget(clear_btn, 2, 0)

        grid_widget = QWidget()
        grid_widget.setLayout(grid_layout)
        self.setCentralWidget(grid_widget)

    def add0x(self, tmp):
        if tmp[:2] != "0x":
            tmp = "0x" + tmp
        return tmp

    def disas_return_pressed(self):
        disas_cur = int(self.add0x(self.disas_cur_addr), 16)
        dbg_base = int(self.add0x(self.dbg_base_addr), 16)
        disas_base = int(self.add0x(self.disas_base_addr), 16)
        try:
            diff = disas_cur - disas_base
            dbg_cur = dbg_base + diff
            self.dbg_cur_addr = hex(dbg_cur)
            self.dbg_cur_le.setText(hex(dbg_cur))
        except ValueError:
            print("Invalid input. Please enter valid hexadecimal values.")
            exit(1)

    def dbg_return_pressed(self):
        dbg_cur = int(self.add0x(self.dbg_cur_addr), 16)
        dbg_base = int(self.add0x(self.dbg_base_addr), 16)
        disas_base = int(self.add0x(self.disas_base_addr), 16)
        try:
            diff = dbg_cur - dbg_base
            disas_cur = disas_base + diff
            self.disas_cur_addr = hex(disas_cur)
            self.disas_cur_le.setText(hex(disas_cur))
        except ValueError:
            print("Invalid input. Please enter valid hexadecimal values.")
            exit(1)

    def clear_btn_clicked(self):
        self.disas_cur_le.clear()
        self.dbg_cur_le.clear()

    def update_disas_base_addr(self, new_text):
        self.disas_base_addr = new_text

    def update_dbg_base_addr(self, new_text):
        self.dbg_base_addr = new_text

    def update_disas_cur_addr(self, new_text):
        self.disas_cur_addr = new_text

    def update_dbg_cur_addr(self, new_text):
        self.dbg_cur_addr = new_text
