import static org.junit.jupiter.api.Assertions.*;

class MenstrualRevolutionTest {

    @org.junit.jupiter.api.Test
    void testSetName() {
        MenstrualRevolution menstrualRevolution = new MenstrualRevolution();
        MenstrualRevolution.setName("Michael");
        assertEquals("Michael", menstrualRevolution.getName());
    }

    @org.junit.jupiter.api.Test
    void testGetName() {
    }

    @org.junit.jupiter.api.Test
    void testSetGender() {
        MenstrualRevolution menstrualRevolution = new MenstrualRevolution();
        MenstrualRevolution.setGender("female");
        assertEquals("female", menstrualRevolution.getGender());
    }

    @org.junit.jupiter.api.Test
    void testSetAge() {
        MenstrualRevolution menstrualRevolution = new MenstrualRevolution();
        MenstrualRevolution.setAge(14);
        assertEquals(14, menstrualRevolution.getAge());
    }

    @org.junit.jupiter.api.Test
    void testGetAge() {
    }

    @org.junit.jupiter.api.Test
    void testSetLastDay() {
        MenstrualRevolution menstrualRevolution = new MenstrualRevolution();
        MenstrualRevolution.setLastDay(4);
        assertEquals(4,  menstrualRevolution.getLastDay());
    }

    @org.junit.jupiter.api.Test
    void testGetLastDay() {
    }

    @org.junit.jupiter.api.Test
    void testSetLength() {
        MenstrualRevolution menstrualRevolution = new MenstrualRevolution();
        MenstrualRevolution.setLength(28);
        assertEquals(28,  menstrualRevolution.getLength());
    }

    @org.junit.jupiter.api.Test
    void testGetLength() {
    }

    @org.junit.jupiter.api.Test
    void testGetOvulationPeriod() {

    }

    @org.junit.jupiter.api.Test
    void testGetMenstrualFlowingPeriod() {
    }

    @org.junit.jupiter.api.Test
    void testGetMenstrualPeriod() {
    }

    @org.junit.jupiter.api.Test
    void testGetFreePeriod() {
    }

    @org.junit.jupiter.api.Test
    void testGetFreePeriod2() {
    }

    @org.junit.jupiter.api.Test
    void testMain() {
    }
}