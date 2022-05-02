""" Python programme to get the OTA firmware version"""
def ota_version():
    my_string = "CM4 Main Firmware Version"
    f = open(r'/home/lokesh/Desktop/758/random', 'r')
    lines_read = (f.readlines()[-1])
    print(lines_read)
    release = lines_read.rsplit(': ', 1)[-1]
    #print(release)
    release_version = release.rsplit('\\',1)[0]
    return print(release_version)
    #print(release_version)
ota_version()
