# Panggilan Musik 1 - Bot Telegram untuk streaming audio dalam panggilan grup
# Hak Cipta (C) 2021 Roj Serbest

# Program ini adalah perangkat lunak gratis: Anda dapat mendistribusikannya kembali dan/atau memodifikasi
# di bawah ketentuan Lisensi Publik Umum GNU Affero sebagai
# diterbitkan oleh Free Software Foundation, baik versi 3 dari
# Lisensi, atau (sesuai pilihan Anda) versi yang lebih baru.

# Program ini disebarluaskan semoga bermanfaat,
# tapi TANPA JAMINAN APAPUN; bahkan tanpa jaminan tersirat dari
# DAGANG atau KESESUAIAN UNTUK TUJUAN TERTENTU. Lihat
# Lisensi Publik Umum GNU Affero untuk lebih jelasnya.
#
# Anda seharusnya telah menerima salinan dari GNU Affero General Public License
# bersama dengan program ini. Jika tidak, lihat <https://www.gnu.org/licenses/>.

# Dimodifikasi oleh Sadew Jayasekara

dari  jalur impor os  

dari  youtube_dl  impor  YoutubeDL

dari  Natsuki Music . konfigurasi  impor  DURATION_LIMIT
dari  Natsuki Music . pembantu . kesalahan  mengimpor  DurationLimitError

ydl_opts  = {
    "format" : "bestaudio[ext=m4a]" ,
    "geo-bypass" : Benar ,
    "nocheckcertificate" : Benar ,
    "outtmpl" : "unduhan/%(id)s.%(ext)s" ,
}

ydl  =  YoutubeDL ( ydl_opts )


def  unduh ( url : str ) ->  str :
    info  =  ydl . ekstrak_info ( url , Salah )
    durasi  =  putaran ( info [ "durasi" ] /  60 )

    jika  durasi  >  DURATION_LIMIT :
        meningkatkan  DurationLimitError (
            f"❌ Video yang berdurasi lebih dari { DURATION_LIMIT } menit tidak diizinkan, video yang disediakan adalah { durasi } menit"
        )
    coba :
        ydl . unduh ([ url ])
    kecuali :
        meningkatkan  DurationLimitError (
            f"❌ Video yang berdurasi lebih dari { DURATION_LIMIT } menit tidak diizinkan, video yang disediakan adalah { durasi } menit"
        )
     jalur kembali . join ( "downloads" , f" { info [ 'id' ] } . { info [ 'ext' ] } " )
