#!/bin/zsh
sudo su root

kubeadm reset -y
systemctl stop kubelet
systemctl stop docker
systemctl stop containerd

ip link delete cni0
ip link delete flannel.1

# deleting files related to kubernetes

rm -rf /var/lib/cni
rm -rf /var/lib/kubelet/* -y
rm -rf /var/lib/etcd/
rm -rf /run/flannel
rm -rf /etc/cni/
rm -rf /etc/kubernetes
rm -rf ~/.kube
rm -rf /var/run/calico/
rm -rf /var/lib/calico/
rm -rf /etc/cni/net.d/
rm -rf /var/lib/cni/

IS_UBUNTU=$(hostnamectl | grep Ubuntu)
if [ "$IS_UBUNTU" ]; then
  sudo apt-get purge kubeadm kubectl kubelet kubernetes-cni kube* -y
  sudo apt-get autoremove
else
  sudo yum remove kubeadm kubectl kubelet kubernetes-cni kube* -y
  sudo yum autoremove
fi

