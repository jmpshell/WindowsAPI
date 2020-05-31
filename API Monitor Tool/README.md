# API Monitor Tool

This small tool was developed in partnership with Van Souza - idHreusen.
<br>Its goal is to extract suspicious APIs from Windows binaries.

 ## Pre requirements:
     pip install r2pipe    


 ## Output examples:

**--> amazon invoice.exe**

AdjustTokenPrivileges<br>
GetProcAddress<br>
FindClose<br>
CloseHandle<br>
ExitProcess<br>
LoadResource<br>
WaitForSingleObject<br>
SetEvent<br>
SetFileTime<br>
WriteFile<br>
ResetEvent<br>
CreateThread<br>
SetFilePointer<br>
UnhandledExceptionFilter<br>
ReadFile<br>
GetDC<br>

**--> jj.exe**

ExitProcess<br>
GetProcAddress<br>
VirtualProtect<br>

**--> OneDrive.exe**

IsDebuggerPresent<br>
UnhandledExceptionFilter<br>
ExitProcess<br>
HeapQueryInformation<br>
VirtualQuery<br>
VirtualAlloc<br>
HeapSetInformation<br>
GetFileInformationByHandle<br>
HeapAlloc<br>
HeapAlloc<br>
CreateThread<br>
ExitThread<br>
HeapFree<br>
VirtualProtect<br>
InitializeCriticalSectionAndSpinCount<br>
GetFileTime<br>
GetFileSizeEx<br>
HeapReAlloc<br>
InterlockedExchange<br>
FindClose<br>
SetEndOfFile<br>
SetFilePointer<br>
WriteFile<br>
ResumeThread<br>
WideCharToMultiByte<br>
LoadResource<br>
TlsFree<br>
TlsSetValue<br>
TlsAlloc<br>
TlsGetValue<br>
WaitForMultipleObjects<br>
GetProcAddress<br>
ReadFile<br>
PeekNamedPipe<br>
CloseHandle<br>
WaitForSingleObject<br>
DeleteCriticalSection<br>
EnterCriticalSection<br>
LeaveCriticalSection<br>
GetAsyncKeyState<br>
GetForegroundWindow<br>
GetDC<br>
GetKeyState<br>
BitBlt<br>
WSAStartup<br>

**--> Revance.exe**

HeapReAlloc<br>
VirtualAlloc<br>
HeapAlloc<br>
HeapAlloc<br>
InitializeCriticalSectionAndSpinCount<br>
LeaveCriticalSection<br>
EnterCriticalSection<br>
CloseHandle<br>
WaitForSingleObject<br>
CreateThread<br>
UnhandledExceptionFilter<br>
IsDebuggerPresent<br>
GetProcAddress<br>
ExitProcess<br>
WriteFile<br>
WideCharToMultiByte<br>
DeleteCriticalSection<br>
TlsGetValue<br>
TlsAlloc<br>
TlsSetValue<br>
TlsFree<br>
VirtualFree<br>
HeapFree<br>
SetFilePointer<br>


**--> VisualizarBO.exe**

DeleteCriticalSection<br>
LeaveCriticalSection<br>
EnterCriticalSection<br>
VirtualFree<br>
VirtualAlloc<br>
WideCharToMultiByte<br>
TlsSetValue<br>
TlsGetValue<br>
WriteFile<br>
SetFilePointer<br>
SetEndOfFile<br>
ReadFile<br>
ExitProcess<br>
CloseHandle<br>
WriteFile<br>
VirtualQuery<br>
VirtualProtect<br>
VirtualFree<br>
VirtualAlloc<br>
SetFilePointer<br>
SetEndOfFile<br>
ReadFile<br>
LoadResource<br>
GetProcAddress<br>
InterlockedExchange<br>
CloseHandle<br>
AdjustTokenPrivileges<br>

