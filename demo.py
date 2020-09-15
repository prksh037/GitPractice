from pywinauto import application
import time

app = application.Application()
app.start('D:\\installers\\Git-2.28.0-64-bit.exe')
app.UserAccountControl.click()