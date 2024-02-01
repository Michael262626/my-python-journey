import java.util.Random;
import java.util.Scanner;
public class Coin {

    enum TossCoin {
        HEADS,
        TAILS;
    }

    public static void main(String[] args) {
        int headsCount = 0;
        int tailsCount = 0;

        Scanner scanner = new Scanner(System.in);

        System.out.println("1. Toss coin");
        System.out.println("2. Exit");
        int choice = scanner.nextInt();

        do{
            System.out.println("1. Toss coin");
            System.out.println("2. Exit");
            choice = scanner.nextInt();
            if (choice == 1) {
                TossCoin result = flip();
                if (result == TossCoin.HEADS) {
                    headsCount++;
                } else {
                    tailsCount++;
                }

            }
            else{

                System.out.println("Heads: " + headsCount + "Tails: " + tailsCount);
            }
        }while(choice == 1);


    }

public static TossCoin flip(){
        Random random = new Random();
        int randomNumbers = random.nextInt(2);
        if(randomNumbers== 0){
            return TossCoin.HEADS;
        }
        else{
            return TossCoin.TAILS;
        }




    }

}