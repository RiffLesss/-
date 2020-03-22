from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QInputDialog, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from random import shuffle
import sys
import sqlite3


class BarleyBreak(QMainWindow):
    def __init__(self):
        self.position = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9' ,'10', '11', '12', '13', '14', '15']
        shuffle(self.position)
        self.moves = 0
        self.flag = False
        record = 1000
        super().__init__()
        uic.loadUi('Barley_Break.ui', self)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QImage('фон.png').scaled(534, 777)))
        self.setPalette(palette)
        self.setWindowTitle('Пятнашки')
        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
        self.matrix = [[self.position[0], self.position[1], self.position[2], self.position[3]],
                  [self.position[4], self.position[5], self.position[6], self.position[7]],
                  [self.position[8], self.position[9], self.position[10], self.position[11]],
                  [self.position[12], self.position[13], self.position[14], '']]
        self.true_matrix = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '']]
        self.true_matrix_2 = [['13', '9', '5', '1'], ['14', '10', '6', '2'], ['15', '11', '7', '3'], ['', '12', '8', '4']]
        self.pushButton_1.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_8)
        self.pushButton_9.clicked.connect(self.run_9)
        self.pushButton_10.clicked.connect(self.run_10)
        self.pushButton_11.clicked.connect(self.run_11)
        self.pushButton_12.clicked.connect(self.run_12)
        self.pushButton_13.clicked.connect(self.run_13)
        self.pushButton_14.clicked.connect(self.run_14)
        self.pushButton_15.clicked.connect(self.run_15)
        self.pushButton_start.clicked.connect(self.run_start)
        self.pushButton_new.clicked.connect(self.run_new)
        self.con = sqlite3.connect("Players.db")
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM Players""").fetchall()
        for elem in result:
            if elem[1] < record:
                record = elem[1]
                self.abs_record = elem[1]
                self.r_name = elem[0]
        self.textBrowser_2.setText('Абсолютный рекорд: ' + str(self.abs_record))
        self.textBrowser_5.setText('Рекордсмен: ' + str(self.r_name))

    def run_start(self):
        i, okBtnPressed = QInputDialog.getText(self, "Введите имя",
                                               "Как тебя зовут?")
        if okBtnPressed:
            self.textBrowser.setText('Игрок: ' + i)
            self.name = i
            self.start()

    def start(self):
        cur = self.con.cursor()
        players = []
        records = []
        result = cur.execute("""SELECT * FROM Players""").fetchall()
        for elem in result:
            players.append(str(elem[0]))
            records.append(elem[1])
        if self.name in players:
            self.record = records[players.index(self.name)]
            self.textBrowser_4.setText('Рекорд: ' + str(self.record))
        else:
            self.textBrowser_4.setText('Рекорд: ' + str('нет'))
            self.flag = True
        self.run_new()

    def run_new(self):
        shuffle(self.position)
        self.pushButton_1.setText(self.position[0])
        self.pushButton_2.setText(self.position[1])
        self.pushButton_3.setText(self.position[2])
        self.pushButton_4.setText(self.position[3])
        self.pushButton_5.setText(self.position[4])
        self.pushButton_6.setText(self.position[5])
        self.pushButton_7.setText(self.position[6])
        self.pushButton_8.setText(self.position[7])
        self.pushButton_9.setText(self.position[8])
        self.pushButton_10.setText(self.position[9])
        self.pushButton_11.setText(self.position[10])
        self.pushButton_12.setText(self.position[11])
        self.pushButton_13.setText(self.position[12])
        self.pushButton_14.setText(self.position[13])
        self.pushButton_15.setText(self.position[14])
        self.pushButton_1.move(10, 120)
        self.pushButton_2.move(140, 120)
        self.pushButton_3.move(270, 120)
        self.pushButton_4.move(400, 120)
        self.pushButton_5.move(10, 250)
        self.pushButton_6.move(140, 250)
        self.pushButton_7.move(270, 250)
        self.pushButton_8.move(400, 250)
        self.pushButton_9.move(10, 380)
        self.pushButton_10.move(140, 380)
        self.pushButton_11.move(270, 380)
        self.pushButton_12.move(400, 380)
        self.pushButton_13.move(10, 510)
        self.pushButton_14.move(140, 510)
        self.pushButton_15.move(270, 510)
        self.matrix = [[self.position[0], self.position[1], self.position[2], self.position[3]],
                  [self.position[4], self.position[5], self.position[6], self.position[7]],
                  [self.position[8], self.position[9], self.position[10], self.position[11]],
                  [self.position[12], self.position[13], self.position[14], '']]
        self.moves = 0
        self.textBrowser_3.setText('Ходы: ' + str(self.moves))

    def run_1(self):
        x = self.pushButton_1.x()
        y = self.pushButton_1.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[0] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_1.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_1.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_1.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_1.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_2(self):
        x = self.pushButton_2.x()
        y = self.pushButton_2.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[1] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_2.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_2.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_2.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_2.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_3(self):
        x = self.pushButton_3.x()
        y = self.pushButton_3.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[2] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_3.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_3.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_3.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_3.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_4(self):
        x = self.pushButton_4.x()
        y = self.pushButton_4.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[3] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_4.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_4.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_4.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_4.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_5(self):
        x = self.pushButton_5.x()
        y = self.pushButton_5.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[4] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_5.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_5.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_5.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_5.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_6(self):
        x = self.pushButton_6.x()
        y = self.pushButton_6.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[5] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_6.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_6.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_6.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_6.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_7(self):
        x = self.pushButton_7.x()
        y = self.pushButton_7.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[6] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_7.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_7.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_7.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_7.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_8(self):
        x = self.pushButton_8.x()
        y = self.pushButton_8.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[7] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_8.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_8.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_8.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_8.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_9(self):
        x = self.pushButton_9.x()
        y = self.pushButton_9.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[8] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_9.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_9.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_9.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_9.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_10(self):
        x = self.pushButton_10.x()
        y = self.pushButton_10.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[9] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_10.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_10.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_10.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_10.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_11(self):
        x = self.pushButton_11.x()
        y = self.pushButton_11.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[10] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_11.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_11.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_11.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_11.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_12(self):
        x = self.pushButton_12.x()
        y = self.pushButton_12.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[11] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_12.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_12.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_12.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_12.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_13(self):
        x = self.pushButton_13.x()
        y = self.pushButton_13.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[12] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_13.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_13.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_13.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_13.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_14(self):
        x = self.pushButton_14.x()
        y = self.pushButton_14.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[13] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_14.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_14.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_14.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_14.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def run_15(self):
        x = self.pushButton_15.x()
        y = self.pushButton_15.y()
        for i in range(4):
            flag = False
            for j in range(4):
                if self.position[14] == self.matrix[i][j]:
                    if j != 0 and self.matrix[i][j - 1] == '':
                        print(self.matrix[i][j - 1])
                        self.matrix[i][j], self.matrix[i][j - 1] = '', self.matrix[i][j]
                        self.pushButton_15.move(x - 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif j != 3 and self.matrix[i][j + 1] == '':
                        self.matrix[i][j], self.matrix[i][j + 1] = '', self.matrix[i][j]
                        self.pushButton_15.move(x + 130, y)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 0 and self.matrix[i - 1][j] == '':
                        self.matrix[i][j], self.matrix[i - 1][j] = '', self.matrix[i][j]
                        self.pushButton_15.move(x, y - 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
                    elif i != 3 and self.matrix[i + 1][j] == '':
                        self.matrix[i][j], self.matrix[i + 1][j] = '', self.matrix[i][j]
                        self.pushButton_15.move(x, y + 130)
                        self.moves += 1
                        self.textBrowser_3.setText('Ходы: ' + str(self.moves))
                        flag = True
                        break
            if flag:
                if (self.matrix == self.true_matrix) or (self.matrix == self.true_matrix_2):
                    self.win()
                break

    def win(self):
        self.open_win_form()
        if self.flag:
            self.players_insert()
            self.record = self.moves
            self.textBrowser_4.setText('Рекорд: ' + str(self.record))
            self.flag = False
        elif self.moves < self.record:
            self.record = self.moves
            self.textBrowser_4.setText('Рекорд: ' + str(self.record))
            self.players_update()
        if self.record < self.abs_record:
            self.abs_record = self.record
            self.r_name = self.name
            self.textBrowser_2.setText('Абсолютный рекорд: ' + str(self.abs_record))
            self.textBrowser_5.setText('Рекордсмен: ' + str(self.r_name))
        self.run_new()

    def open_win_form(self):
        self.win_form = WinForm(self)
        self.win_form.show()

    def players_update(self):
        cur = self.con.cursor()
        query = """UPDATE Players SET Best_Score=? WHERE Player=?"""
        cur.execute(query, (self.record, self.name))
        self.con.commit()

    def players_insert(self):
        cur = self.con.cursor()
        query = """
             INSERT INTO Players
                 (Player, Best_Score)
             VALUES
                  (?, ?)
                """
        data = [self.name, self.moves]
        cur.execute(query, data)
        self.con.commit()


class WinForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QImage('фон.png').scaled(534, 777)))
        self.setPalette(palette)
        self.setGeometry(0, 0, 534, 777)
        self.setWindowTitle('Победа')
        self.lbl = QLabel(self)
        self.lbl.setFont(QFont("Times", 13, QFont.Bold))
        text = "НЕ НУ ЭТО ПОБЕДА!!!1!!1!!!!1!!НЕ НУ ЭТО ПОБЕДА!!!1!!1!!!!1!!\n"
        self.lbl.setText(text * 100)


app = QApplication(sys.argv)
ex = BarleyBreak()
ex.show()
sys.exit(app.exec_())