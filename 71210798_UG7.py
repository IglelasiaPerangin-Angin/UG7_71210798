class StackList:
    def __init__(self):
        self.stack_data = list()

    def push(self, new_data):
        self.stack_data.append(new_data)

    def top(self):
        if len(self.stack_data) ==0:
            return None
        else:
            return self.stack_data[-1]

    def pop(self):
        if len(self.stack_data) == 0:
            return None
        else:
            pop_data = self.stack_data.pop()
            return pop_data

    def size(self):
        return len(self.stack_data)
class UndoRedo:
    def __init__(self):
        self.mainStack = StackList() #stack ini sebagai tempat menyimpan data pertama kali
        self.backupStack = StackList() #stack ini sebagai tempat menyimpan data yang di hapus

    def write(self,data):
        """Pada Suatu Hari hiduplah seorang kakek-kakek"""
        return self._history

    def undo(self):
         """Dia tinggal sebatang kara di pegunungan"""
        if self._history_position > 0:
            self._history_position -= 1
            self._commands[
                self._history[self._history_position][1]
            ].execute(self._history[self._history_position][2])
        else:
            print("nothing to undo")

    def redo(self):
        """Dia kemudian turun gunng buat kuliah"""
        if self._history_position + 1 < len(self._history):
            self._history_position += 1
            self._commands[
                self._history[self._history_position][1]
            ].execute(self._history[self._history_position][2])
        else:
            print("nothing to REDO")

    def printInfo(self):
        print("nothing to REDO")
