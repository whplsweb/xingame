@ECHO OFF
setlocal EnableDelayedExpansion
color 3e
title 新增服務配置
 
PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof
:runas
 
start main.exe
 
echo 執行完畢,任意鍵退出
 
pause >nul
exit