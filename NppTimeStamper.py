import datetime
import re
import math

def timestamper(args):
      editor.setUndoCollection(False)

      currentLang = str(notepad.getCurrentLang())

      if re.search('(JS|CSS)$', currentLang) :
            timestampPattern = '\d{6,8}-\d{2,4}'
            timestampAlreadyExisted = False
            firstVisibleLine = editor.getFirstVisibleLine()
            currentPosition = editor.getCurrentPos()
            currentLine = editor.lineFromPosition(currentPosition)
            newTimestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
            limit = min(30, editor.getLineCount())

            for i in range(0, limit):

                  if re.search(timestampPattern, editor.getLine(i)) :
                        text = re.sub(timestampPattern, newTimestamp, editor.getLine(i))
                        editor.replaceWholeLine(i, text)
                        timestampAlreadyExisted = True

            if timestampAlreadyExisted == False:
                  newTimestampComment = '/*! {0} */'.format(newTimestamp) + '\n\n'
                  editor.insertText(0, newTimestampComment)
                  currentPosition = currentPosition + len(newTimestampComment)

            notepad.menuCommand(MENUCOMMAND.FORMAT_CONV2_UTF_8)
            editor.gotoPos(currentPosition)

      editor.setUndoCollection(True)

notepad.callback(timestamper, [NOTIFICATION.FILEBEFORESAVE])