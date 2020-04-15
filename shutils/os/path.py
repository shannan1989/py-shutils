import os


def cleandir(_dir):
    '''
        清理目录，操作包括：删除.DS_Store文件、删除空目录
        以下目录会被跳过，不做处理：
        .svn
    '''
    if not os.path.isdir(_dir):
        return

    for d in os.listdir(_dir):
        if d == '.svn':
            continue
        if d == '.DS_Store':
            os.remove(os.path.join(_dir, d))
        else:
            path = os.path.join(_dir, d)
            if os.path.isdir(path):
                cleandir(path + os.path.sep)

    if not os.listdir(_dir):
        os.rmdir(_dir)
