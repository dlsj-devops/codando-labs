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
    String a = "escopo maior";

    public void printValor() {
        String a = "escopo menor";

        //Mesmo nome -> usa o menor escopo
        System.out.println(a);
    }
}

class VariaveisTest {
    static int i = 3;

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

        VariavelMesmoNome vmn = new VariavelMesmoNome();
        vmn.printValor();

        for (new VariaveisTest().i = 10; new VariaveisTest().i < 100; new VariaveisTest().i++) {
            System.out.println(i);
        }
    }
}