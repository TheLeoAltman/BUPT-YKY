import shutil

class txt:
    def __init__(self, path, filename):
        out_path = 'trans/' + filename
        in_path = path + '/' + filename
        shutil.copyfile(in_path, out_path)