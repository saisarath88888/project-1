
set -e

URL="https://stackoverflow.com/questions"
USER="$(git remote show origin | grep Fetch | grep -o 'https://github.com/[^\/]*')"
DATE="$(date "+%Y/%m/%d")"
DIR="history/$(dirname $DATE)"
FILE="$(basename $DATE)"

mkdir -p $DIR
curl "$URL" > "$DIR/$FILE"

git config --global user.email "histgen-bot@meain.io"
git config --global user.name "Histgen"

git add .
git commit -m "$DATE"
git push origin master
