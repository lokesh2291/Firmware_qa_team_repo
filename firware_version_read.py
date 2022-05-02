""" Python programme to get the firmware firmware from the latest master code"""
def image():
    my_string = "#define CM4_MAIN_FLASH_VERSION"
    f = open(r'/home/lokesh/Desktop/19_april_master/mark3-firmware-trunk/Version/fw_versions.h', 'r')
    lines_read = f.read()
    st =""
    count = 0
    for item in lines_read.split("\n"):
        if my_string in item:
            st = (item.rsplit(' ',1)[-1]) + "."
            count= count +1
            if (count == 4):
                st = (item.rsplit(' ',1)[-1])
            print(st,end="")
print("Release-",end = "")
image()

