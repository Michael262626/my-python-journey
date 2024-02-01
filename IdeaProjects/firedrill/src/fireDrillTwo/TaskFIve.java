package fireDrillTwo;

import java.util.Scanner;


    public class TaskFIve {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            int sum = 0;
            int evenNumbers = 0;

            for (int count = 1; count <= 10; count++) {
                System.out.println("Enter score");
                int scores = scanner.nextInt();

                if(scores%2==0){
                    sum+=count;
                    evenNumbers = sum;
                }
            }
            System.out.printf("Even numbers: %d", evenNumbers);
        }
    }

