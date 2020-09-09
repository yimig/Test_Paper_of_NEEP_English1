import os
import tempfile
import win32api
import win32print
import time

def printer_loading(filename):
    open(filename, "r")
    win32api.ShellExecute(0,"print",filename,'/d:"%s"' % win32print.GetDefaultPrinter(),".",0)

printer_loading("work/2010T2.docx")