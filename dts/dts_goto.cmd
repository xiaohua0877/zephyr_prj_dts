@echo off

C:\Python37\python.exe  ./extract_dts_includes.py  --dts ../build/stm32f723e_disco.dts_compiled  --yaml ../bindings  --keyvalue ../build/generated_dts_board.conf  --include  ../build/generated_dts_board_unfixed.h


pause