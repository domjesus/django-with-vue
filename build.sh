echo '...Run npm build'
npm run build
echo '...Done...'

echo '...Format index.html as Jinja template'
py format_index_html.py
echo '...Done...'

echo '...Collect static'
py manage.py collectstatic --noinput
echo '...Done...'

echo '...Run migrations'
py manage.py migrate
echo '...Done...'
