package Test1;

public class driver extends data {

    public driver(int age, String name) {
        super(age, name);
        //TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {

        data test = new data(10, "Name");

        System.out.println(test.getName());
        System.out.println(test.getAge());
    }
}