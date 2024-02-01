package fireDrillOne;

public class TaskSeven {

    public static void main(String[] args) {
        for (int count = 1; count <= 10; count++) {
            int number = count;
            int sum = 0;
            if (count % 4 == 0) {
                for (int index = 1; index <= 5; index++) {
                    int number1 = count;

                    sum += number;
                    number *= number1;
                }

                System.out.printf(" %d", sum);
            }


            }
        }
    }

