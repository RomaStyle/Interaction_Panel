import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QWidget, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ShareWindow(QMainWindow):
    def __init__(self, selected_work_image_path):
        super().__init__()
        self.setWindowTitle("Поделиться")
        self.setFixedSize(450, 450)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        central_widget.setLayout(main_layout)

        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)


        work_label = QLabel("Работа:")
        work_label.setAlignment(Qt.AlignCenter)
        work_label.setStyleSheet("font-weight: bold;")
        left_layout.addWidget(work_label, alignment=Qt.AlignHCenter)

        selected_work_label = QLabel()
        selected_work_pixmap = QPixmap(selected_work_image_path)
        selected_work_pixmap = selected_work_pixmap.scaledToWidth(150)
        selected_work_label.setPixmap(selected_work_pixmap)
        selected_work_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(selected_work_label, alignment=Qt.AlignHCenter)

        comments_label = QLabel("Комментарий:")
        comments_label.setStyleSheet("font-weight: bold;")
        left_layout.addWidget(comments_label, alignment=Qt.AlignHCenter)

        # поиск строка
        search_line_edit = QLineEdit()
        search_line_edit.setPlaceholderText("Введите текст")
        search_line_edit.setStyleSheet("color: #AAAAAA; font-style: italic;")  # Серый цвет и курсив
        left_layout.addWidget(search_line_edit)

        send_to_button = QPushButton("Направить в...")
        send_to_button.setStyleSheet("font-weight: bold;"
                                     "background-color: #4CAF50;"  # Зелёный цвет
                                     "border-style: outset;"  # Стиль границы
                                     "border-width: 2px;"  # Ширина границы
                                     "border-color: #45a049;"  # Цвет границы
                                     "padding: 6px 10px;"  # Отступы внутри кнопки
                                     "color: white;"  # Цвет текста
                                     "font-size: 16px;"  # Размер шрифта
                                     "border-radius: 6px;")  # Закругление углов
        left_layout.addWidget(send_to_button, alignment=Qt.AlignHCenter)
        send_to_button.setEnabled(False)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)


        generation_request_label = QLabel("Запрос генерации:")
        generation_request_label.setAlignment(Qt.AlignCenter)  # Выравнивание по центру
        generation_request_label.setStyleSheet("font-weight: bold;")
        right_layout.addWidget(generation_request_label, alignment=Qt.AlignHCenter)

        # поиск строка
        generation_request_line_edit = QLineEdit()
        generation_request_line_edit.setPlaceholderText("Сгенерируй по примеру подобной картинки подобную гору в пустынном стиле с обостренностями на скалах")
        generation_request_line_edit.setStyleSheet("color: #AAAAAA; font-style: italic;")
        right_layout.addWidget(generation_request_line_edit)


        generate_button = QPushButton("Сгенерировать")
        generate_button.setStyleSheet("font-weight: bold;"
                                       "background-color: #008CBA;"  # Синий цвет
                                       "border-style: outset;"  # Стиль границы
                                       "border-width: 2px;"  # Ширина границы
                                       "border-color: #007A99;"  # Цвет границы
                                       "padding: 6px 10px;"  # Отступы внутри кнопки
                                       "color: white;"  # Цвет текста
                                       "font-size: 16px;"  # Размер шрифта
                                       "border-radius: 6px;")  # Закругление углов
        right_layout.addWidget(generate_button, alignment=Qt.AlignHCenter)

        #контейнер для картинок
        images_layout = QVBoxLayout()

        #два горизонтальных контейнера
        for i in range(2):
            hbox = QHBoxLayout()
            images_layout.addLayout(hbox)
            for j in range(2):
                image_label = QLabel()
                image_pixmap = QPixmap(f"generated_work{(i*2)+j+1}.png")
                image_pixmap = image_pixmap.scaledToWidth(150)  # размер фото
                image_label.setPixmap(image_pixmap)
                hbox.addWidget(image_label, alignment=Qt.AlignHCenter)

        right_layout.addLayout(images_layout)

        self.setStyleSheet("""
            background-color: #000000; 
            color: #FFFFFF; 
            font-family: Arial;
        """)


        generation_request_line_edit.setFocusPolicy(Qt.ClickFocus)
        generation_request_line_edit.mousePressEvent = lambda event: generation_request_line_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShareWindow("selected_work.png")
    window.show()
    sys.exit(app.exec())
