
import fcntl, os

from PyObjCTools.AppHelper import callLater, runEventLoop
from PyObjCTools.Debugging import installVerboseExceptionHandler

def showblocking():
    print(
        fcntl.fcntl(1, fcntl.F_GETFL) & os.O_NONBLOCK,
        fcntl.fcntl(2, fcntl.F_GETFL) & os.O_NONBLOCK,
    )


installVerboseExceptionHandler()
callLater(1.0, showblocking)
runEventLoop()
