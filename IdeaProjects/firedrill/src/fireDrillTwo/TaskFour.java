package fireDrillTwo;

import java.util.Scanner;

public class TaskFour {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;

        for (int count = 1; count <= 10; count++) {
            System.out.println("Enter score");
            int scores = scanner.nextInt();
            if(count%2==0) {
                sum += scores;

            }

        }
        System.out.printf("\nsum: %d", sum);



    }
}
