# Usando o vagrant

- Definir a box

Achar as box em app.vagrantup.com/boxes/search 

- Criar o Vagrantfile

- Executar a VM com o vagrant

## Passos

### Box escolhida:

https://app.vagrantup.com/ubuntu/boxes/jammy64

### Vagrantfile

- Criando o vagrantfile

```shell
vagrant init ubuntu/jammy64
```

- Habiltnado a rede

```shell
  config.vm.network "public_network"
```

- Configurando o provider

```shell
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true
    #   # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
```

### Executando

```shell
vagrant up
```

### Mounting shared folders...

```text
default: /vagrant => "folder atual (.)"
```