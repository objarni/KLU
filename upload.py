def run():
    from ftplib import FTP
    from getpass import getpass
    
    print("Upload script for KLU.")
    print("This script will update the appropriate files on the remote FTP server.")
    password = getpass("Enter FTP password:")
    if not password:
        return
    ftp = FTP()
    ftp.connect('ftpcluster.loopia.se')
    try:
        ftp.login('olofbjarnason.se', password)
    except:
        print("Password incorrect. Aborting.")
        return

    ftp.cwd('olofbjarnason.se/public_html/cgi-bin/0004')
    ftp.sendcmd('TYPE i')
    files = ['klu.py', 'webklu.py', 'desc.py']
    for file in files:
        upload_file(ftp, file)
    ftp.quit()

def upload_file(ftp, file):
    print('Uploading ' + file + ' ...')
    try: ftp.delete(file)
    except: pass
    f = open(file, 'r')
    ftp.storlines('STOR ' + file, f)
    ftp.voidcmd('SITE CHMOD 755 ' + file)
    f.close()
    print('Done.')

if __name__ == "__main__":
    run()
