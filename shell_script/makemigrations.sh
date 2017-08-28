echo "*********************************************************************"
echo "MAKING MIGRATIONS"

echo "Getting virtual env resources .............................."

read -p 'directory to virtual env e.g /var/env/bin/activate' virtualenv

echo Activating virtual env at $virtualenv

source $virtualenv

./manage.py makemigrations --settings setting.dev