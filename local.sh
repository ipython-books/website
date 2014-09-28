cp pelicanconf.py pelicanconf_loc.py
cp pelicanconf.py pelicanconf_pub.py

echo "SITEURL = '/'" | cat - pelicanconf_loc.py > /tmp/out && mv /tmp/out pelicanconf_loc.py
echo "SITEURL = 'http://ipython-books.github.io'" | cat - pelicanconf_pub.py > /tmp/out && mv /tmp/out pelicanconf_pub.py

pelican -r -s=pelicanconf_loc.py &

cd output
python -m http.server &
cd ..
