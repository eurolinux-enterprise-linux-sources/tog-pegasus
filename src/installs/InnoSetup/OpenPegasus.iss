; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

; define the macros for repository directory and the namespaces here.

#define REPOSITORY "'repository'"
#define NS_PG_INTERNAL "'root/PG_Internal'"
#define NS_PG_INTEROP  "'root/PG_InterOp'"
#define NS_CIMV2 "'root/cimv2'"

; define the Schema version to be used for building up the repository.
#define VER "'27'"

; define the OpenPegasus version for the installable
#define OPEN_PEGASUS_VERSION "2.4"

#define SystemRootdir  ReadReg(HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion","SystemRoot")
#define PegasusRootDir GetEnv('PEGASUS_HOME')


[Registry]
Root: HKLM; Subkey: "Software\OpenPegasus"; Flags: createvalueifdoesntexist uninsdeletekey
Root: HKLM; Subkey: "Software\OpenPegasus"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"
Root: HKLM; Subkey: "Software\OpenPegasus"; ValueType: string; ValueName: "Version"; ValueData: "{#OPEN_PEGASUS_VERSION}"
Root: HKLM; Subkey: SYSTEM\CurrentControlSet\Control\Session Manager\Environment;ValueType: expandsz; ValueName: Path; ValueData: "{reg:HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment,Path};{app}\OpenPegasus\bin"

