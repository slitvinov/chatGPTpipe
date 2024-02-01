rm -f i; mkfifo i
python -u main.py < i | tee chat.log &
tail -f /dev/null > i &
