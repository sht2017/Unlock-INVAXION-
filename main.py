import winreg,win32api,win32con
try:
    invaxionReg=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"SOFTWARE\Aquatrax\INVAXION",0,winreg.KEY_ALL_ACCESS)
except FileNotFoundError:
    win32api.MessageBox(0, "No invaxion data founded! Does invaxion be installed on this computer?\n未找到音灵的游戏数据！ 此电脑上安装了音灵吗？", "Warning",win32con.MB_ICONWARNING)
    exit()
try:
    i=0
    while True:
        if winreg.EnumValue(invaxionReg,i)[0].find("Offline_PlayerSongList")!=-1:
            global index
            index=i
            break
        i+=1
except WindowsError:
    win32api.MessageBox(0, "No invaxion data founded! Have you played invaxion online before April 7th, 2021?\n未找到音灵的游戏数据！ 是否在停服前进行过在线游戏？", "Warning",win32con.MB_ICONWARNING)
    exit()
winreg.SetValueEx(invaxionReg,winreg.EnumValue(invaxionReg,index)[0],0,winreg.REG_BINARY,b'[{"songId":80031},{"songId":80008},{"songId":80011},{"songId":80012},{"songId":80010},{"songId":80034},{"songId":80007},{"songId":80015},{"songId":80013},{"songId":80009},{"songId":80014},{"songId":80019},{"songId":80020},{"songId":80018},{"songId":63122},{"songId":63123},{"songId":63204},{"songId":62005},{"songId":62006},{"songId":63103},{"songId":69008},{"songId":68008},{"songId":68108},{"songId":80002},{"songId":64005},{"songId":69018},{"songId":68002},{"songId":68001},{"songId":82005},{"songId":82006},{"songId":82007},{"songId":82011},{"songId":65102},{"songId":68106},{"songId":64003},{"songId":62021},{"songId":65036}]\x00')
winreg.CloseKey(invaxionReg)
win32api.MessageBox(0, "Unlocked/解锁成功", "Notification",win32con.MB_OK)
