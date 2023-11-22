# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ib2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import math
import time
from math import sqrt

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys
from PyQt5.QtWidgets import QFileDialog
import sympy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.view_possl = QtWidgets.QTextBrowser(self.centralwidget)
        self.view_possl.setGeometry(QtCore.QRect(10, 10, 781, 271))
        self.view_possl.setObjectName("view_possl")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(280, 350, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generate.setFont(font)
        self.generate.setAutoFillBackground(False)
        self.generate.setObjectName("generate")
        self.size_possl = QtWidgets.QSpinBox(self.centralwidget)
        self.size_possl.setGeometry(QtCore.QRect(260, 300, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.size_possl.setFont(font)
        self.size_possl.setMinimum(1)
        self.size_possl.setMaximum(100000)
        self.size_possl.setProperty("value", 10000)
        self.size_possl.setObjectName("size_possl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 300, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(440, 300, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.upload.setFont(font)
        self.upload.setObjectName("upload")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(440, 350, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.test1 = QtWidgets.QPushButton(self.centralwidget)
        self.test1.setGeometry(QtCore.QRect(10, 430, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test1.setFont(font)
        self.test1.setObjectName("test1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.test2 = QtWidgets.QPushButton(self.centralwidget)
        self.test2.setGeometry(QtCore.QRect(10, 480, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.test2.setFont(font)
        self.test2.setAutoRepeat(False)
        self.test2.setAutoExclusive(False)
        self.test2.setObjectName("test2")
        self.test3 = QtWidgets.QPushButton(self.centralwidget)
        self.test3.setGeometry(QtCore.QRect(10, 530, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.test3.setFont(font)
        self.test3.setAutoRepeat(False)
        self.test3.setAutoExclusive(False)
        self.test3.setObjectName("test3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 400, 191, 21))
        self.label_3.setObjectName("label_3")
        self.view_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.view_result.setGeometry(QtCore.QRect(360, 430, 421, 131))
        self.view_result.setObjectName("view_result")
        self.generate_2 = QtWidgets.QPushButton(self.centralwidget)
        self.generate_2.setGeometry(QtCore.QRect(170, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.generate_2.setFont(font)
        self.generate_2.setAutoFillBackground(False)
        self.generate_2.setObjectName("generate_2")
        self.generate_3 = QtWidgets.QPushButton(self.centralwidget)
        self.generate_3.setGeometry(QtCore.QRect(10, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.generate_3.setFont(font)
        self.generate_3.setAutoFillBackground(False)
        self.generate_3.setObjectName("generate_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Связка события нажатия кнопки с функцией load_sequence
        self.upload.clicked.connect(self.load_sequence)
        # Связка события нажатия кнопки с функцией save_sequence
        self.save.clicked.connect(self.save_sequence)
        # Связка события нажатия кнопки с функцией generate_bits
        self.generate.clicked.connect(self.generate_bits)
        # Связка события нажатия кнопки с функцией frequency_test
        self.test1.clicked.connect(self.frequency_test)
        # Связка события нажатия кнопки с функцией sequence_test
        self.test2.clicked.connect(self.sequence_test)
        # Связка события нажатия кнопки с функцией extended_test
        self.test3.clicked.connect(self.extended_test)

        self.generate_3.clicked.connect(self.cubic_congruential_generator)
        self.generate_2.clicked.connect(self.add_gen2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generate.setText(_translate("MainWindow", "RSA"))
        self.label.setText(_translate("MainWindow", "длина генерируемой последовательности в битах:"))
        self.upload.setText(_translate("MainWindow", "Загрузить последовательность из файла"))
        self.save.setText(_translate("MainWindow", "Сохранить последовательность в файл"))
        self.test1.setText(_translate("MainWindow", "Частотный тест"))
        self.label_2.setText(_translate("MainWindow", "Тесты:"))
        self.test2.setText(_translate("MainWindow", "Тест на последовательность одинаковых бит"))
        self.test3.setText(_translate("MainWindow", "Расширенный тест напроизвольные отклонения"))
        self.label_3.setText(_translate("MainWindow", "Результат теста:"))
        self.generate_2.setText(_translate("MainWindow", "Аддитивный"))
        self.generate_3.setText(_translate("MainWindow", "Куб. конгруэнтный"))


    def add_gen2(self):
        a = 55
        b = 24
        n = 32

        key = [random.randint(0, 2 ** 31 - 1) for _ in range(a)]
        bin_arr = []
        # Количество итераций для генерации последовательности
        num_iterations = int(self.size_possl.text())

        for i in range(a, num_iterations + a):
            Xi = (key[i-a] + key[i-b]) % 2 ** n
            key.append(Xi)
            bin_arr.append(bin(Xi)[2:])
        sequence_str = ''.join(map(str, bin_arr))
        # Выведите последовательность в self.view_possl
        self.view_possl.setText(sequence_str)

    def cubic_congruential_generator(self):
        seed = time.time()
        a = 16807
        b = 16807
        c = 16807
        d = 16807
        m = 2 ** 32 - 1
        n = int(self.size_possl.text())
        random_numbers = [seed]
        bin_arr = []
        for i in range(n):
            state = (a * random_numbers[i-1] ** 3 + b * random_numbers[i - 1] ** 2 + c * random_numbers[i - 1] + d) % m
            state = int(format(int(state), '032b'))
            random_numbers.append(state)
            bin_arr.append(state)
        # Объедините биты в одну строку
        sequence_str = ''.join(map(str, bin_arr))

        # Выведите последовательность в self.view_possl
        self.view_possl.setText(sequence_str)


    # Функция для проверки числа на простоту с использованием теста Миллера-Рабина
    def is_prime(self, n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        # Выразим n - 1 как 2^r * d
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Проведем тест Миллера-Рабина k раз
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

        return True

    # Функция для генерации случайных больших простых чисел
    def generate_large_primes(self, bits):
        while True:
            potential_prime = random.getrandbits(bits)
            if potential_prime % 2 == 0:
                potential_prime += 1
            if self.is_prime(potential_prime):
                return potential_prime

    def find_coprime_k(self, N):
        # Вычислите f(N)
        fN = N - 1

        # Создайте список всех целых чисел от 2 до N - 1
        possible_k_values = list(range(2, fN))

        while True:
            # Случайным образом выберите k
            k = random.choice(possible_k_values)

            # Проверьте, что k и f(N) взаимно просты
            if math.gcd(k, fN) == 1:
                return k

    # генерация и вывод последовательности бит
    def generate_bits(self):
        # Получить длину последовательности из self.size_possl
        sequence_length = int(self.size_possl.text())

        # Генерируйте случайную последовательность бит длиной sequence_length
        # random_sequence = [str(random.randint(0, 1)) for _ in range(sequence_length)]
        bits = 12  # Размер в битах
        # p = self.generate_large_primes(bits)
        # q = self.generate_large_primes(bits)

        p = sympy.randprime(10 ** 3, 10 ** 4)

        q = sympy.randprime(10 ** 3, 10 ** 4)

        N = p * q
        fN = (p - 1) * (q - 1)

        k = self.find_coprime_k(fN)

        u0 = random.choice(list(range(1, N - 1)))
        u_arr = [u0]
        x_arr = []
        for i in range(1, sequence_length + 1):
            # val = numpy.power(u_arr[i - 1], k)
            # val = u_arr[i - 1] ** k
            val2 = pow(u_arr[i - 1], k, N)
            # val2 = val % N
            u_arr.append(val2)
            x_arr.append(val2 & 1)

        print(len(x_arr))
        # Объедините биты в одну строку
        sequence_str = ''.join(map(str, x_arr))

        # Выведите последовательность в self.view_possl
        self.view_possl.setText(sequence_str)

    # загрузка последовательности из файла
    def load_sequence(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Открываем файловый диалог для выбора файла
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(None, "Выберите файл", "",
                                                     "Текстовые файлы (*.txt);;Все файлы (*)", options=options)

        if file_paths:
            # Выбран хотя бы один файл
            file_path = file_paths[0]

            try:
                with open(file_path, 'r') as file:
                    sequence_str = file.read()

                # Выведите последовательность в self.view_possl
                self.view_possl.setPlainText(sequence_str)
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка при чтении файла: {str(e)}")

    # Функция для сохранения последовательности в файл
    def save_sequence(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Открываем файловый диалог для выбора места сохранения
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(None, "Сохранить файл", "",
                                                   "Текстовые файлы (*.txt);;Все файлы (*)", options=options)

        if file_path:
            try:
                # Получить текст из self.view_possl
                sequence_str = self.view_possl.toPlainText()

                # Записать последовательность в выбранный файл
                with open(file_path, 'w') as file:
                    file.write(sequence_str)

                QtWidgets.QMessageBox.information(None, "Успешно", "Последовательность успешно сохранена в файл.")
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка при сохранении файла: {str(e)}")

    # Частотный тест
    def frequency_test(self):
        # Получить текст из self.view_possl
        sequence = self.view_possl.toPlainText()
        summ = 0
        for i in sequence:
            summ += 2 * int(i) - 1

        stat = abs(summ) / sqrt(len(sequence))

        if stat <= 1.82138636:
            # Вывести результат теста в self.view_result
            result = f"S({stat}) <= {1.82138636}\nТест пройден"
            self.view_result.setPlainText(result)
        else:
            # Вывести результат теста в self.view_result
            result = f"S({stat}) >= {1.82138636}\nТест НЕ пройден"
            self.view_result.setPlainText(result)

    # Тест на последовательность одинаковых бит
    def sequence_test(self):
        # Получить текст из self.view_possl
        sequence = self.view_possl.toPlainText()

        # Вычисление суммы
        summ = 0
        for i in sequence:
            summ += int(i)

        # Вычисление частоты
        freq = summ / len(sequence)

        # Вычисление V
        V = 0
        for i in range((len(sequence) - 1)):
            if int(sequence[i]) == int(sequence[i + 1]):
                V += 1
            i += 1
        V += 1

        # Вычисление статистики
        stat = abs(V - 2 * len(sequence) * freq * (1 - freq)) / (2 * sqrt(2 * len(sequence)) * freq * (1 - freq))

        if stat <= 1.82138636:
            # Вывести результат теста в self.view_result
            result = f"S({stat}) <= {1.82138636}\nТест пройден"
            self.view_result.setPlainText(result)
        else:
            # Вывести результат теста в self.view_result
            result = f"S({stat}) >= {1.82138636}\nТест НЕ пройден"
            self.view_result.setPlainText(result)

    # Расширенный тест на произвольные отклонения
    def extended_test(self):
        sums = []
        # Получить текст из self.view_possl
        sequence = self.view_possl.toPlainText()

        # Вычисляются суммы 𝑆𝑖 последовательно удлиняющихся подпоследовательностей, начинающихся с 𝑋1
        summ = 0
        for i in range(len(sequence)):
            for i in range(i):
                summ += 2 * int(sequence[i]) - 1
            sums.append(summ)
        print(sums)

        # Формируется новая последовательность 𝑆′ = 0, 𝑆1, 𝑆2, … , 𝑆𝑛, 0
        sums.append(0)
        sums.insert(0, 0)

        # Вычисляется 𝐿 = 𝑘 − 1, где k – количество нулей в полученной последовательности 𝑆′.
        k = 0
        for i in sums:
            if i == 0:
                k += 1
        L = k - 1

        Y = []
        for i in range(-9, 0):
            s = 0
            for j in sums:
                if i == j:
                    s += 1
            y = abs(s - L) / sqrt(2 * L * (4 * abs(i) - 2))
            Y.append(y)

        for i in range(1, 10):
            s = 0
            for j in sums:
                if i == j:
                    s += 1
            y = abs(s - L) / sqrt(2 * L * (4 * abs(i) - 2))
            Y.append(y)

        success = True
        text = ""
        k = 1
        for i in Y:
            if i > 1.82138636:
                success = False
            text += f"Y{k}({i})\n"
            k += 1
            self.view_result.setPlainText(text)

        if success == True:
            text += "Тест пройден"
        else:
            text += "Тест не пройден"
        self.view_result.setPlainText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
