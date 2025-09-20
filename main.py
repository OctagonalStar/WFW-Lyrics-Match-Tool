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

    # 获取根logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 移除所有现有的处理器
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # 添加新的处理器
    logger.addHandler(console_handler)

    # 可选：创建文件处理器
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

