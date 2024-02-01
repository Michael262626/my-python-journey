package fireDrillTwo;

import java.util.Scanner;

public class TaskTen {

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int sum = 0;
            double average = 0.0;
            for (int count = 1; count <= 10; count++) {
                System.out.println("Enter score:");
                int score = scanner.nextInt();
                if (score > 0 && score < 100) {
                    sum += count;
                    average = sum/count;
                    System.out.printf("Sum: %d", sum);
                }
            }
        }
    }

