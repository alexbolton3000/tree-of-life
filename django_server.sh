cd backend/tree_data/

echo 
echo "Migrations ..."
./manage.py migrate
echo "Starting python server ..."
./manage.py runserver
