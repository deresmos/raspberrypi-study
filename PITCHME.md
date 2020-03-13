## Day 1

---

### Raspberry Pi とは

- シングルボードコンピューター
- 簡単にいうと、とても小さなコンピューター
- 格安（5000円〜8000円）

---

### Raspberry Piで何ができる？

- 24時間稼働の格安サーバーとして利用化 |
- 人感センサーつけて、親フラ防止！ |

---

### 電気代

|        |         |                           |
|--------|---------|---------------------------|
| 3b+    | 3W      | 一ヶ月約58円              |
| 4b 4GB | 5W〜6W? | 一ヶ月約97円〜116円ぐらい |

---

### Raspberry Pi OSたち

- [OS いろいろ](https://www.raspberrypi.org/downloads/)
- 今回は、Raspbian Liteを利用

---

# デモ

---

### Raspbian LiteをSDカードにインストール
※if, ofは絶対に間違えないように！

```bash code-noblend code-wrap zoom-11
dd bs=4M if=2020-02-13-raspbian-buster-lite.img of=/dev/sdb conv=fsync
```

+++

### dd
ブロックデバイスを直接読み書きできるコマンド

+++

### conv=fsync
メタデータも含めるぞ、オプション

---

### sshd自動起動
```bash code-noblend
sudo touch boot/ssh
```

起動後
```bash code-noblend
ssh pi@raspberrypi.local
```

+++

### リンクローカルアドレス
DHCPサーバが存在しないネットワーク内で使われる、特別なIPアドレス
169.254.0.0/16

+++

avahiにより、ホスト名でアクセス可能

/etc/hostname

---

### Wifi接続

```bash code-noblend code-wrap
wpa_passphrase ssid password >> /etc/wpa_supplicant/wpa_supplicant.conf

ip a
ip link set wlan0 up

rfkill list
rfkill unblock 0
sudo reboot
```

Wi-Fi接続完了！

+++

### RF-kill
無線送信器を、アクティベート、非アクティブ化することができる。

```bash code-noblend
rfkill list
```

ソフトウェアが再アクティベートできる状態 (soft blocked) 

ソフトウェアが再アクティベートできない状態 (hard blocked) 

---

初期設定

@code[bash zoom-10 code-noblend code-wrap](src/setup_raspbian_sd.sh)

@snap[north span-100]
@[2-3, zoom-16](/boot, /をマウント)
@[5, zoom-16](デフォルト接続情報をコピー)
@[6, zoom-16](接続したいSSID設定を追記)
@[8, zoom-16](起動時にsshdを起動させる用)
@[9, zoom-16](boot/wpa_supplicant.confに置くことで、いい感じに設定してくれる)
@[11, zoom-16](必要に応じて、IP固定とかする)
@snapend

+++

### IP固定

/etc/dhcpcd.conf

```text code-noblend
interface wlan0
static ip_address=192.168.1.122/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

+++

### dhcpcd
DHCPのクライアント

+++

```bash code-noblend
sudo systemctl daemon-reload
sudo systemctl restart dhcpcd
sudo ip addr del 192.168.1.120/24 dev wlan0
```

@snap[north span-100]
@[1, zoom-16](設定変更を反映させる。今回の修正には実は関係ないので不要)
@[2, zoom-16](dhcpcdサービスを再起動)
@[3, zoom-16](不要なIPを削除)
@snapend


---

Webサーバーをさくっと立ててみる

```bash code-noblend
scp index.html 宛先:./index.html

ssh ラズパイ入る
python3 -m http.server 8008
```


---

## Python
FizzBuzzで学ぶ基本構文

---

@code[python zoom-10 code-noblend code-wrap](src/fizzbuzz.py)

@snap[north span-100]
@[1, zoom-16](randomパッケージの読み込み)
@[3, zoom-16](20〜40の間でランダムな整数を返す)
@[6-7,12, zoom-16](関数定義。printでコンソールに出力)
@[10, zoom-16](for文。rangeは、指定個数の連番配列を返してくれる)
@[11,13,15,17, zoom-16](if文。論理演算子は、and, or, notで表現)
@[11-18, zoom-16](fizzbuzz)
@snapend
