import java.util.Scanner;
public class test {
    public static void main(String[] args) {
        PassiveBot sigma = new PassiveBot();
        sigma.greeting();
        System.out.print("You: ");
        Scanner input = new Scanner(System.in);
        String rah = input.nextLine();

        System.out.println(sigma.response(rah));
        while(!rah.equals("bye")){
            System.out.print("You: ");
            rah = input.nextLine();
            System.out.println(sigma.response(rah));
        }

    }
}
