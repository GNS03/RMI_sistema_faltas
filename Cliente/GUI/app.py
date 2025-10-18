import warnings

from PyQt6.QtCore import Qt

warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QSizePolicy, QSpacerItem, QTableWidgetItem, \
    QVBoxLayout, QWidget
import sys

## Custom functions
from client_functions import aluno, avaliacao, disciplina, professor



class MyApp(QMainWindow):
    def __init__(self):
        print("Starting GUI...")
        super().__init__()
        uic.loadUi("GUI/UI/new_app.ui", self)

        print("GUI started")

        # Start on login page
        self.stackedWidget.setCurrentIndex(1) # TODO

        # Connect login button
        self.login_button.clicked.connect(self.handle_login)

        # Connect table list click
        # Sends the name the item clicked to load_table (signal?), inside load_table gets the item name, so it can get
        # the data from the database
        self.listWidget.itemClicked.connect(self.load_table)

        # Connect details to table row
        # Sends the item(tableItem) clicked to populate_fields, so it gets the columns and their values, from that row
        self.tableWidget.itemClicked.connect(self.populate_fields_from_row)

        # --- Connect action buttons ---
        self.update_button.clicked.connect(self.update_row)  # Update selected row
        self.delete_button.clicked.connect(self.delete_row)  # Delete selected row
        self.add_button.clicked.connect(self.add_row)  # Add new row

    ## Login screen
    def handle_login(self):
        username = self.user_input.text()
        password = self.password_input.text()

        if username == "root" and password == "root":
            print("Login successful")
            # Go to main page (index 1)
            self.stackedWidget.setCurrentIndex(1)
        else:
            print("Login failed")

    ## Main screen: populate table TODO: Populate with the SQL data, that comes from the server AAAAAAAAAAAAA DONE
    def load_table(self, item, verbose=True):
        table_name = item.text()

        if verbose:
            print(f"Loading table {table_name}...")

        # Fetch fresh data from server
        if table_name == "Alunos":
            data = aluno.select()
        elif table_name == "Disciplinas":
            data = disciplina.select()
        elif table_name == "Avaliações":
            data = avaliacao.select()
        elif table_name == "Professores":
            data = professor.select()
        else:
            data = []

        # print(data)

        # Return empty
        if not data:
            print(f"Couldn't load table {table_name} or table is empty")
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)

            return

        # Set number of rows, columns and headers
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(data[0].keys()))

        # Fill table rows, columns and values
        for row_idx, row_data in enumerate(data):
            for col_idx, key in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

        if verbose:
            print(f"Table {table_name} loaded")

        # Create detail fields
        # print(list(data[0].keys()))
        self.create_detail_fields(list(data[0].keys()))

    ## Main screen: populate details, TODO: Wrong spacing DONE: Made vertical_fields smaller
    def create_detail_fields(self, columns):

        # Clear old widgets
        for i in reversed(range(self.vertical_fields.count())):
            widget = self.vertical_fields.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.fields = {}

        self.vertical_fields.setSpacing(5)  # minimal space between rows
        self.vertical_fields.setContentsMargins(0, 0, 0, 0)

        # Add labels and lineEdits for each column
        for col in columns:
            container = QWidget()
            container_layout = QVBoxLayout(container)
            container_layout.setSpacing(2)  # space between label and input
            container_layout.setContentsMargins(0, 0, 0, 0)

            label = QLabel(col)
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            label.setFixedHeight(label.fontMetrics().height())  # only enough height for text

            line_edit = QLineEdit()
            line_edit.setFixedHeight(25)

            container_layout.addWidget(label)
            container_layout.addWidget(line_edit)

            self.vertical_fields.addWidget(container)

            self.fields[col] = line_edit

        # Connect update button safely
        # try:
        #     self.update_button.clicked.disconnect()
        # except TypeError:
        #     pass
        # self.update_button.clicked.connect(self.update_row)


    def populate_fields_from_row(self, item):
        if not hasattr(self, "fields"):
            return

        row = item.row()
        headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
        for col_idx, key in enumerate(headers):
            if key in self.fields:
                table_item = self.tableWidget.item(row, col_idx)
                if table_item:
                    self.fields[key].setText(table_item.text())

    def refresh_current_table(self):
        selected_item = self.listWidget.currentItem()
        if not selected_item and self.listWidget.count() > 0:
            # Default to first item
            selected_item = self.listWidget.item(0)
        if selected_item:
            self.load_table(selected_item, verbose=False)


    ## Button Functions

    def add_row(self):
        print("Add button clicked")

        if not hasattr(self, "fields"):
            print("No fields to read")
            return

        # Collect values from detail fields
        new_row_data = {}
        for key, line_edit in self.fields.items():
            new_row_data[key] = line_edit.text()

        print("Adding row with data:", new_row_data)

        # Get currently selected table name
        current_item = self.listWidget.currentItem()
        if not current_item:
            print("No table selected.")
            return

        table_name = current_item.text()

        if table_name == "Alunos":
            aluno.inserir(**new_row_data)
        elif table_name == "Disciplinas":
            disciplina.inserir(**new_row_data)
        elif table_name == "Avaliações":
            avaliacao.inserir(**new_row_data)
        elif table_name == "Professores":
            professor.inserir(**new_row_data)
        else:
            pass

        self.refresh_current_table()


    def update_row(self):
        print("Update button clicked")

        if not hasattr(self, "fields"):
            print("No fields to read")
            return

        # Collect values from detail fields
        new_row_data = {}
        for key, line_edit in self.fields.items():
            new_row_data[key] = line_edit.text()

        print("Updating row with data:", new_row_data)

        # Get currently selected table name
        current_item = self.listWidget.currentItem()
        if not current_item:
            print("No table selected.")
            return

        table_name = current_item.text()

        if table_name == "Alunos":
            aluno.editar(**new_row_data)
        elif table_name == "Disciplinas":
            disciplina.editar(**new_row_data)
        elif table_name == "Avaliações":
            avaliacao.editar(**new_row_data)
        elif table_name == "Professores":
            professor.editar(**new_row_data)
        else:
            pass

        self.refresh_current_table()

    def delete_row(self):
        print("Delete button clicked")

        if not hasattr(self, "fields"):
            print("No fields to read")
            return

        # Collect values from detail fields
        new_row_data = {}
        for key, line_edit in self.fields.items():
            new_row_data[key] = line_edit.text()

        print("Deleting row with data:", new_row_data)

        # Get currently selected table name
        current_item = self.listWidget.currentItem()
        if not current_item:
            print("No table selected.")
            return

        table_name = current_item.text()

        if table_name == "Alunos":
            aluno.remover(**new_row_data)
        elif table_name == "Disciplinas":
            disciplina.remover(**new_row_data)
        elif table_name == "Avaliações":
            avaliacao.remover(**new_row_data)
        elif table_name == "Professores":
            professor.remover(**new_row_data)
        else:
            pass

        self.refresh_current_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
