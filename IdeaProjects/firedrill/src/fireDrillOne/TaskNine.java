package fireDrillOne;

public class TaskNine {
    public static void main(String[] args) {
        int sum = 0;
        for (int count = 1; count <= 10; count++) {
            int number = count;
            if (count % 4 == 0) {
                for (int index = 1; index <= 5; index++) {

                    sum += number;
                    number *= count;
                    sum *= sum;

                }


            }



        }
        System.out.printf(" %d", sum);

    }
}
