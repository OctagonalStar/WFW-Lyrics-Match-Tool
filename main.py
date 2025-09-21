import ui
import func
import sys
import time
import logging


def setup_logging():
    # 创建自定义格式器
    formatter = logging.Formatter(
        fmt="%(asctime)s\t[%(levelname)s]\t|%(name)s|\t: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logger.addHandler(console_handler)

    # file_handler = logging.FileHandler("app.log", encoding="utf-8")
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    app = ui.QApplication(sys.argv)
    gui = ui.Ui_root()
    root = ui.QMainWindow()
    gui.setupUi(root)
    root.show()
    sys.exit(logger.info("Normally Exiting...") if app.exec() == 0 else logger.error("An Exception Happened Exiting..."))

