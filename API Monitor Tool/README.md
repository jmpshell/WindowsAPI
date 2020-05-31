# API Monitor Tool

This small tool was developed in partnership with Van Souza - idHreusen.
<br>Its goal is to extract suspicious APIs from Windows binaries.

 ## Pre requirements:
     pip install r2pipe    


 ## Output examples:

**--> amazon invoice.exe**

     AdjustTokenPrivileges
     GetProcAddress
     FindClose
     CloseHandle
     ExitProcess
     LoadResource
     WaitForSingleObject
     SetEvent
     SetFileTime
     WriteFile
     ResetEvent
     CreateThread
     SetFilePointer
     UnhandledExceptionFilter
     ReadFile
     GetDC

**--> jj.exe**
     
     ExitProcess
     GetProcAddress
     VirtualProtect

**--> OneDrive.exe**
     
     IsDebuggerPresent
     UnhandledExceptionFilter
     ExitProcess
     HeapQueryInformation
     VirtualQuery
     VirtualAlloc
     HeapSetInformation
     GetFileInformationByHandle
     HeapAlloc
     HeapAlloc
     CreateThread
     ExitThread
     HeapFree
     VirtualProtect
     InitializeCriticalSectionAndSpinCount
     GetFileTime
     GetFileSizeEx
     HeapReAlloc
     InterlockedExchange
     FindClose
     SetEndOfFile
     SetFilePointer
     WriteFile
     ResumeThread
     WideCharToMultiByte
     LoadResource
     TlsFree
     TlsSetValue
     TlsAlloc
     TlsGetValue
     WaitForMultipleObjects
     GetProcAddress
     ReadFile
     PeekNamedPipe
     CloseHandle
     WaitForSingleObject
     DeleteCriticalSection
     EnterCriticalSection
     LeaveCriticalSection
     GetAsyncKeyState
     GetForegroundWindow
     GetDC
     GetKeyState
     BitBlt
     WSAStartup

**--> Revance.exe**

     HeapReAlloc
     VirtualAlloc
     HeapAlloc
     HeapAlloc
     InitializeCriticalSectionAndSpinCount
     LeaveCriticalSection
     EnterCriticalSection
     CloseHandle
     WaitForSingleObject
     CreateThread
     UnhandledExceptionFilter
     IsDebuggerPresent
     GetProcAddress
     ExitProcess
     WriteFile
     WideCharToMultiByte
     DeleteCriticalSection
     TlsGetValue
     TlsAlloc
     TlsSetValue
     TlsFree
     VirtualFree
     HeapFree
     SetFilePointer


**--> VisualizarBO.exe**

     DeleteCriticalSection
     LeaveCriticalSection
     EnterCriticalSection
     VirtualFree
     VirtualAlloc
     WideCharToMultiByte
     TlsSetValue
     TlsGetValue
     WriteFile
     SetFilePointer
     SetEndOfFile
     ReadFile
     ExitProcess
     CloseHandle
     WriteFile
     VirtualQuery
     VirtualProtect
     VirtualFree
     VirtualAlloc
     SetFilePointer
     SetEndOfFile
     ReadFile
     LoadResource
     GetProcAddress
     InterlockedExchange
     CloseHandle
     AdjustTokenPrivileges