[Setup]
AppName=OpenPegasus
AppVerName=OpenPegasus {#OPEN_PEGASUS_VERSION}
AppPublisher=Open Pegasus Community
AppPublisherURL=http://www.openpegasus.org
AppSupportURL=http://www.openpegasus.org
AppUpdatesURL=http://www.openpegasus.org
DefaultDirName={pf}\OpenPegasus
DefaultGroupName=OpenPegasus

[Files]
Source: "{#PegasusRootDir}\bin\cimserver.exe" ; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\UserAuthProvider.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegCLIClientLib.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegclient.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegcliutils.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegcommon.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegcompiler.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegconfig.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegexportclient.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegexportserver.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\peggetoopt.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\peghandlerservice.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegindicationservice.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\peglistener.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegprm.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegprovider.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegprovidermanager.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegrepository.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegserver.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\peguser.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegwql.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\ProviderRegistrationProvider.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\pegauthentication.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\OSProvider.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\ConfigSettingProvider.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\NamespaceProvider.dll"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
; System files
Source: "{#SystemRootdir}\system32\msvcp71.dll"; DestDir: "{app}\OpenPegasus\bin"; Check: MSVCPlusPlusDotNetInstalled
Source: "{#SystemRootdir}\system32\msvcr71.dll"; DestDir: "{app}\OpenPegasus\bin"; Check: MSVCPlusPlusDotNetInstalled
; With the above files cimserver runs

; This is for schemas
Source: "{#PegasusRootDir}\Schemas\*.*"; DestDir: "{app}\OpenPegasus\Schemas"; Flags: ignoreversion recursesubdirs
;Other seven CIMServer Utilities
Source: "{#PegasusRootDir}\bin\cimmof.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\cimmofl.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\cimauth.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\cimprovider.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\cimconfig.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
Source: "{#PegasusRootDir}\bin\cimuser.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion

; The following are the test clients, to add more clients to your installable, refer to commented lines below.
Source: "{#PegasusRootDir}\bin\CLI.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
;Source: "{#PegasusRootDir}\bin\WebClient.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
;Source: "{#PegasusRootDir}\bin\wbemexec.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
;Source: "{#PegasusRootDir}\bin\CGIClient.exe"; DestDir: "{app}\OpenPegasus\bin"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

; The following are optional sections for future usage. Refer to help file of Inno Setup for help on these sections.
[InstallDelete]

[INI]

[Tasks]

[Icons]

[Run]
; NOTE: The following entry contains an English phrase ("Launch"). You are free to translate it into another language if required.
Filename: "{app}\OpenPegasus\bin\cimserver.exe"; Parameters: " -install"; BeforeInstall: InformUser; Check: CIMServerAsWINService
Filename: "{app}\OpenPegasus\bin\cimserver.exe"; Parameters: " -start"; Check: CIMServerAsWINService; AfterInstall: BuildRepository
Filename: "{app}\OpenPegasus\bin\cimserver.exe"; Parameters: " "; Flags: nowait; BeforeInstall: InformUser; Check: CIMServerAsAnExe; AfterInstall: BuildRepository

[UninstallDelete]
Type: filesandordirs; Name: "{app}\OpenPegasus"

[UninstallRun]
Filename: "{app}\OpenPegasus\bin\cimserver.exe"; Parameters: " -stop"; Check: CIMServiceExists
Filename: "{app}\OpenPegasus\bin\cimserver.exe"; Parameters: " -remove" ; Check: CIMServiceExists

; If the user chooses not to install cimserver as a windows service, then we give a wait of 10000 milliseconds
; so that before the repository starts getting builded , cimserver is started. CIMMOFL doesn't seem to help here.
[Code]

var
  Cimservice: Boolean;

procedure InformUser();
begin
MsgBox('There will be a series of Dos prompts opening and closing before the installation finishes, this may take some time.',mbInformation,MB_OK);
end;

procedure BuildRepository();
var
appPath, params,dirname,filename,cimmof : String;
resultCode: Integer;
begin
appPath := ExpandConstant('{app}') + '\OpenPegasus';
cimmof := appPath + '\bin\cimmof.exe';
AddQuotes(cimmof);

if not Cimservice then
   MsgBox('Please wait until Cimserver starts (Cmd prompt will show "Cimserver 2.4 , started".',mbInformation,MB_OK);

dirname := appPath + '\Schemas\CIM' + {#VER};
filename := appPath+ '\Schemas\CIM' + {#VER} + '\Core' + {#VER}+'_Qualifiers.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_PG_INTERNAL} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\Pegasus\Internal\VER20';
filename := appPath+ '\Schemas\Pegasus\Internal\VER20\PG_InternalSchema20.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_PG_INTERNAL} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\CIM' + {#VER};
filename := appPath+ '\Schemas\CIM' + {#VER} + '\CIM_Core' + {#VER}+'.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_PG_INTEROP} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\CIM' + {#VER};
filename := appPath+ '\Schemas\CIM' + {#VER} + '\CIM_Event' + {#VER}+'.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_PG_INTEROP} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\Pegasus\InterOP\VER20';
filename := appPath+ '\Schemas\Pegasus\InterOp\VER20\PG_InterOpSchema20.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_PG_INTEROP} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\CIM' + {#VER};
filename := appPath+ '\Schemas\CIM' + {#VER} + '\CIM_Schema' + {#VER}+'.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_CIMV2} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\Pegasus\ManagedSystem\VER20';
filename := appPath+ '\Schemas\Pegasus\ManagedSystem\VER20\PG_ManagedSystemSchema20.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_CIMV2} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

dirname := appPath + '\Schemas\Pegasus\ManagedSystem\VER20';
filename := appPath+ '\Schemas\Pegasus\ManagedSystem\VER20\PG_ManagedSystemSchema20R.mof';
params := ' -R  ' + {#REPOSITORY} + ' -I  ' + AddQuotes(dirname) +' -n  ' + {#NS_PG_INTEROP} + '  ' + AddQuotes(filename);
InstExec(cimmof,params, appPath, True, False, SW_SHOWNORMAL, resultCode);

end;

function InitializeSetup(): Boolean;
var
OpenPegasusFound: Boolean;
str : String;
begin
str :=  'SOFTWARE\OpenPegasus';
OpenPegasusFound := RegKeyExists(HKLM,str);
if not OpenPegasusFound then
begin
  Result := True
  Cimservice := MsgBox('Would you like to install OpenPegasus as a Windows Service', mbConfirmation, MB_YESNO) = idYes;
end
else
begin
   MsgBox('OpenPegasus is already installed , please uninstall the old version first.(Setup will exit)',mbInformation,MB_OK);
   Result := False;
end
end;

function NeedRestart(): Boolean;
begin
  Result := True
end;

function MSVCPlusPlusDotNetInstalled(): Boolean;
begin
Result := True;
if FileExists(ExpandConstant('{#SystemRootDir}\System32\msvcp71.dll')) then
  begin
    if FileExists(ExpandConstant('{#SystemRootDir}\System32\msvcp71.dll')) then
      begin
        Result := False;
      end;
  end;
end;

function CIMServerAsWINService: Boolean;
begin
Result := Cimservice;
end;

function CIMServerAsAnExe: Boolean;
begin
  Result := False;
if not Cimservice then
begin
  Result := True;
end;
end;

function CIMServiceExists:Boolean;
begin
  Result := False;
if Cimservice then
begin
  Result := True;
end;
end;










