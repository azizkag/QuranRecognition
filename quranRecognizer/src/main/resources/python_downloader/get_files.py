import urllib
import os



author = "AbdulSamad_64kbps_QuranExplorer.Com"
surah = "001"
#file_name = "001"
readers = ["Abdullaah_3awwaad_Al-Juhaynee_128kbps","Abdullah_Basfar_64kbps","Abdullah_Matroud_128kbps","Abdurrahmaan_As-Sudais_64kbps","Abu_Bakr_Ash-Shaatree_64kbps","Ahmed_Neana_128kbps","Ahmed_ibn_Ali_al-Ajamy_64kbps_QuranExplorer.Com","Akram_AlAlaqimy_128kbps","Alafasy_64kbps","Ali_Hajjaj_AlSuesy_128kbps","Ali_Jaber_64kbps","Fares_Abbad_64kbps","Ghamadi_40kbps","Hani_Rifai_64kbps","Hudhaify_64kbps","Khaalid_Abdullaah_al-Qahtaanee_192kbps","Maher_AlMuaiqly_64kbps","Mohammad_al_Tablaway_64kbps", "Muhammad_AbdulKareem_128kbps", "Muhammad_Ayyoub_64kbps", "Muhammad_Jibreel_64kbps", "Muhsin_Al_Qasim_192kbps", "Mustafa_Ismail_48kbps","Nasser_Alqatami_128kbps", "Parhizgar_48kbps", "Sahl_Yassin_128kbps", "Salaah_AbdulRahman_Bukhatir_128kbps", "Salah_Al_Budair_128kbps", "Saood_ash-Shuraym_128kbps","Yaser_Salamah_128kbps", "Yasser_Ad-Dussary_128kbps", "ahmed_ibn_ali_al_ajamy_128kbps", "aziz_alili_128kbps", "khalefa_al_tunaiji_64kbps",
"mahmoud_ali_al_banna_32kbps"]
ayat = ["001","002","003","004","005","006","007"]

for author in readers:
    #create the path to the files
    directory = author+"/"+surah
    if not os.path.exists(directory):
            os.makedirs(directory)

    for file_name in ayat:
        testfile = urllib.URLopener()
        testfile.retrieve("http://www.everyayah.com/data/AbdulSamad_64kbps_QuranExplorer.Com/"+surah+file_name+".mp3", author+"/"+surah+"/"+file_name+".mp3")

        os.system("sox "+author+"/"+surah+"/"+file_name+".mp3 -c 1 -r 8000 "+author+"/"+surah+"/"+file_name+".wav")

        #insert the name of the utternace path in fileids_file

        with open("fatiha_train.fileids", "a") as myfile:
                myfile.write(author+"/"+surah+"/"+file_name+"\n")


