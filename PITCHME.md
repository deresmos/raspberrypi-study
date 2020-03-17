## Day 2

---

### Day1のおさらい

- OSインストール(dd)
- WiFi接続(wpa_supplicant, wpa_passphrase, rfkill)
- SSHD起動(systemctl or /boot/ssh)

---

### キーボード、ディスプレイ不要
- SSHD起動(systemctl or /boot/ssh) |
  - -> /boot/ssh 空ファイルおく |
- WiFi接続(wpa_supplicant, wpa_passphrase, rfkill) |
  - -> /boot/wpa_supplicant.confを置く |

---

### 人感センサー

- 赤外線により人間の所在を検知する

---

### GPIO

- General-purpose input/output
- ユーザーによって制御可能な汎用出力インターフェース

---

### 人感センサーつなげてみる

---

### Pythonセットアップ

- [Berry Conda](https://github.com/jjhelmus/berryconda)


```bash
wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
bash Berryconda3-2.0.0-Linux-armv7l.sh
```

---

### GPIO制御するパッケージインストール

```bash
pip install RPi.GPIO
```

---

### 人感センサー使ってみる
