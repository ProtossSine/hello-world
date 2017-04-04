url = 'http://tb-video.bdstatic.com/tieba-smallvideo-transcode/91_c947ee06d11a3e25029f046103ac0cb4_3.mp4?authorization=bce-auth-v1%2Fde94045c2e42438fad71ab8df47a6727%2F2017-03-18T02%3A47%3A25Z%2F1800%2F%2Fc6c56ca7c1ca412cf7a7d94c800d487e07662385d3306b7a76bb2dba21fa3b15'
root = "G://DataScraping//"
path = root + url.split('/')[-1].split('?')[0]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('save successfully')
    else:
        print('file existed')
except:
    print('failed')
