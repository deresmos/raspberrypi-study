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

- 3b+ (3W)    一ヶ月約58円
- 4b 4GB (6W) 一ヶ月約116円だったはず

---

### Raspberry Pi OSたち

- [OS いろいろ](https://www.raspberrypi.org/downloads/)
- 今回は、Raspbian Liteを利用

---

# デモ

---

### Raspbian LiteをSDカードにインストール
※if, ofは絶対に間違えないように！

```bash
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
```bash
sudo touch boot/ssh
```

起動後
```bash
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

```bash
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

```bash
rfkill list
```

ソフトウェアが再アクティベートできる状態 (soft blocked) 

ソフトウェアが再アクティベートできない状態 (hard blocked) 

---

```bash
cd workspace
sudo mount /dev/sdb1 boot
sudo mount /dev/sdb2 root

sudo cp root/etc/wpa_supplicant/wpa_supplicant.conf ./
sudo bash -c 'wpa_passphrase ssid password >> wpa_supplicant.conf'

sudo touch boot/ssh
sudo cp wpa_supplicant.conf boot/

sudo vim root/etc/dhcpcd.conf
```

+++

### IP固定

- /etc/dhcpcd.conf

```text:
interface wlan0
static ip_address=192.168.1.122/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

+++

### dhcpcd
DHCPのクライアント

---

## Python
FizzBuzzで学ぶ基本構文

---

```python
import random

length = random.randint(20, 40)


def print_fizzbuzz():
    print("Fizz Buzz!")


for i in range(length):
    if (i % 3 == 0) and (i % 5 == 0):  # i % 15 == 0
        print_fizzbuzz()
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)
```
