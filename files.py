import os.path
import time
import shutil

# 指明被遍历的文件夹
ROOT_DIR = "D:\Files\Dicom"
# 磁盘容量值上限，开始删除文件
START_DELETE_CONST = 0.3
# 磁盘容量值下限，暂停删除文件
STOP_DETELE_CONST = 0.09


# 判断F可以容量是否大于F盘容量的3%
def needDeleteFile():
    total, used, free = shutil.disk_usage("d:/")
    rate = float(free/total)
    print(currentTime()+":当前剩余容量百分比"+str(rate)+"%")
    if rate < START_DELETE_CONST and rate > STOP_DETELE_CONST:
        print("不需要删除")
        return False
    else:
        print("需要删除")
        return True


# 获取当前时间，输出日志使用
def currentTime():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


'''对日期文件进行排序&删除'''
def day_sort_delete_files(rootdir):
    while needDeleteFile():
        # 先排序
        path_list = sort_files(rootdir)
        #检查是否有文件夹& 容量是否够
        if len(path_list) > 0:
            # 删除文件
            try:
                shutil.rmtree(path=os.path.join(rootdir, path_list[0]))
            except:
                print("删除失败")
        else:
            shutil.rmtree(path=rootdir)
            break


'''对文件进行排序'''
def sort_files(rootdir):
    path_list = os.listdir(rootdir)
    path_list.sort()
    print(path_list)
    return path_list


if __name__ == "__main__":
    while needDeleteFile():
        # 对指定文件夹进行排序
        month_list = sort_files(ROOT_DIR)
        if len(month_list) > 0:
            if os.listdir(os.path.join(ROOT_DIR, month_list[0])):
                # 遍历日期->刪除日期->检查是否暂停
                day_sort_delete_files(os.path.join(
                    ROOT_DIR, month_list[0]))
            else:
                # 存在文件夹
                if len(month_list) > 0:
                    # 取最小月份
                    print(month_list[0])
                    # 月份文件夹为null删除
                    shutil.rmtree(os.path.join(ROOT_DIR, month_list[0]))
