from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import sys

app = QApplication(sys.argv)
label = QLabel('Drop Shadow Effect')
shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(10)
shadow.setXOffset(5)
shadow.setYOffset(5)
shadow.setColor(QColor(0, 0, 0, 160))
label.setGraphicsEffect(shadow)
label.show()
sys.exit(app.exec_())
