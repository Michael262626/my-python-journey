package fireDrillOne;

public class TaskSix {
    public static void main(String[] args) {
        for (int count = 1; count <= 10; count++) {
            int number =count;
                if (count % 4 == 0) {
                    for (int index = 1; index <= 5; index++) {
                       int number1 = count;

                    System.out.print(number+" ");
                    number*=number1;
                }
            }
        }
    }
}
