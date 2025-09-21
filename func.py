import ui
import os
from PySide6.QtWidgets import QFileDialog, QApplication, QMainWindow, \
    QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
import logging
logger = logging.getLogger(__name__)

def choose_file(root,  title: str, filter: str):
    """
    打开一个文件 getOpenFileName
    该方法返回值 是一个元组，第一个元素是选择的文件路径，第二个元素是文件类型，
    如果你只想获取文件路径即可，可以采用下面的代码写法。
    如果用户点击了 选择框的 取消选择按钮，返回 空字符串
    :return: str 选择的文件路径
    """
    file_path,_ = QFileDialog.getOpenFileName(
        root,  # 父窗口对象
        title,  # 标题
        os.getcwd(),  # 起始目录
        filter,  # 选择类型过滤项，过滤内容在括号中
    )
    return file_path

def messaagebox(root, title, message):
    """
    显示一个消息框
    :param root: 父窗口对象
    :param title: 窗口标题
    :param message: 窗口内容
    :return:
    """
    QMessageBox.information(root, title, message)

def generate_lrc(time_static: list[int], lyrics: list[str], delay: int, u3d: bool =  False):
    temp = ""
    for x in lyrics:
        temp += x
    logger.info("Receive time:" + str(len(time_static)) + "lrc:" + str(len(temp)))
    ans = ""
    stime = []
    for x in time_static:
        x += delay
        if x < 0:
            x = 0
        stime.append("[%s:%s.%s]" % (str(int(x//60000)).zfill(2),
                                     str(int(x%60000//1000)).zfill(2),
                                     str(int(x%1000//10)).zfill(2) if not u3d else str(int(x%1000)).zfill(3)))
    for i in range(len(stime)):
        ans += stime[i] + temp[i]
    return ans