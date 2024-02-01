package fireDrillOne;

public class TaskFive {
    public static void main(String[] args) {
        for(int count  = 1; count <= 10; count++) {
            for (int index = 1; index <= 5; index++) {
                if (count % 4 == 0) {

                    System.out.printf(" %d", count);
                }
            }
        }
    }
}
