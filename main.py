from contract import Contract
from storage import Storage
from material import Material
from storage_2 import Storage2
from product import Product
from database import Database
import os
import pandas as pd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit, QMessageBox


# os.system("git fetch origin")
# os.system("git reset --hard origin/master")
# os.system("git clean -f -d")

database = Database()
material_storage = Storage()
product_storage = Storage2()


class UIWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.setContentsMargins(200, 11, 200, 11)
        self.hbox1.setSpacing(25)
        self.hbox1.setObjectName("hbox1")
        self.button1 = QtWidgets.QPushButton("Production")
        self.button1.setFont(QtGui.QFont("Sanserif", 20))
        self.button1.setStyleSheet('color:black')
        self.hbox1.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton("Merchandise")
        self.button2.setFont(QtGui.QFont("Sanserif", 20))
        self.button2.setStyleSheet('color:black')

        self.hbox1.addWidget(self.button2)

        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.setContentsMargins(100, 11, 100, 11)
        self.hbox2.setSpacing(25)
        self.hbox2.setObjectName("hbox2")
        self.button3 = QtWidgets.QPushButton("Contracts")
        self.button3.setFont(QtGui.QFont("Sanserif", 20))
        self.button3.setStyleSheet('color:black')
        self.hbox2.addWidget(self.button3)
        self.button4 = QtWidgets.QPushButton("Material Storage")
        self.button4.setFont(QtGui.QFont("Sanserif", 20))
        self.button4.setStyleSheet('color:black')

        self.hbox2.addWidget(self.button4)
        self.button5 = QtWidgets.QPushButton("Product Storage")
        self.button5.setFont(QtGui.QFont("Sanserif", 20))
        self.button5.setStyleSheet('color:black')

        self.hbox2.addWidget(self.button5)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.setContentsMargins(11, 11, 11, 11)
        self.vbox.setSpacing(6)
        self.vbox.setObjectName("vbox")
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)


