import csv,datetime

def time_now():
    now = datetime.datetime.now()
    time_now = now.strftime('%Y-%m-%d %H:%M:%S')
    return time_now

def w_text(str):
    now = datetime.datetime.now()
    time_new = now.strftime('%Y-%m-%d')
    filename = time_new + '.txt'
    text = open(filename,'ab')
    text.writelines(time_now()+' '+ str+'\n')
    text.close()

# filename = 'foo.txt'
# with open(filename) as f:
#     dat = f.read()
#     for each in dat:
#         print each
    # jam = dat.split(',')
    # james = dat.strip().split(',')
    # print james
    # print jam

def w_sort():
    data = [1,3,2,4,5,8,7]
    c = sorted(data)
    c.sort()
    print data
    print c
    data.sort()
    print data


# csv_reader = csv.reader(open('cc.csv'))
# for row in csv_reader:
#     print row
#     print row[0],row[1]







