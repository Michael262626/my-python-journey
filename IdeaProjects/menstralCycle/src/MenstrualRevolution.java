import java.util.Scanner;
public class MenstrualRevolution{
    private static String name;
    private static String gender;
    private static int age;
    private static int lastDay;
    private static int length;

    public MenstrualRevolution(){
        MenstrualRevolution.name = name;
        MenstrualRevolution.gender = gender;
        MenstrualRevolution.age = age;
        MenstrualRevolution.lastDay = lastDay;
        MenstrualRevolution.length = length;
    }
    public static void setName(String name){
        MenstrualRevolution.name = name;
    }
    public static String getName(){
        return name;
    }
    public static void setGender(String gender){
        MenstrualRevolution.gender = gender;
    }
    public static String getGender(){
        return gender;
    }
    public static void setAge(int age){
        MenstrualRevolution.age = age;
    }
    public static int getAge(){
        return age;
    }


    public static void setLastDay(int lastDay){
        MenstrualRevolution.lastDay = lastDay;
    }
    public static int getLastDay(){
        return lastDay;
    }
    public static void setLength(int length){
        MenstrualRevolution.length = length;
    }
    public static int getLength(){
        return length;
    }


    public static int getOvulationPeriod(){
       int ovulationCheck = (getLastDay() + 7) + 6;
       return ovulationCheck;
    }
    public static int getMenstrualFlowingPeriod(){
        int mensturalCheck =  (getLength() - getLastDay()) + 7 ;
        return  mensturalCheck ;
    }
    public static int getMenstrualPeriod(){
        int menstrualCheck2 = (28 - getLastDay()) + 7;
        return menstrualCheck2;
    }
    public static int getFreePeriod(){
        int freePeriod = (getLength() - getLastDay()) + 12;
        return freePeriod;
    }
    public static int getFreePeriod2(){
        int freePeriod2 = (28 - getLastDay()) + 12;
        return freePeriod2;
    }



    public static void main(String... args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("To know about this app enter yes proceed?");
        String response = scanner.next();

        do {
            if(!response.equalsIgnoreCase("yes")){
                System.out.println("To know about this app enter yes or no to proceed?");
                response = scanner.next();
            }
            else{

                System.out.println("This app is to give you a brief knowledge about menstral cycle and hygiene. And also  lessens the myths and confusion around it.\nMenstrual Cycle\n" +
                        "A menstrual cycle begins when you get your period or menstruate. This is when you shed the lining of your uterus. This cycle is part of your reproductive system and prepares your body for a possible pregnancy. A typical cycle lasts between 24 and 38 days.\nMenstruation is the monthly shedding of the lining of your uterus. Menstruation is also known by the terms menses, menstrual period, menstrual cycle or period. Menstrual blood — which is partly blood and partly tissue from the inside of your uterus — flows from your uterus through your cervix and out of your body through your vagina.\nMenstruation is driven by hormones. Hormones are chemical messengers in your body. Your pituitary gland (in your brain) and your ovaries (part of your reproductive system) make and release certain hormones at certain times during your menstrual cycle.\n" +
                        "\n" +
                        "These hormones cause the lining of your uterus to thicken. This happens so that if a pregnancy would occur, an egg can implant into your uterine lining. Hormones also cause your ovaries to release an egg (ovulation). The egg moves down your fallopian tubes, where it waits for sperm. If a sperm doesn’t fertilize that egg, pregnancy doesn’t occur. The lining of your uterus breaks down and sheds. This is your period.");
                break;
            }
        }while(response.equalsIgnoreCase("yes"));

        System.out.println("Enter continue");
        String click = scanner.next();
        if (!click.equalsIgnoreCase("continue")) {
            System.out.println("Enter continue");
            click = scanner.next();
        }
        do {

            System.out.println("Kindly enter your name!");
            String userName = scanner.next();
            setName(userName);

            System.out.println("Enter gender type!");
            String gender = scanner.next();
            if (!gender.equalsIgnoreCase("female")) {
                System.out.println("This app is restricted only female are allowed to use this app.");
                break;
            } else {
                System.out.println("Enter your age: ");
                int userAge = scanner.nextInt();
                setAge(userAge);
                if (userAge <= 8) {
                    System.out.println("You have to be  above 8 to experience your period");
                    break;
                } else if (age >= 51) {
                    System.out.println("You have reached the stage of menopause. \nYou must be in the range of 8-51 to use this app thank you :)");
                    break;
                } else if (userAge >= 8 || userAge <= 51) {
                    System.out.println("Is your menstrual cycle regular enter yes or no");
                    String choose = scanner.next();
                    if(choose.equalsIgnoreCase("yes")) {
                        System.out.println("Enter the length of your cycle");
                        int userLength = scanner.nextInt();
                        setLength(userLength);
                        System.out.println("Enter the date it occurred last?");
                        int lastDay = scanner.nextInt();
                        setLastDay(lastDay);
                        System.out.printf("\n%s Your next period will occur in the next %d days\n", getName(), getMenstrualFlowingPeriod());
                        System.out.printf("\nYour ovulation period will be in the next %d days\n", getOvulationPeriod());
                        System.out.printf("\nYour normal day will occur in the next %d days\n", getFreePeriod());
                    }
                    else{
                        System.out.println("When did your last period start?");
                        int lastDay = scanner.nextInt();
                        setLastDay(lastDay);
                        System.out.printf("\n%s Your next period will occur in the next %d days\n", getName(),  getMenstrualPeriod());
                        System.out.printf("\nYou are likely to see your ovulation period the next %d\n", getOvulationPeriod());
                        System.out.printf("Your normal day will occur in the next %d", getFreePeriod2());
                    }
                }

                String choice = " ";

                do {

                    if (!choice.equalsIgnoreCase("yes")) {
                        System.out.println("Do you feel any pains or you are not comfortable? enter yes or no ");
                        choice = scanner.next();
                    } else {
                        System.out.println("To ease your menstrual cramps, your health care provider might recommend: Pain relievers. Over-the-counter pain relievers, such as ibuprofen (Advil, Motrin IB, others) or naproxen sodium (Aleve), at regular doses starting the day before you expect your period to begin can help control the pain of cramps.\n" +
                                "\n" +
                                "Or local recommendations\n" + "Several herbal remedies, such as ginger, fennel, Chinese herbs, cinnamon, Pycnogenol, and peppermint, have been studied for treating dysmenorrhea (menstrual cramps). Despite promising results, the quality of the studies is generally poor and there is no clear proof that any of the herbal remedies help");
                        System.out.println("Thanks for your services\nFor more information please contact any physician, gynecologist, or a women's health clinic for assistance.");
                        break;
                    }
                } while (choice.equalsIgnoreCase("yes"));

                do {
                    System.out.println("Thanks for your services\nFor more information please contact any physician, gynecologist, or a women's health clinic for assistance.");
                    break;
                } while (choice.equalsIgnoreCase("no"));
            }
            break;
        }
        while(click.equalsIgnoreCase("continue"));



    }
}