# QUERY="YOUR_MYSQL_QUERY_HERE"
QUERY=$(xclip -o)
echo -e '\n' $QUERY
read -p "Please Enter any key to proceed: " aa

if mysql \
	-u 'lfdfrontier' \
	-h 'mysqlfrontier-dev-flexible.mysql.database.azure.com'  \
	-p'9xH9YAf6HJYH54J'  \
	-D'burquestores'  \
	-e "$QUERY" \
	; then
	play -n synth 1.0 sine 1000
else
    play -n synth 1.0 sine 1000
fi
