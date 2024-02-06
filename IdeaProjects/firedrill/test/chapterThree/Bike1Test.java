package chapterThree;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Bike1Test {

    private Bike1 powerBike;

    @BeforeEach
    public void initializeBike() {
        powerBike = new Bike1();
    }

    @Test
    public void turnOnBike_bikeIsOnTest() {
        assertFalse(powerBike.isOn());

        powerBike.toggle();
        assertTrue(powerBike.isOn());
    }

    @Test
    public void turnBikeOff_bikeIsOffTest() {
        assertFalse(powerBike.isOn());
        powerBike.toggle();
        assertTrue(powerBike.isOn());

        powerBike.toggle();
        assertFalse(powerBike.isOn());
    }


    @Test
    public void testAccelerationGear1() {

        powerBike.toggle();
        powerBike.acceleration();
        for (int count = 1; count <= 15; count++) {
            powerBike.acceleration();
        }

        assertEquals(1, powerBike.getGear());
        assertEquals(16, powerBike.getVelocity());

    }

    @Test
    public void testAccelerationGear2() {


        powerBike.acceleration();
        for (int count = 1; count <= 22; count++) {
            powerBike.acceleration();
        }

        assertEquals(2, powerBike.getGear());
        assertEquals(25, powerBike.getVelocity());


    }

    @Test
    public void testAccelerationGear3() {

        powerBike.toggle();

        for (int count = 1; count <= 28; count++) {
            powerBike.acceleration();
        }

        assertEquals(3, powerBike.getGear());
        assertEquals(37, powerBike.getVelocity());

    }

    @Test
    public void testAccelerationGear4() {

        powerBike.toggle();

        for (int count = 1; count <= 31; count++) {
            powerBike.acceleration();
        }

        assertEquals(4, powerBike.getGear());
        assertEquals(47, powerBike.getVelocity());

    }

    @Test
    public void testDecelerationGear1() {

        powerBike.toggle();
        powerBike.acceleration();
        for (int count = 1; count <= 15; count++) {
            powerBike.acceleration();
        }

        for (int count = 1; count <= 2; count++) {
            powerBike.deceleration();
        }

        assertEquals(1, powerBike.getGear());
        assertEquals(14, powerBike.getVelocity());
    }
    @Test
    public void testDecelerationGear2() {

        powerBike.toggle();

        for (int count = 1; count <= 25; count++) {
            powerBike.acceleration();
        }

        for (int count = 1; count <= 4; count++) {
            powerBike.deceleration();
        }

        assertEquals(2, powerBike.getGear());
        assertEquals(21, powerBike.getVelocity());
    }
    @Test
    public void testDecelerationGear3() {

        powerBike.toggle();

        for (int count = 1; count <= 33; count++) {
            powerBike.acceleration();
        }

        for (int count = 1; count <= 7; count++) {
            powerBike.deceleration();
        }

        assertEquals(3, powerBike.getGear());
        assertEquals(30, powerBike.getVelocity());
    }
    @Test
    public void testDecelerationGear4() {

        powerBike.toggle();
        for (int count = 1; count <= 44; count++) {
            powerBike.acceleration();
        }

        for (int count = 1; count <= 15; count++) {
            powerBike.deceleration();
        }

        assertEquals(4, powerBike.getGear());
        assertEquals(39, powerBike.getVelocity());
    }



}







        //     powerBike.setGear(2);
        //  powerBike.deceleration();
        //         assertEquals(26, powerBike.getVelocity());
        //    powerBike.deceleration();
        //        assertEquals(22, powerBike.getVelocity());


        //     powerBike.setGear(3);
        //     powerBike.acceleration();
        //        assertEquals(38, powerBike.getVelocity());
        //    powerBike.deceleration();
        //        assertEquals(32, powerBike.getVelocity());


        //     powerBike.setGear(4);
        //     powerBike.acceleration();
        //        assertEquals(48, powerBike.getVelocity());
        //     powerBike.deceleration();
        //        assertEquals(40, powerBike.getVelocity());
        //  }






