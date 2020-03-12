#! /bin/bash

set -eu

if [[ $# -ne 2 ]]; then
  echo "引数しっかり指定ね！"
  echo "$ ${0} {device_file} {ssid}"
  exit 1
fi

raise(){
  exit 1
}

readonly device_file=$1
readonly ssid=$2
read -sp "Passhrase: " passphrase
echo

function finalize() {
  echo "Unmounting boot and root"
  sudo umount boot root
}

cd workspace

echo "Mounting boot and root"
sudo mount ${device_file}1 boot
sudo mount ${device_file}2 root


set +x
(
  echo "- Setup wpa_spplicant.conf"
  sudo cp root/etc/wpa_supplicant/wpa_supplicant.conf ./ || raise
  sudo bash -c "wpa_passphrase '${ssid}' '${passphrase}' >> wpa_supplicant.conf" || raise
  sudo cp wpa_supplicant.conf boot/ || raise

  echo "- Setup sshd"
  sudo touch boot/ssh || raise

  finalize
  echo "Success!(^o^)"
) || (
  echo "error(-o-)"

  finalize
  exit 1
)