class UIContracts(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIContracts, self).__init__(parent)
        # self.CPSBTN = QtWidgets.QPushButton("text2", self.centralwidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(len(database.contracts.keys()))
        self.tableWidget.setColumnCount(3)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_add = QtWidgets.QPushButton("Add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_edit = QtWidgets.QPushButton("Edit")
        self.verticalLayout.addWidget(self.pushButton_edit)
        self.pushButton_remove = QtWidgets.QPushButton("Remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_sort = QtWidgets.QPushButton("Sort")
        self.verticalLayout.addWidget(self.pushButton_sort)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton("Close")
        self.verticalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.setLayout(self.verticalLayout_2)

        self.Contracts()

    def Contracts(self):

        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Company Name"))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Start Date"))
        # self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("End Date"))
        headers = ["Company Name", "Start Date", "End Date"]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        current_contracts = list(database.contracts.values())
        print(current_contracts)
        for i in range(len(database.contracts.values())):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(current_contracts[i].company_name))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(current_contracts[i].start_date))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(current_contracts[i].end_date))
            self.tableWidget.setColumnWidth(0, 200)


    def add(self):
        row = self.tableWidget.currentRow()
        text, ok = QInputDialog.getText(self, "Employee Dialog", "Enter Company Name")
        if ok and text is not None:
            name = text
        text, ok = QInputDialog.getText(self, "Employee Dialog", "Enter Start Date")
        if ok and text is not None:
            start_date = text
        text, ok = QInputDialog.getText(self, "Employee Dialog", "Enter End Date")
        if ok and text is not None:
            end_date = text
        cont = Contract(name, start_date, end_date)
        database.add_contract(cont)
        w.startUIContracts()
        # a = len(database.contracts.keys()) - 1
        # self.tableWidget.setRowCount(len(database.contracts.keys()))
        # self.tableWidget.setItem(a, 0, QtWidgets.QTableWidgetItem(cont.company_name))
        # self.tableWidget.setItem(a, 1, QtWidgets.QTableWidgetItem(cont.start_date))
        # self.tableWidget.setItem(a, 2, QtWidgets.QTableWidgetItem(cont.end_date))

    def edit(self):
        item = self.tableWidget.currentItem()
        column = self.tableWidget.currentColumn()

        if item is not None:
            string, ok = QInputDialog.getText(self, "Employee Dialog", "Edit",
                                              QLineEdit.Normal, item.text())
            if ok and string is not None:
                item.setText(string)

    def remove(self):
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)
        cont = database.contracts[item.text()]
        if item is None:
            return

        reply = QMessageBox.question(self, "Remove Employee", "Do You Want To Remove Contract " + str(item.text()),
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            database.delete_contract(cont)
            w.startUIContracts()


    def sort(self):
        self.tableWidget.sortItems(0)


class UIMerchandise(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIMerchandise, self).__init__(parent)
        self.CPSBTN = QtWidgets.QPushButton("text2", self)
        self.CPSBTN.move(100, 350)


class UIProduction(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIProduction, self).__init__(parent)
        self.CPSBTN = QtWidgets.QPushButton("text2", self)
        self.CPSBTN.move(100, 350)


class UIProduct(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIProduct, self).__init__(parent)
        self.CPSBTN = QtWidgets.QPushButton("text2", self)
        self.CPSBTN.move(100, 350)


class UIMaterial(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIMaterial, self).__init__(parent)
        self.CPSBTN = QtWidgets.QPushButton("text2", self)
        self.CPSBTN.move(100, 350)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 1000, 600)
        self.setFixedSize(1000, 600)
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        saveAction = QtWidgets.QAction(QtGui.QIcon("save.png"), 'Save', self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save_all)
        self.startUIWindow()

    def save_all(self):
        reply = QMessageBox.question(self, "Remove Employee", "Do You Want To Save Your Changes ",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            save_materials()
            save_contracts()
            save_products()

    def startUIWindow(self):
        self.uiWindow = UIWindow(self)
        self.setWindowTitle("UIWindow")
        self.setCentralWidget(self.uiWindow)
        self.uiWindow.button1.clicked.connect(self.startUIProduction)
        self.uiWindow.button2.clicked.connect(self.startUIMerchandise)
        self.uiWindow.button3.clicked.connect(self.startUIContracts)
        self.uiWindow.button4.clicked.connect(self.startUIProduct)
        self.uiWindow.button5.clicked.connect(self.startUIMaterial)
        self.show()

    def startUIContracts(self):
        self.uiContracts= UIContracts(self)
        self.setWindowTitle("UIContracts")
        self.setCentralWidget(self.uiContracts)
        self.uiContracts.pushButton_close.clicked.connect(self.startUIWindow)
        self.uiContracts.pushButton_add.clicked.connect(self.uiContracts.add)
        self.uiContracts.pushButton_edit.clicked.connect(self.uiContracts.edit)
        self.uiContracts.pushButton_remove.clicked.connect(self.uiContracts.remove)
        self.uiContracts.pushButton_sort.clicked.connect(self.uiContracts.sort)
        self.show()

    def startUIMerchandise(self):
        self.uiMerchandise = UIMerchandise(self)
        self.setWindowTitle("UIMerchandise")
        self.setCentralWidget(self.uiMerchandise)
        self.uiMerchandise.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUIProduction(self):
        self.uiProduction= UIProduction(self)
        self.setWindowTitle("UIProduction")
        self.setCentralWidget(self.uiProduction)
        self.uiProduction.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUIProduct(self):
        self.uiProduct = UIProduct(self)
        self.setWindowTitle("UIProduct")
        self.setCentralWidget(self.uiProduct)
        self.uiProduct.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUIMaterial(self):
        self.uiMaterial = UIMaterial(self)
        self.setWindowTitle("UIMaterial")
        self.setCentralWidget(self.uiMaterial)
        self.uiMaterial.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()


def read_contracts():
    contracts = pd.read_excel('contracts.xlsx')

    companies = contracts['Company Name']
    start_dates = contracts['Start Date']
    end_dates = contracts['End Date']

    for i in range(len(companies)):
        contract = Contract(companies[i], start_dates[i], end_dates[i])
        database.add_contract(contract)


def read_materials():
    materials = pd.read_excel('materials.xlsx')

    names = materials['Material Name']
    quantities = materials['Quantity']
    arrivals = materials['Arrival Date']
    expires = materials['Expire Date']
    suppliers = materials['Supplier']
    for i in range(len(names)):
        print(names[i])
        supplier = database.contracts[suppliers[i]]
        M1 = Material(names[i], quantities[i], arrivals[i], expires[i], supplier)
        supplier.add_material(M1)
        material_storage.add_material(M1)


def read_products():

    products = pd.read_excel('products.xlsx', sheet_name='Sheet1')
    sheet2 = pd.read_excel('products.xlsx', sheet_name='Sheet2')

    names = products['Product Name']
    expires = products['Expire Date']
    quantities = products['Quantity']
    ingrds = sheet2['Ingredients']

    for i in range(len(names)):
        ingredients = {}
        for j in range(len(ingrds)):
            ingredients[ingrds[j]] = sheet2[names[i]][j]
        print(ingredients)
        P1 = Product(names[i], ingredients, expires[i], quantities[i])
        print(P1.product_name, P1.expire_date, P1.quantity)
        product_storage.add_product(P1)


def save_materials():
    materials = {'Material Name': [],
                 'Quantity': [],
                 'Arrival Date': [],
                 'Expire Date': [],
                 'Supplier': []
                 }

    for material in material_storage.storage_dict.values():
        materials['Material Name'].append(material.material_name)
        materials['Quantity'].append(material.quantity)
        materials['Arrival Date'].append(material.date)
        materials['Expire Date'].append(material.expiration_date)
        materials['Supplier'].append(material.supplier.company_name)

    materials = pd.DataFrame(materials)

    writer = pd.ExcelWriter('materials.xlsx')
    materials.to_excel(writer)
    writer.save()


def save_contracts():
    contracts = {'Company Name': [],
                 'Start Date': [],
                 'End Date': []
                 }

    for contract in database.contracts.values():
        contracts['Company Name'].append(contract.company_name)
        contracts['Start Date'].append(contract.start_date)
        contracts['End Date'].append(contract.end_date)

    contracts = pd.DataFrame(contracts)

    writer = pd.ExcelWriter('contracts.xlsx')
    contracts.to_excel(writer)
    writer.save()


def save_products():
    products = {'Product Name': [],
                'Expire Date': [],
                'Quantity': []
                }

    for product in product_storage.storage2_dict.values():
        products['Product Name'].append(product.product_name)
        products['Expire Date'].append(product.expire_date)
        products['Quantity'].append(product.quantity)

    products = pd.DataFrame(products)

    writer = pd.ExcelWriter('products_1.xlsx', sheet_name='Sheet1')
    products.to_excel(writer)
    writer.save()


read_contracts()
read_materials()
read_products()

# ingredients = {"Leather": 3, "String": 2}
# shoe = Product("Shoe", ingredients, "20.10.2021")
# shoe.produce(material_storage, 6, product_storage)

# print(shoe.quantity)
# print(product_storage.storage2_dict)
example_product = product_storage.storage2_dict["Milk Chocolate"]
example_product.produce(material_storage, 2, product_storage)
print(example_product.quantity)
print(product_storage.storage2_dict)

# from pyqtgui import Window
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Window()
# ui.setupUi(Dialog, database, material_storage, product_storage)
# Dialog.show()
# sys.exit(app.exec_())
# from erpgui import MainWindow
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
sys.exit(app.exec_())

# os.system("git add -A")
# os.system("git commit -m \"Commit.\"")
# os.system("git push -u origin master")


