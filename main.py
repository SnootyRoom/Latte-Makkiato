import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.showTable()
        self.upd_btn.clicked.connect(self.showTable)

    def showTable(self):
        cur = self.con.cursor()
        res = cur.execute('''SELECT * FROM Coffee''').fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.con.close()


class AddChangeCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.con = sqlite3.connect('coffee.sqlite')
        self.add_btn.clicked.connect(self.addCoffee)
        self.change_btn.clicked.connect(self.changeCoffee)
        self.my_widget = MyWidget()

    def addCoffee(self):
        cur = self.con.cursor()
        name = self.name.text()
        roasting = self.roasting.text()
        structure = self.structure.text()
        descreption = self.descreption.text()
        price = int(self.price.text())
        amount = int(self.amount.text())
        cur.execute('''INSERT INTO Coffee(name, roasting, structure, descreption, price, amount) 
        VALUES(?, ?, ?, ?, ?, ?)''', (name, roasting, structure, descreption, price, amount,))
        self.con.commit()
        self.my_widget.showTable()

    def changeCoffee(self):
        cur = self.con.cursor()
        change = self.changeline.text()
        id = int(self.id.text())
        if self.comboBox.currentText() == 'Название':
            cur.execute('''UPDATE Coffee SET name = ? WHERE id = ?''', (change, id,))
        if self.comboBox.currentText() == 'Обжарка':
            cur.execute('''UPDATE Coffee SET roasting = ? WHERE id = ?''', (change, id,))
        if self.comboBox.currentText() == 'Структура':
            cur.execute('''UPDATE Coffee SET structure = ? WHERE id = ?''', (change, id,))
        if self.comboBox.currentText() == 'Описание':
            cur.execute('''UPDATE Coffee SET descreption = ? WHERE id = ?''', (change, id,))
        if self.comboBox.currentText() == 'Цена':
            cur.execute('''UPDATE Coffee SET price = ? WHERE id = ?''', (int(change), id,))
        if self.comboBox.currentText() == 'Объём':
            cur.execute('''UPDATE Coffee SET amount = ? WHERE id = ?''', (int(change), id,))
        self.con.commit()
        self.my_widget.showTable()

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    e = AddChangeCoffee()
    e.show()
    sys.exit(app.exec())