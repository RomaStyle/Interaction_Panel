import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from share_button import ShareWindow  # для окна поделиться

class ThreeDArtWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Art Окно")
        self.setGeometry(100, 60, 1000, 640)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()
        self.display_image("tool_image.jpg")  #изображение при открытии окна
        self.share_window = None

    def setup_ui(self):
        self.setStyleSheet("""
            background-color: #222222; 
            color: #FFFFFF; 
            font-family: Arial;
        """)

        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        create_button = QPushButton("Создать файл")
        save_button = QPushButton("Сохранить")
        share_button = QPushButton("Поделиться")
        share_button.setStyleSheet("font-weight: bold;")
        top_layout.addWidget(create_button)
        top_layout.addWidget(save_button)
        top_layout.addWidget(share_button)
        main_layout.addLayout(top_layout)

        tools_and_image_layout = QHBoxLayout()

        tools_layout = QVBoxLayout()
        tool_icons = ["maya_icon.png", "figma_icon.png", "blender_icon.png", "photoshop_icon.png", "illustrator_icon.png"]
        tool_images = ["maya_work.png", "figma_work.png", "blender_work.png", "photoshop_work.png", "illustrator_work.jpg"]

        for icon, image_path in zip(tool_icons, tool_images):
            button = QPushButton()
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(64, 64))
            button.setFixedSize(64, 64)
            button.clicked.connect(lambda checked, image_path=image_path: self.display_image(image_path))
            tools_layout.addWidget(button)

        tools_and_image_layout.addLayout(tools_layout)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        tools_and_image_layout.addWidget(self.image_label)

        ai_layout = QVBoxLayout()
        ai_tools = ["Красивизатор 9000", "Midjorney", "Leonardo AI"]

        ai_label = QLabel("AI-инструменты:")
        ai_label.setAlignment(Qt.AlignCenter)
        ai_layout.addWidget(ai_label)

        for ai_tool in ai_tools:
            ai_button = QPushButton(ai_tool)
            ai_image_path = f"{ai_tool.lower()}_work.png"
            ai_button.clicked.connect(lambda checked, image_path=ai_image_path: self.display_image(image_path))
            ai_layout.addWidget(ai_button)

        tools_and_image_layout.addLayout(ai_layout)

        main_layout.addLayout(tools_and_image_layout)
        self.central_widget.setLayout(main_layout)


        share_button.clicked.connect(self.open_share_window)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToHeight(600)
        self.image_label.setPixmap(pixmap)

    def open_share_window(self):
        if self.share_window is None or not self.share_window.isVisible():
            self.share_window = ShareWindow("selected_work.png")
            self.share_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThreeDArtWindow()
    window.show()
    sys.exit(app.exec())
