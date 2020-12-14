import os
import sys
import zipfile

#获取脚本路径, 如果是在IDE下运行，只能用此方式获取
def get_cur_dir():
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path

    elif os.path.isfile(path):
        return os.path.dirname(path)

def recurse_files(input_path, result):
    files = os.listdir(input_path)

    for file in files:
        if os.path.isdir(os.path.join(input_path,file)):
            if file != 'users': #过滤文件夹
                recurse_files(os.path.join(input_path,file), result)
        else:
            ext = os.path.splitext(file)[1]
            if input_path == cur_dir:#根目录只添加特定类型文件
                if ext == '.dll' or ext == '.exe' or ext == '.qm':
                    result.append(os.path.join(input_path,file))
            else:
                result.append(os.path.join(input_path,file))

if __name__ == '__main__':
    cur_dir = get_cur_dir()

    zip_file_name = os.path.join(cur_dir, 'debug.zip');
    if os.path.isfile(zip_file_name): os.remove(zip_file_name)
    zip = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    filelists = []
    recurse_files(cur_dir, filelists)

    for file in filelists:
        arcName = file #在压缩包内名字
        if os.path.dirname(file) == cur_dir:
            arcName = os.path.basename(file) #文件在要压缩目录下，则只为文件名
        else:
            dir = os.path.dirname(file)
            dir = dir.replace(cur_dir + '\\', '') #只从要压缩的目录下当前目录名开始
            arcName = dir + '\\' + os.path.basename(file)

        zip.write(file, arcName)
        #zip.write(file) #会出现全路径

    # 调用了close方法才会保证完成压缩
    zip.close()
