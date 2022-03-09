sh ./build.sh

export PORT=8000
echo '...Server runnning on port ' $PORT
py manage.py runserver $PORT
