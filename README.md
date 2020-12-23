_For english scroll down..._

[![Discord](https://img.shields.io/discord/545564775497859072?label=Discord&logo=discord&style=plastic)](https://discord.gg/JbFdHMK) 
![Repo Boutu](https://img.shields.io/github/repo-size/cinicin/cncn_m2?style=plastic "Repository boyutu") ![Toplam Indırme](https://img.shields.io/github/downloads/cinicin/cncn_m2/total?style=plastic)



# cncn_m2 / TR

Altyapınında altyapısı...

Sadece kütüphane güncellemeleri ve başarılı şekilde derleyebilmek için gerekli düzenlemeler yapılmıştır.

_TEST EDİLDİĞİ PLATFORMLAR_:

* FreeBSD 12.1 x86
* FreeBSD 12.2 x86
* Windows 10 x64

## KURULUM

[![Youtube](https://img.shields.io/youtube/views/xqSfA8Mhikc?style=social)](https://youtu.be/xqSfA8Mhikc)

Sayaca tıklayarak videoya gidebilirsiniz. Video ilk paylaşılan hali için ancak pek bir fark yok varsayılan dil türkçe olduğundan aynı şekilde kurabilirsiniz.

<details>
  <summary>Gerekenler</summary>

Windows Tarafında :

* [Visual Studio 2019](https://visualstudio.microsoft.com/)
* İş görebilecek bir editör.
* SFTP Client [WinSCP](https://winscp.net/) , [FileZilla](https://filezilla-project.org/)
* Sanallaştırma programı, FreeBSD makinanız yoksa.

FreeBSD Tarafında :

* Gmake-4.3_2
* Python 2.7.18
* Devil 1.7.8
* Llvm-devel 12.0
* Mysql 8.0.22 (client ve server)
* p7zip 16.02_2
* Makedepend 1.0.6

 </details>

 <details>
   <summary>Kurulum</summary>

1. [İndirin](https://github.com/cinicin/cncn_m2.git) ve ya git ile clonlayın tüm projeyi. Hem bsd hem win tarafına.
2. [Crypto++](https://github.com/weidai11/cryptopp.git) 'u indirin ve ya klonlayın
3. cryptopp klasörünü `../cncn_m2/srcs/harici/cryptopp_8_30/cryptopp` lokasyonuna atın. **üzerine yazmayın. !!!**
4. [boost 1.75 indirin.](https://www.boost.org/users/download/)
5. boost klasörünü `../cncn_m2/srcs/harici/boost_1_75_0/boost` lokasyonuna atın. ( sadece boost klasörünü diğerleri gerekli değil. )
6. `sh cncn.sh` yazarak scripti çalıştırın.
7. Önce libleri sonra game ve db yi derleyin. `derle lib db game`
8. Scripti tekrar başlatın.
9. Klasör hiyerarşisini oluşturmak için `kurulum` yazın.
10. Client projesini derleyin. Release olarak.
11. `bin` klasöründen client exe'sini `cncn_m2/client` içine atın.
12. `../cncn_m2/client/pack/root/serverinfo.py` makinenizin ip adresini yazın.
13. [Pack](https://www.dosyaupload.com/ozh1) arşivini client klasörüne çıkarın.
14. Artık sisteminiz hazır.

 </details>

## cncn.sh


![Komut Ekranı](/info/img/cncn_sh_command_screen.jpg)


_Sıralama Soldan-Sağa doğrudur._

> Yani, girdiğiniz stringler soldan sağa doğru okunur.
`baslat 1 2 auth db` şeklinde girerseniz önce 1 sonra 2 sonra auth en son db yi başlatır. Db başlamadığından dolayıda 1 2 auth başlayamayacaktır. Önce db yi yazmayı sizin düşünmeniz gerekiyor.

_Tek seferde maksimum 9 string girilebilir._

> Dokuzdan fazla girerseniz işlem gerçekleşmez.

_Tek sefer birden fazla eylem gerçekleştirilebilir._

> `derle baslat kapat db auth 1 ` gibi ya da `kapat baslat all` gibi tek seferde birden fazla eylem yaptırılabilir sıralama soldan sağa doğru her zaman.

:mega: _**AYNI STRINGLERI BIRDEN FAZLA KULLANMA !!!**_

> `derle derle d all` gibi bir komut girişi 3 kere derleme yapar. Ya da `baslat db db auth ` gibi bir komut db kanalını iki kez başlatmaya çalışır. başlatma ve kapatma fonksiyonlarında kontroller var tekrar başlatmayacaktır ancak derleme işlemlerinde kontrol yok.



#### Eylemler:


| String | Yerine Kullanılabilecek Stringler |
| -----  | --------------------------------- |
| `baslat` | `b` - `start` |
| `kapat` | `k` - `close` - `kill` |
| `derle` | `d` - `compile` |
| `temizle` | `clear` |
| `temiz` | `clean` |
| `kurulum` | `setup` |

> `kurulum` komutu sürekli kullanacağınız bir komut değil ilk kullanımda çalışırmalısınız server klasör sistemini oluşturur. Sembolik linkleri ve klasörleri.




#### Değerler:

| String | Yerine K. | Açıklaması |
| ------ | ---------- |- |
| `1` | - | 1.Kanalı ifade eder. |
| `2` |  - | 2.Kanalı ifade eder. |
| `3` |  - | 3.Kanalı ifade eder. |
| `4` |  - | 4.Kanalı ifade eder. |
| `99` | - | ortak kanalını ifade eder. |
| `test` | - | test kanalını ifade eder. |
| `auth` |  - | Auth Kanalını ifade eder. |
| `db` |  - | Duruma göre db kanalını ya da db kaynak kodlarını ifade eder. |
| `game` |  - | game kaynak kodlarını ifade eder. |
| `ymir` | - | Ymir kütüphanelerini ifade eder. |
| `lib` |  - | ymir kütüphanelerine ek olarak cryptopp'uda ifade eder. |
| `libgame` | - | libgame kütüphanesini ifade eder. |
| `liblua` | - | liblua kütüphanesini ifade eder. |
| `libpoly` | - | libpoly kütüphanesini ifade eder. |
| `libsql` | - | libsql kütüphanesini ifade eder. |
| `libthecore` | - | libthecore kütüphanesini ifade eder. |
| `qc` | - | qc kaynak kodlarını ifade eder. |



 </details>






# cncn_m2 / EN


Most basic clean as f**k m2 client-server system.
Only the necessary code correction have been made for library upgrades and successful compilation.
You can check the history tab for more detailed information.





_TESTED WITH_:

* FreeBSD 12.1 x86
* FreeBSD 12.2 x86
* Windows 10 x64


## INSTALL

[![Youtube](https://img.shields.io/youtube/views/xqSfA8Mhikc?style=social)](https://youtu.be/xqSfA8Mhikc)





<details>
  <summary>Requirements</summary>

On Windows:

* [Visual Studio 2019](https://visualstudio.microsoft.com/)
* A good text editor.
* SFTP Client [WinSCP](https://winscp.net/) , [FileZilla](https://filezilla-project.org/)
* A virtualization product if you don't have a FreeBSD machine.

On FreeBSD:

* Gmake-4.3_2
* Python 2.7.18
* Devil 1.7.8
* Llvm-devel 12.0
* Mysql 8.0.22 (client and server)
* p7zip 16.02_2
* Makedepend 1.0.6

> You can watch the video above for prepating 

 </details>


 <details>
   <summary>Install</summary>

1. [Download](https://github.com/cinicin/cncn_m2.git) or clone the repository to both FreeBSD and Windows side

2. Download or clone [Crypto++](https://github.com/weidai11/cryptopp.git)

3. Move cryptopp folder to `../cncn_m2/srcs/harici/cryptopp_8_30/cryptopp` **don't overwrite. !!!**

4. [Download boost 1.75](https://www.boost.org/users/download/)

5. Move boost folder to `../cncn_m2/srcs/harici/boost_1_75_0/boost`  ( other folders and files not needed )

6. Start cncn.sh `sh cncn.sh`

7. Compile all source files that needs to be compiled by writing this command `compile lib db game`

8. Restart the script.

9. Type this command `setup`
10. Compile client vs project as release
11. move or copy  exe file that created in `bin` to `../cncn_m2/client`
12. `../cncn_m2/client/pack/root/serverinfo.py`. Change ip.
13. [Pack](https://www.dosyaupload.com/ozh1) extract to client folder.
14. Check How to change language part.


 </details>





:key: Herhangi bir şifre ile karşılaşırsanız `cinicin` dir.



![version](https://img.shields.io/github/v/release/cinicin/cncn_m2?style=plastic)

History :

- [x] Script cncn.sh
- [x] Preparing envoirment [FreeBSD 12.1](https://www.freebsd.org/)
- [x] Getting the codes from kraizy.tgz
- [x] Rewrite all makefiles.
- [x] Temporary locale folder.
- [x] Successfuly server-client connection. 
- [x] Upgrade -> Mysql 8
- [x] Upgrade -> [cryptopp 8.20](https://github.com/weidai11/cryptopp)
- [x] Upgrade -> [boost 1.75.0](https://www.boost.org/)
- [x] Upgrade -> DevIL 1.8
- [x] Upgrade -> [lzo 2.10](http://www.oberhumer.com/opensource/lzo/)
- [x] Upgrade -> Granny 2.11
- [x] Upgrade -> Python 2.7
- [x] Upgrade -> libjpeg-9a
- [x] Temporary client folder.
- [x] Eng server side locale.
- [x] Eng client side locale.
- [x] Eng protos
- [x] Modify cncn.sh for eng support.
- [x] Modify cncn.sh. Add channel cleaner function.
- [x] Qc src correction.
- [x] Add dump proto src.
- [x] Compile dump proto and test.
- [x] Upgrade -> [cryptopp 8.30](https://github.com/weidai11/cryptopp)





How to change language ?

> Only english and turkish language added because I don't know any other language 
>> I put some cheat sheet in files for if u need to add another language.

 1. Open cncn.sh with a good editor, change the language part on top side to `en`. Default `tr`.
 2. Open navicat go `commmon->locale` and change `turkey` to `uk` or any other european locale if you change another locale rather than `uk` go `../cncn_m2/datas/locale/` and rename `uk` to your locale name. `english` not work properly I don't know and too lazy to figure it out.
 3. Start cncn.sh and enter this code `setup`
 4. Edit `../cncn_m2/client/locale.cfg` to `10002 1252 en`

_*All makefiles configured for tr folder structure. Open evey makefile change `ayarlar` to `settings` if you dont do this, you can't compile the srcs*_

> Or in evey compilation process, edit cncn.sh  en->tr and run setup before compile and change en again and setup again. Your choice... I know it's messy :)





## cncn.sh


![Komut Ekranı](/info/img/cncn_sh_command_screen.jpg)


_Reads left to right direction._

> So the strings you enter are read from left to right.
If you enter `start 1 2 auth db`, first 1 then 2 then auth starts db will start last. 1 2 auth will not be able to start because the db is not started You have to think about typing db first yourself.

_Maximum 9 strings can be entered at one time._

> If you enter more than nine, the reading will not take place.

_Multiple actions can be performed at one time._

> More than one action can be performed at once, such as `compile start close db auth 1` or `close start all` reads from left to right all the time.

:mega: _**YOU SHOULD NOT USE MORE THAN ONE THE SAME STRINGS !!! !!!**_

> A command input such as `compile compile d all` compiles 3 times. Or a command like `start db db auth` tries to start the db channel twice. There are checks in the startup and shutdown functions, it will not restart, but there is no control in compilation.



#### Functions:

| String | Can be used instead |
| -----  | --------------------------------- |
| `baslat` | `b` - `start` |
| `kapat` | `k` - `close` - `kill` |
| `derle` | `d` - `compile` |
| `temizle` | `clear` |
| `temiz` | `clean` |
| `kurulum` | `setup` |

> `setup` You should run this command for the first time, not a command that you will use constantly, it creates the server folder system. Symbolic links and folders.

> `clear` will clear channel folders `clean` for srcs remove all object files and binaries.


#### Values:

| String | Can be used instead | Description |
| ------ | ---------- |- |
| `1` | - | For Channel 1 |
| `2` |  - | For Channel 2 |
| `3` |  - | For Channel 3 |
| `4` |  - | For Channel 4 |
| `99` | - | For Channel 99 |
| `test` | - | For Channel test |
| `auth` |  - | For Channel auth |
| `db` |  - | For db channel or db source codes depending on the situation. |
| `game` |  - | For game source codes. |
| `ymir` | - | For Ymir libs. |
| `lib` |  - | Also cryptopp in addition to ymir libraries. |
| `libgame` | - | For libgame library. |
| `liblua` | - | For liblua library. |
| `libpoly` | - | For libpoly library. |
| `libsql` | - | For libsql library. |
| `libthecore` | - | For libthecore library. |
| `qc` | - |  For qc source codes. |



Examples:

 <details>
   <summary>Starting multiple channels</summary>


`start db auth test`

`db auth test start`

`db start auth test`


both are legit and same meaning starts first db later auth later test 

 </details>


You know what there is no need more examples script foolproof... You can type freely just don't type same string twice.




























