import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QLineEdit
from PySide6.QtGui import QPixmap, QFont, QColor
from PySide6.QtCore import Qt
from Treeple_d_art_window import ThreeDArtWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Панель взаимодействия отделов")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        # Применяем стили
        self.setStyleSheet("""
            background-color: #222222; /* Черный фон */
            color: #FFFFFF; /* Белый цвет текста */
            font-family: Arial;
        """)

        # Левая часть экрана
        left_layout = QVBoxLayout()

        profile_icon = QLabel()
        profile_icon.setPixmap(QPixmap("m_profile.png").scaled(50, 50, Qt.KeepAspectRatio))
        profile_name = QLabel("Владимир")
        profile_name.setStyleSheet("font-weight: bold; font-size: 14px;")
        profile_department = QLabel("<i>Level Art</i>")
        profile_department.setStyleSheet("font-size: 12px; color: #CCCCCC;")

        recent_button = QPushButton("Недавние")
        settings_button = QPushButton("Настройки")

        departments_label = QLabel("<b>Отделы:</b>")
        departments_label.setStyleSheet("font-size: 14px;")
        departments_layout = QVBoxLayout()

        departments = ["Level design", "3D Art", "Level art", "3D art Vehicles", "VFX/ Animation",
                       "Audio Design", "Narrative Design", "2D Art", "Content QA"]
        for department in departments:
            department_button = QPushButton(department)
            department_button.setStyleSheet("font-size: 12px;")
            department_button.clicked.connect(self.open_3d_art_window)
            departments_layout.addWidget(department_button)

        left_layout.addWidget(profile_icon, alignment=Qt.AlignCenter)
        left_layout.addWidget(profile_name, alignment=Qt.AlignCenter)
        left_layout.addWidget(profile_department, alignment=Qt.AlignCenter)
        left_layout.addWidget(recent_button)
        left_layout.addWidget(settings_button)
        left_layout.addWidget(departments_label)
        left_layout.addLayout(departments_layout)

        # Правая часть экрана
        right_layout = QVBoxLayout()

        projects_label = QLabel("<b>Проекты:</b>")
        projects_label.setStyleSheet("font-size: 14px;")
        search_line_edit = QLineEdit()
        search_line_edit.setPlaceholderText("Поиск")
        search_line_edit.setStyleSheet("font-size: 12px; color: #CCCCCC; background-color: #444444; border: 1px solid #555555; border-radius: 5px;")
        projects_layout = QVBoxLayout()

        # Примеры проектов
        project_data = [
            {"name": "Жемчужная река", "date": "Дата изменения: 27.04.2024", "icon": "project_icon1.png"},
            {"name": "Граница Империи", "date": "Дата изменения: 27.04.2024", "icon": "project_icon2.png"},
            {"name": "Перевал", "date": "Дата изменения: 27.04.2024", "icon": "project_icon3.png"},
            {"name": "Провинция", "date": "Дата изменения: 27.04.2024", "icon": "project_icon4.png"},
            {"name": "Рудники", "date": "Дата изменения: 27.04.2024", "icon": "project_icon5.png"}
        ]

        for project in project_data:
            project_widget = QWidget()
            project_layout = QHBoxLayout()
            project_icon = QLabel()
            project_icon.setPixmap(QPixmap(project["icon"]).scaled(100, 100, Qt.KeepAspectRatio))  # Иконка проекта
            project_name = QPushButton(project["name"])  # Названия проектов как активные кнопки
            project_name.setStyleSheet("font-weight: bold; font-size: 12px; text-align: left; color: #FFFFFF;")  # Цвет текста белый
            project_name.setFlat(True)  # Убираем стиль кнопки
            project_date = QLabel(project["date"])
            project_date.setStyleSheet("font-size: 10px; color: #CCCCCC;")
            project_layout.addWidget(project_icon)
            project_layout.addWidget(project_name)
            project_layout.addWidget(project_date)
            project_widget.setLayout(project_layout)
            projects_layout.addWidget(project_widget)

        right_layout.addWidget(projects_label)
        right_layout.addWidget(search_line_edit)
        right_layout.addLayout(projects_layout, stretch=1)  # Растягиваем layout на всю доступную высоту

        # Расположение левой и правой частей
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 2)

        self.central_widget.setLayout(main_layout)

    def open_3d_art_window(self):
        self.three_d_art_window = ThreeDArtWindow()
        self.three_d_art_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
