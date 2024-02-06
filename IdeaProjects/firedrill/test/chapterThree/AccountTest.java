package chapterThree;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AccountTest {
    @Test
    public void depositNegativeBalance_balanceRemainsUnchangedTest(){
        Account michaelAccount = new Account();
        assertEquals(0, michaelAccount.getBalance());

        michaelAccount.deposit(-50_000);
        assertEquals(0, michaelAccount.getBalance());
    }
    @Test
    public void depositPositiveAmount_balanceIncreasesTest(){
        Account michaelAccount = new Account();
        assertEquals(0, michaelAccount.getBalance());

        michaelAccount.deposit(2_000);
        assertEquals(2_000, michaelAccount.getBalance());
    }
    @Test
    public void depositPositiveAmountTwice_balanceIncreasesTest(){
        Account michaelAccount = new Account();
        assertEquals(0, michaelAccount.getBalance());

        michaelAccount.deposit(2_000);
        michaelAccount.deposit(4_000);
        assertEquals(6_000, michaelAccount.getBalance());

    }
    @Test
    public void withdrawAmountHigherThanTheBalanceTest(){
        Account michaelAccount = new Account();
        assertEquals(0, michaelAccount.getBalance());

        michaelAccount.withdraw(20_000);
        assertEquals(0,  michaelAccount.getBalance());

    }

    @Test
    public void withdrawAmountLesserThanTheBalanceTest(){
        Account michaelAccount = new Account();
        assertEquals(0, michaelAccount.getBalance());
        michaelAccount.deposit(1_200);


        michaelAccount.withdraw(1000);
        assertEquals(200, michaelAccount.getBalance());
    }
    @Test
    public void withdrawAmountThanTheBalanceTest(){
        Account michaelAccount = new Account();
        assertEquals(0, michaelAccount.getBalance());
        michaelAccount.deposit(200);

        michaelAccount.withdraw(50_000);
        assertEquals(200, michaelAccount.getBalance());


    }
}
