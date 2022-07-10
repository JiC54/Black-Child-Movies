if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/JiC54/Black-Child-Movies.git /Black-Child-Movies
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Black-Child-Movies
fi
cd /Black-Child-Movies
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
