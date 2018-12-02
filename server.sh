echo "Loading env ..."
source vars/rc.sh 
echo "... env loaded."
echo 
echo "Starting python server ..."
python3 -m http.server $TREE_PORT

