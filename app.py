from PyQt5 import QtCore, QtGui, QtWidgets
from cpu_freq import Ui_MainWindow
from cpu_frame import MojWid
from subprocess import Popen, PIPE
import time
import sys
import threading

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget_list = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_headline()
        self.init_cpus()
        self.sthread = SThread()
        self.sthread.signal.connect(self.update_gui)
        self.sthread.start()
        
    def init_headline(self):
        headlineProc = Popen('cat /proc/cpuinfo | grep model\ name | sort --unique', shell=True, stdout=PIPE)
        headline = headlineProc.communicate()[0].decode("utf-8").split(': ')[1].split(' CPU')[0]
        self.ui.label.setText(headline)

    def init_cpus(self):
        out = Popen('cat /proc/cpuinfo | grep cpu\ M', shell=True, stdout=PIPE)
        cpuFrequesList = out.communicate()[0].decode("utf-8").split('\n')
        aggDisp = ''
        for index, line in enumerate(cpuFrequesList):
                if ':' in line:
                    mojwi = MojWid()
                    mojwi.label_2.setText(f'  CPU {index}: ')
                    self.widget_list.append(mojwi)
                    self.ui.MainLayout.addWidget(mojwi)


    def update_gui(self, result):
        cpu_temp_list = result['cpu_temp_list']
        cpu_freq_list = result['cpu_freq_list']
        temp_arr = ''
        agg_disp = ''
        
        for index, line in enumerate(cpu_temp_list):
            if 'high' in line:
                if 'Pack' not in line:
                    temp_arr += line.split('(h')[0].split(': ')[1].strip() + ';'
        
        for index, line in enumerate(cpu_freq_list):
                if ':' in line:
                    agg_disp += str(index) + line.split(': ')[1]
                    self.widget_list[index].label_3.setText(line.split(': ')[1] + ' Mh/z')
                    self.widget_list[index].textBrowser_2.setText(temp_arr.split(';')[int(index/2)])
                    self.widget_list[index]
        self.sthread.update_time = self.ui.horizontalSlider.value() / 100
            

class SThread(QtCore.QThread):
    signal = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.update_time = 0

    def run(self):
        print('started thread')
        while True:
            temp = Popen('sensors | grep °C', shell=True, stdout=PIPE)
            cpu_temp_list = temp.communicate()[0].decode("utf-8").split('\n')
                         
            
            out = Popen('cat /proc/cpuinfo | grep cpu\ M', shell=True, stdout=PIPE)
            cpu_freq_list = out.communicate()[0].decode("utf-8").split('\n')
            
            self.signal.emit({'cpu_temp_list': cpu_temp_list, "cpu_freq_list": cpu_freq_list})
            time.sleep(self.update_time)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
