import sys
import os

# Detect app directory (supports normal python script and frozen exe)
if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(os.path.abspath(sys.executable))
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Convert any relative file paths in sys.argv to absolute paths before changing directory
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if os.path.exists(sys.argv[i]):
            sys.argv[i] = os.path.abspath(sys.argv[i])

# 2. Change current working directory to the application directory
# This ensures any assets, relative paths, or local tools are always found
os.chdir(app_dir)

# 3. Setup DLL directory and PATH for libmpv / ffmpeg
if sys.platform == "win32":
    try:
        os.add_dll_directory(app_dir)
    except AttributeError:
        pass
    os.environ["PATH"] = app_dir + os.pathsep + os.environ.get("PATH", "")

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, QEvent, QTimer
from gui import MainWindow

class GlobalDragDropFilter(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.DragEnter or event.type() == QEvent.Type.DragMove:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                return True
        elif event.type() == QEvent.Type.Drop:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                urls = event.mimeData().urls()
                if urls:
                    file_paths = []
                    for url in urls:
                        path = url.toLocalFile()
                        if not path:
                            path = url.toString().replace('file:///', '')
                        if path:
                            file_paths.append(os.path.normpath(path))
                    if self.main_window and file_paths:
                        self.main_window.handle_dropped_files(file_paths)
                return True
        return super().eventFilter(watched, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # Install global filter
    drag_drop_filter = GlobalDragDropFilter(window)
    app.installEventFilter(drag_drop_filter)
    
    window.show()
    
    # Set global tooltip style
    app.setStyleSheet("""
        QToolTip {
            color: white;
            background-color: #2b2b2b;
            border: 1px solid #767676;
            padding: 4px;
        }
    """)
    
    # Process files passed via command line (Explorer "Open With", double click, or CLI)
    valid_extensions = ['.mkv', '.mp4', '.avi']
    cmd_files = [f for f in sys.argv[1:] if os.path.isfile(f) and os.path.splitext(f)[1].lower() in valid_extensions]
    if cmd_files:
        if len(cmd_files) == 1:
            QTimer.singleShot(100, lambda: window.load_file(cmd_files[0]))
        else:
            QTimer.singleShot(100, lambda: window.load_multi_files(cmd_files))
            
    sys.exit(app.exec())
