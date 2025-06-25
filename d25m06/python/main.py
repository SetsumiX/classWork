import os
import shutil

# folder = r"D:\Влад_Python5\secondPy\start\d25m06"
#
# data = {
#     "image": ["png", "jpeg", "jpg"],
#     "move": ["mp4", "mpeg", "avi", "mov"],
#     "sound": ["mp3", "aac"],
#     "text": ["txt", "doc"],
#     "book": ["pdf", "fb2"]
# }
#
# content = os.listdir(folder)
#
# # def show(path):
# #     for i in path:
# #         print(i)
# #
# # show(content)
#
# def move(i, catalog, folder):
#     ext = i.split(".")[-1].lower()
#
#     for k, v in catalog.items():
#         subdir = os.path.join(folder, k)
#         if not os.path.isdir(subdir):
#             os.makedirs(subdir, exist_ok=True)
#         if ext in v:
#             shutil.move(os.path.join(folder, i), os.path.join(subdir, i))
#             print(f"Файл {i} перемещён в папку {k}. Путь: {subdir}")
#             break
#
# for i in content:
#     move(i, data, folder)

folder = r"D:\Влад_Python5\secondPy\start\d25m06"

data = {
    "image": ["png", "jpeg", "jpg"],
    "move": ["mp4", "mpeg", "avi", "mov"],
    "sound": ["mp3", "aac"],
    "text": ["txt", "doc"],
    "book": ["pdf", "fb2"],
    "python": ["py"]
}

class File_Mover:
    def __init__(self, pathFolder, data):
        self._pathFolder = pathFolder
        self._data = data
        self._content = os.listdir(self._pathFolder)


    def show(self):
        for i in self._content:
            print(i)

    def sort(self):
        for i in self._content:
            ext = i.split(".")[-1].lower()

            for k, v in self._data.items():
                subdir = os.path.join(self._pathFolder, k)
                if not os.path.isdir(subdir):
                    os.makedirs(subdir, exist_ok=True)
                if ext in v:
                    shutil.move(os.path.join(self._pathFolder, i), os.path.join(subdir, i))
                    print(f"Файл {i} перемещён в папку {k}. Путь: {subdir}")
                    break

filesDir = File_Mover(folder, data)
filesDir.show()
filesDir.sort()
