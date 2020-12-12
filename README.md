# cncn_m2

---

v 1.0.0

---

:key: Herhangi bir şifre ile karşılaşırsanız `cinicin` dir.

Currently only Turkish...


## Durum:

- [x] Script `cncn.sh`
- [x] [FreeBSD 12.1](https://www.freebsd.org/) çalışma ortamı hazırlanması.
- [x] Makefile düzeltilmesi.
- [x] Sızdırılan kodların derlenmesi.
- [x] Toplama locale,data,veritabanı dosyaları (Temp).
- [x] Başarılı client-server bağlantısı.
- [x] Mysql 8 yükseltme.
- [x] [cryptopp 8.20](https://github.com/weidai11/cryptopp) yükseltme.
- [x] [boost 1.75.0](https://www.boost.org/) yükseltme.
- [x] devIL 1.8 yükseltme.
- [x] [lzo 2.10](http://www.oberhumer.com/opensource/lzo/) yükseltme.
- [x] granny 2.11 yükseltme.
- [x] Python 2.7 yükseltme.
- [x] libjpeg-9a yükseltme. (thanks to megaladon :)
- [x] Client klasörünün hazırlanması. (Temp)
- [ ] Client klasörünün elden geçirilmesi.
- [ ] Tüm veritabanının elden geçirilmesi.
- [ ] Quest sisteminin gözden geçirilmesi.
- [ ] Proto tablolarının elden geçirilmesi.
- [ ] Dump_proto derlemesi.


Temp client folder:

	[client.7z](https://www.dosyaupload.com/g8iw)


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
| `baslat` | `b` - `start` - `Baslat` - `ac` - `Ac` - `Start` |
| `kapat` | `k` - `close` - `kill` - `Close` - `Kapat` |
| `derle` | `d` - `compile` - `Derle` - `gmake` - `make` |
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
| `all` | `hepsi` | duruma göre tüm kanalları ya da tüm kaynak kodlarını ifade eder. |
| `ymir` | - | Ymir kütüphanelerini ifade eder. |
| `lib` |  - | ymir kütüphanelerine ek olarak cryptopp'uda ifade eder. |
| `libgame` | - | libgame kütüphanesini ifade eder. |
| `liblua` | - | liblua kütüphanesini ifade eder. |
| `libpoly` | - | libpoly kütüphanesini ifade eder. |
| `libsql` | - | libsql kütüphanesini ifade eder. |
| `libthecore` | - | libthecore kütüphanesini ifade eder. |
| `qc` | - | qc kaynak kodlarını ifade eder. |
