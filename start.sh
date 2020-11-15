

function chei(){
clear
figlet -f smmono9 "EARN MONEY" | lolcat
echo -e $lg " [¥] Checking your Internet Connection "
echo " "
ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" != 0 ]]
then
echo -e $ye " [-] Internet:${re} FAILED"
echo ""
echo -e $lgf "  Active A Internet Connection"
echo ""
echo -e $ye "                Exit"
echo "." | lolcat
sleep 2
exit
else
echo -e $ye " [√] Internet:${lg} CONNECTED"
sleep 2
fi
}

function report(){
gitpull
clear
}


function main(){
clear
echo -e $red"                ◆━━━━━━━▣✦▣━━━━━━━━◆◆━━━━━━━▣✦▣━━━━━━━━◆"
echo -e "           " $ylo"        [1] PLAY GAME.     "           
echo -e "           " $red"        [2] REPORT TO ADMIN.  "
echo -e $red"                ◆━━━━━━━▣✦▣━━━━━━━━◆◆━━━━━━━▣✦▣━━━━━━━━◆"
echo -e -n $red"I"$cy"N"$ylo"P"$blue"U"$pink"T"$ylo">:"
read finput
case $finput in
     1) clear
        cd $HOME
	cd /data/data/com.termux/files/home/earn_money
	python EMONEY.py
     ;;
     2) clear
        cd /data/data/com.termux/files/home/earn_money
	python l.py
     ;;
      
     *) figlet -f big "      Invalid" | lolcat
        figlet -f big "       INPUT " | lolcat
        main
     ;;

esac
}
chei
report
main
