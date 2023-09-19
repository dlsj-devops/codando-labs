class Pessoa {
    //variaveis de instancia
    String nome;
    String sobrenome;

    //construtor
    Pessoa(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    //método
    public String getNomeCompleto(){
        return nome + " " + sobrenome;
    }

    //metodo com mesmo nome do construtor
    String Pessoa() {
        return nome + " " + sobrenome;
    }
}