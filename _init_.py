impor sys
impor periksa
impor logging

dari teks impor dedent

dari .utils import _get_variable
dari .exceptions import HelpfulError

 Yikes kelas :
    def  find_module ( mandiri , nama lengkap , path = Tidak Ada ):
        jika nama lengkap ==  ' permintaan ' :
            kembali  diri
        return  Tidak ada

    def  _get_import_chain ( mandiri , * , hingga = Tidak Ada ):
        stack = inspect.stack () [ 2 :]
        coba :
            untuk frameinfo di stack:
                coba :
                    jika  tidak frameinfo.code_context:
                        terus

                    data = dedent ( ' ' .join (frameinfo.code_context))
                    if data.strip () == hingga:
                        meningkatkan  StopIteration

                    hasilkan frameinfo.filename, frameinfo.lineno, data.strip ()
                    data del
                akhirnya :
                    del frameinfo
        akhirnya :
            del tumpukan

    def  _format_import_chain ( self , chain , * , message = None ):
        lines = []
        untuk baris di chain:
            lines.append ( " Dalam % s , baris % s : \ n     % s "  % baris)

        jika pesan:
            lines.append (pesan)

        return  ' \ n ' .join (baris)

    def  load_module ( mandiri , nama ):
        if _get_variable ( ' allow_requests ' ):
            sys.meta_path.pop ( 0 )
            return  __import__ ( ' permintaan ' )

        import_chain =  tuple ( self ._get_import_chain ( hingga = ' dari .bot import MusicBot ' ))
        import_tb =  mandiri ._format_import_chain (import_chain)

        meningkatkan HelpfulError (
            " Anda mencoba mengimpor permintaan, atau mengimpor modul yang menggunakan permintaan.   "
            " Permintaan (atau modul apa pun yang menggunakan permintaan) tidak boleh digunakan dalam kode ini.   "
            " Lihat % s mengapa permintaan tidak cocok untuk kode ini. "
            %  " [https://discordpy.readthedocs.io/en/latest/faq.html#what-does-blocking-mean] " ,

            " Jangan gunakan permintaan, sebaliknya gunakan aiohttp. Api sangat mirip dengan permintaan "
            " Saat menggunakan objek sesi. [http://aiohttp.readthedocs.io/en/stable/] If "
            " modul yang kamu coba gunakan tergantung pada permintaan, lihat apakah kamu dapat menemukan yang serupa "
            " Modul yang kompatibel dengan asyncio. Jika Anda tidak dapat menemukannya, pelajari cara menghindari pemblokiran "
            " di coroutine. Jika Anda baru dalam pemrograman, pertimbangkan untuk belajar lebih banyak tentang caranya "
            " kode asinkron dan coroutine berfungsi. Memblokir panggilan (terutama permintaan HTTP) dapat mengambil "
            " lama sekali, selama itu bot tidak bisa melakukan apa pun kecuali menunggu.   "
            " Jika Anda yakin tahu apa yang Anda lakukan, cukup tambahkan` allow_requests = True` di atas Anda "
            " Pernyataan impor, yang menjadi` permintaan impor` atau modul apa pun yang bergantung pada permintaan. " ,

            footnote = " Impor traceback (panggilan terakhir terakhir): \ n "  + import_tb
        )

sys.meta_path.insert ( 0 , Yikes ())

dari .bot impor MusicBot
dari .constructs import BetterLogRecord

__all__  = [ ' MusicBot ' ]

logging.setLogRecordFactory (BetterLogRecord)

_func_prototype =  " def {logger_func_name} (mandiri, pesan, * args, ** kwargs): \ n " \
                  "     if self.isEnabledFor ( {levelname} ): \ n " \
                  "         self._log ( {levelname} , pesan, args, ** kwargs) "

def  _add_logger_level ( levelname , level , * , func_name  =  Tidak Ada ):
    "" "
    : ketik levelname: str
        Nama referensi level, misalnya DEBUG, PERINGATAN, dll
    : tipe level: int
        Tingkat pencatatan angka
    : ketik func_name: str
        Nama fungsi logger untuk masuk ke level, misalnya "info" untuk log.info (...)
    "" "

    func_name = func_name atau levelname.lower ()

    setattr (logging, levelname, level)
    logging.addLevelName (level, levelname)

    exec (_func_prototype.format ( logger_func_name = func_name, levelname = levelname), logging. __dict__ , locals ())
    setattr (logging.Logger, func_name, eval (func_name))


_add_logger_level ( ' EVERYTHING ' , 1 )
_add_logger_level ( ' NOISY ' , 4 , func_name = ' noise ' )
_add_logger_level ( ' FFMPEG ' , 5 )
_add_logger_level ( ' VOICEDEBUG ' , 6 )

log = logging.getLogger ( __name__ )
log.setLevel (logging. EVERYTHING )

fhandler = logging.FileHandler ( nama file = ' log / musicbot.log ' , enkode = ' utf-8 ' , mode = ' a ' )
fhandler.setFormatter (logging.Formatter (
    " [ { relatifCreated: .16f } ] {asctime} - {levelname} - {name} | "
    " Dalam {filename} :: {threadName} ( {thread} ), baris {lineno} di {funcName} : {message} " ,
    style = ' { '
))
log.addHandler (fhandler)

del _func_prototype
del _add_logger_level
del fhandler
