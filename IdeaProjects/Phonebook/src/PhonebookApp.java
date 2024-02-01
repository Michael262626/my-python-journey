import java.util.Scanner;
import java.util.ArrayList;
public class PhonebookApp {
    private static String name;
    private static String number;


    public static void setName(String name){
        PhonebookApp.name = name;
    }
    public static String getName(){
        return name;
    }
    public static void setNumber(String number){
        PhonebookApp.number = number;
    }
    public static String getNumber(){
        return number;
    }

    public static void main(String[] args) {
        ArrayList<String> names =  new ArrayList<>();
        ArrayList<String> numbers = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        System.out.println("=======>>☎️📞 PHONE BOOK APP☎️📞 <<========");
        System.out.println(">>>>What would you like to do 😏?<<<<");
        System.out.println("1. Create a new phoneNumber ");
        System.out.println("2. Search contact number ");
        System.out.println("3. Delete contact number");
        System.out.println("4. Exit...");
        System.out.println("                               ^ ");
        System.out.println("Enter any of the options above | ");
        int choice = scanner.nextInt();

        while(choice == 1){
                System.out.println("Enter the name and the contact created by space :)");
                String nameEntered = scanner.next();
                String numberEntered = scanner.next();
                names.add(nameEntered);
                numbers.add(numberEntered);
                System.out.println("Saving.....");
                System.out.println("Contact saved successfully!!✔️");
                break;


        }
        System.out.println("Do you want to explore more? -> enter yes/no");
        String options = scanner.next();
        if(options.equalsIgnoreCase("no")){
            System.out.println("Exiting.....🚶🚶🚶🚶");

        }
        else{
            System.out.println("Enter any of the options above | ");
            choice = scanner.nextInt();
            while(choice == 2){
                if (!options.equalsIgnoreCase("yes") && !options.equalsIgnoreCase("no")) {
                    System.out.println("Do you want to explore more? -> enter yes/no");
                    options = scanner.next();


                }else{

                        System.out.println("Enter the name to be searched");
                        String userName = scanner.next();
                        int index = names.indexOf(userName);
                        if(index != -1){
                            System.out.println("Contact found");
                            System.out.printf("\nName: %s", names.get(index));
                            System.out.printf("\nNumber: %s", numbers.get(index));
                        }
                        else{
                            System.out.println("No contact found");
                        }
                    break;


                }

            }

        }


        if(options.equalsIgnoreCase("no")){
            System.out.println("Exiting.....🚶🚶🚶🚶");
        }
        else {
            System.out.println("Enter any of the options above | ");
            choice = scanner.nextInt();

            while(choice==3){


                    System.out.println("Enter the name of the contact you want to be deleted");
                    String userName = scanner.next();
                    int deleteName = names.indexOf(userName);
                    if (deleteName != -1) {
                        names.remove(deleteName);
                        numbers.remove(deleteName);
                        System.out.println("Contact deleted successfully");
                        break;

                    } else {
                        System.out.println("Contact not found");
                        break;

                    }



            }
        }

        while(choice==4){


                    System.out.print("Wait for some seconds\nExiting app....🚶🚶🚶🚶1");
                    break;


        }


    }
}