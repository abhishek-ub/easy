# We can't just do this in Python because the Python script is a
# subprocess of the terminal, and thus can't change the directory;
# we need to actually change the directory in a shell script.

dir=$(dirname ${BASH_SOURCE[0]})
path=$(python $dir/printPath.py $1)

if [ "$path" = 'None' ]
then
    echo "Couldn't find \"$1\" directory anywhere in the path \"$PWD\""
else
    cd "$path"
fi
