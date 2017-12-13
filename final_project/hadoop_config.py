import sys
import os
import xml.etree.ElementTree
import multiprocessing

#
# Set parameters in respective xml path
#
def set_params(path, options):
    param_tree = xml.etree.ElementTree.parse(path)
    root = param_tree.getroot()
    for property in root:
        if property[0].text in options:
            value = options[property[0].text]
            if value:
                property[1].text = value
    param_tree.write(path)

def main(user_param_file_path):
    user_param_file = open(user_param_file_path, 'r')
    user_param_file = user_param_file.readlines()
    options = {}
    for line in user_param_file:
        if (len(line) > 1) & (line[0] != '*'):
            line = line.split(": ")
            options[line[0]] = line[1].strip('\n')

    options['yarn.nodemanager.resource.cpu-vcores'] = str(multiprocessing.cpu_count())
    options['yarn.nodemanager.resource.memory-mb'] = str(int(os.sysconf('SC_PAGE_SIZE'))*int(os.sysconf('SC_PHYS_PAGES'))/1024/1024)

    set_params('/home/ubuntu/hadoop_hbase_bk/hadoop/etc/hadoop/core-site.xml', options)
    set_params('/home/ubuntu/hadoop_hbase_bk/hadoop/etc/hadoop/hdfs-site.xml', options)
    set_params('/home/ubuntu/hadoop_hbase_bk/hadoop/etc/hadoop/mapred-site.xml', options)
    set_params('/home/ubuntu/hadoop_hbase_bk/hbase/conf/hbase-site.xml',options)
    set_params('/home/ubuntu/hadoop_hbase_bk/hadoop/etc/hadoop/yarn-site.xml',options)


if __name__ == "__main__":
    user_param_file = sys.argv[1]
    main(user_param_file)
