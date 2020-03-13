cd workspace
sudo mount /dev/sdb1 boot
sudo mount /dev/sdb2 root

sudo cp root/etc/wpa_supplicant/wpa_supplicant.conf ./
sudo bash -c 'wpa_passphrase ssid password >> wpa_supplicant.conf'

sudo touch boot/ssh
sudo cp wpa_supplicant.conf boot/

sudo vim root/etc/dhcpcd.conf
