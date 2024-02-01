import java.util.Random;
import java.util.Scanner;
public class Main {
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {

        System.out.println("Enter a number in the range 1-1000!");
        int number = scanner.nextInt();
        guessNumber(number);
    }
    public static void guessNumber (int number){
        Random random = new Random();
        int secretNumber = random.nextInt(1000)+1;

        int count;
        for(count = 0; count <= 10; count++){
            if(number < secretNumber){
                System.out.println("Too low!\nTry again!");
                number  = scanner.nextInt();
            }else if(number>secretNumber){
                System.out.println("Too high!\nTry again!");
                number = scanner.nextInt();
            }else{
                System.out.println("Congratulations!!! you have guessed the correct number");
                break;
            }
                if(count>10){
                System.out.println("You have reached your guess limit :(");
                break;
            }
        }

    }


}