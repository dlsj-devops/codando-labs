class Person {
    //variavel de classe
    static int id = 15;

    //Variavel de instancia
    String name = "sem nome definido";

    public void setName(String sn) {
        this.name = sn;
    }
    
    public String getName() {
        return this.name;
    }
}

class VariavelMesmoNome {
    int a = 100;

    public void printValor() {
        int a = 200;

        //Mesmo nome -> usa o menor escopo
        System.out.println(a);
    }
}

class VariaveisTest {
    public static void main(String[] args) {
        Person p1 = new Person();

        // variavel de classe
        System.out.println(p1.id);

        System.out.println(Person.id);

        //variavel de instancia
        Person p2 = new Person();

        p2.setName("joao");

        System.out.println(p1.getName());

        System.out.println(p2.getName());

    }
}