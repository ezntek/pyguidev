if test -f "/usr/local/bin/python3"; then
    pip3 install tk
    cp main.py dist.py
    echo "#!/usr/local/bin/python3" | cat - dist.py | tee dist.py
    mkdir dist.app
    chmod +x dist.py
    mv dist.py dist.app/dist
else
    echo "install python into /usr/local/bin (with the python.org site installer) first!"
fi