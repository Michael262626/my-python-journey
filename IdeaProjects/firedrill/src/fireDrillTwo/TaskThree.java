package fireDrillTwo;

import java.util.Scanner;

public class TaskThree {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double average = 0;
        int sum = 0;
        for (int count = 1; count <= 10; count++) {
            System.out.println("Enter score");
            int scores = scanner.nextInt();
            sum += count;
            average = sum / count;
        }
        System.out.printf("\nsum: %d", sum);
        System.out.printf("\nAverage: %.2f", average);
    }
}
