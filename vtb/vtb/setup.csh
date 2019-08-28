
if ( -d ~/.vtb) then
    rm -rf ~/.vtb
    mkdir ~/.vtb
else
    mkdir ~/.vtb
endif 



cp -r skill ~/.vtb/
cp -f cdsinit  ~/.cdsinit


