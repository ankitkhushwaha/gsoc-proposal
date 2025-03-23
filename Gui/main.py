# from PyQt6.QtWidgets import *
# from PyQt6.QtGui import QFont


# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setWindowTitle('ANkit')
#     window.setGeometry(100,100, 200,300)

#     label = QLabel(window)
#     label.setText('Hello world')
#     label.setFont(QFont('Arial', 20))
#     label.move(100,100)
#     window.show()
#     app.exec()





# if __name__=='__main__':
#     main()

# from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt6.QtWebEngineWidgets import QWebEngineView
# from PyQt6.QtCore import QUrl
# import sys

# # from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# # from PyQt6.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
# # from PyQt6.QtCore import QUrl
# # import sys
# class RestrictedWebPage(QWebEngineView):
#     """ Custom WebPage to restrict navigation to only one domain """
#     ALLOWED_DOMAIN = "example.com"  # Change this to your allowed website

#     def acceptNavigationRequest(self, url, _type, isMainFrame):
#         if self.ALLOWED_DOMAIN in url.toString():
#             return super().acceptNavigationRequest(url, _type, isMainFrame)
#         return False  # Block other websites
    
# class Browser(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Python Web Browser")
#         self.setGeometry(100, 100, 1200, 800)

#         # Create a WebEngineView
#         self.browser = QWebEngineView()
#         self.browser.setPage(RestrictedWebPage(self))  #
#         self.browser.setUrl(QUrl("https://www.google.com"))  #

#         # Set layout
#         container = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(self.browser)
#         container.setLayout(layout)
#         self.setCentralWidget(container)

# # Run the application
# app = QApplication(sys.argv)
# window = Browser()
# window.show()
# sys.exit(app.exec())

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys

class Browser(QMainWindow):
    ALLOWED_DOMAIN = "google.com"  # Change this to your allowed website

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restricted Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Create WebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(f"https://{self.ALLOWED_DOMAIN}"))  # Allowed website

        # Connect navigation event to restriction function
        self.browser.page().navigationRequested.connect(self.handle_navigation)

        # Set layout
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_navigation(self, request):
        """ Restrict navigation to only one domain """
        url = request.url().toString()
        if self.ALLOWED_DOMAIN not in url:
            print(f"Blocked navigation to: {url}")
            request.reject()  # Block navigation
        else:
            request.accept()  # Allow navigation

# Run the application
app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec())
