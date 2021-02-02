IFS=$'\n'
cd /home/amir/Dr-israr
for i in `ls`; do 
	cd $i
	f=`ls *.wmv 2>/dev/null | wc -l`
	if [[ $f > 0 ]]; then
		for file in `ls *.wmv`; do
			new_name=`echo $file | sed s:.wmv:.mp3:g | sed s:'Dr. Israr Ahmed - '::g | sed s:' (www.aswatalislam.net)'::g | sed s:' Dr. Israr Ahmed '::g `
			ffmpeg -i $file -acodec libmp3lame -ab 60k $new_name
			DEL -rf "$file"
		done
	fi
	cd ../
done

