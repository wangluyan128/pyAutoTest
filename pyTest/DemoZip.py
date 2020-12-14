import os
import sys
import zipfile

#��ȡ�ű�·��, �������IDE�����У�ֻ���ô˷�ʽ��ȡ
def get_cur_dir():
    path = sys.path[0]
    #�ж�Ϊ�ű��ļ�����py2exe�������ļ�������ǽű��ļ����򷵻ص��ǽű���Ŀ¼�������py2exe�������ļ����򷵻ص��Ǳ������ļ�·��
    if os.path.isdir(path):
        return path

    elif os.path.isfile(path):
        return os.path.dirname(path)

def recurse_files(input_path, result):
    files = os.listdir(input_path)

    for file in files:
        if os.path.isdir(os.path.join(input_path,file)):
            if file != 'users': #�����ļ���
                recurse_files(os.path.join(input_path,file), result)
        else:
            ext = os.path.splitext(file)[1]
            if input_path == cur_dir:#��Ŀ¼ֻ����ض������ļ�
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
        arcName = file #��ѹ����������
        if os.path.dirname(file) == cur_dir:
            arcName = os.path.basename(file) #�ļ���Ҫѹ��Ŀ¼�£���ֻΪ�ļ���
        else:
            dir = os.path.dirname(file)
            dir = dir.replace(cur_dir + '\\', '') #ֻ��Ҫѹ����Ŀ¼�µ�ǰĿ¼����ʼ
            arcName = dir + '\\' + os.path.basename(file)

        zip.write(file, arcName)
        #zip.write(file) #�����ȫ·��

    # ������close�����Żᱣ֤���ѹ��
    zip.close()
