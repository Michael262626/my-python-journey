import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
class PhonebookAppTest {

@Test
    void getName() {
       PhonebookApp phonebookapp = new PhonebookApp();
       PhonebookApp.setName("Michael");
       assertEquals("Michael",  phonebookapp.getName());
    }



    @Test
    void getNumber() {
        PhonebookApp phonebookapp = new PhonebookApp();
        PhonebookApp.setNumber("07066993421");
        assertEquals("07066993421",  phonebookapp.getNumber());
    }

    @Test
    void main() {
        ArrayList<String> names = new ArrayList<>();
        names.add("michael");
        names.add("07066993421");


        names.add("michael");
        names.add("07066993421");


        assertEquals(4, names.size());
        assertTrue(names.contains("michael"));
        assertTrue(names.contains("07066993421"));
    }
    void removeFrom() {

        ArrayList<String> names = new ArrayList<>();
        names.add("michael");
        names.add("07066993421");


        names.remove("michael");
        names.remove("07066993421");

        assertEquals(1, names.size());
        assertFalse(names.contains("michael"));
        assertTrue(names.contains("07066993421"));
    }

}




