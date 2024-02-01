package fireDrillTwo;

import java.util.Scanner;

public class TaskSeven {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;
        int evenNumbers = 0;
        double average = 0.0;

        for (int count = 1; count <= 10; count++) {
            System.out.println("Enter score");
            int scores = scanner.nextInt();
            sum+=count;
            if(sum%2==0){
                evenNumbers = sum;
                average = evenNumbers/count;
            }
        }
        System.out.printf("Even numbers: %d", evenNumbers);
        System.out.printf("Even numbers: %.2f", average);
    }
}

