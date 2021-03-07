#!/bin/bash

PLANSZA=("0" "0" "0" "0" "0" "0" "0" "0" "0")
GRACZ="2"
WYGRANA="0"
ERROR = ""

function wyswietl {
    clear
    echo "Plansza"
    echo "${PLANSZA[0]} | ${PLANSZA[1]} | ${PLANSZA[2]}"
    echo "${PLANSZA[3]} | ${PLANSZA[4]} | ${PLANSZA[5]}"
    echo "${PLANSZA[6]} | ${PLANSZA[7]} | ${PLANSZA[8]}"

    if [ "${ERROR}" != "" ]
    then
        echo -e "\n${ERROR}"
        ERROR=""
    fi
}

function porownajPola {
    POLE1="$1"
    POLE2="$2"
    POLE3="$3"
    if [ "${PLANSZA[${POLE1}]}" == "${PLANSZA[${POLE2}]}" ] && [ "${PLANSZA[${POLE3}]}" == "${PLANSZA[${POLE2}]}" ];
    then
        if [ "${PLANSZA[${POLE1}]}" == "0" ];
        then
            return 1;
        else
            return 0;
        fi
    else
        return 1;
    fi
}

function zaznaczPole {
    POLE="$1"
    if [ "${PLANSZA[${POLE}]}" == "0" ];
    then 
        if [ $GRACZ -eq 1 ];
        then
            PLANSZA[${POLE}]="X"
        else
            PLANSZA[${POLE}]="O"
        fi 
    else
        ERROR="To pole jest już zajęte!!!" 
    fi
}

function sprawdzWygrana {

    if porownajPola "0" "1" "2" ||
    porownajPola "3" "4" "5" ||
    porownajPola "6" "7" "8" ||
    porownajPola "0" "3" "6" ||
    porownajPola "1" "4" "7" ||
    porownajPola "2" "5" "8" ||
    porownajPola "0" "4" "8" ||
    porownajPola "2" "4" "6"
    then
        WYGRANA=$((GRACZ))
    fi

    POLA_ZAPELNIONE=0
    for item in ${PLANSZA[*]}
    do
        if [ "${item}" == "0" ]
        then
            POLA_ZAPELNIONE=1
            break
        fi
    done
    
    if [ ${POLA_ZAPELNIONE} -eq 0 ]
    then
        WYGRANA=3
    fi
}

function zmienGracza {
    if [ $GRACZ -eq 1 ];
    then
        GRACZ="2"
    else
        GRACZ="1"
    fi 
}

while [ $WYGRANA -eq "0" ]
do
  wyswietl
  zmienGracza
  echo -e "\nKtóre pole zaznaczyć dla zawodnika ${GRACZ}"
  read POLE

  echo ${POLE}
  if [ "${POLE}" == "" ] || [ "${POLE}" -gt 8 ];
  then
	ERROR="Złe pole"
	zmienGracza
	continue
  else
    zaznaczPole ${POLE}
  fi
  sprawdzWygrana
done

reset 
if [ ${WYGRANA} -eq 3 ]
then
    echo "Remis!!!"
else
    echo "Wygrał gracz nr $GRACZ"
fi
