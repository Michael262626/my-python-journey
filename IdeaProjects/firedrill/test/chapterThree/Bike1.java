package chapterThree;

public class Bike1 {

    private boolean isOn;

    private int velocity;

    private int gear;

    public boolean isOn() {
        return isOn;
    }

    public void toggle() {
        isOn = !isOn;
    }

    public int acceleration() {
        if (velocity <= 20){ gear = 1;
        velocity++;}
        else if (velocity >= 21 && velocity <= 30){ gear = 2;
        velocity += 2;}
        else if (velocity >= 31 && velocity <= 40){ gear = 3;
        velocity += 3;}
        else if(velocity >= 41) { gear = 4;
        velocity += 4;}

        return velocity;
    }
    public int deceleration(){
        if (velocity >= 0 && velocity <= 20){ gear = 1;
        velocity--;}
        else if (velocity >= 21 && velocity <= 30){ gear = 2;
        velocity -= 2;}
        else if (velocity >= 31 && velocity <= 40){ gear = 3;
        velocity -= 3;}
        else if (velocity >= 41){ gear = 4;
        velocity -= 4;}
        return velocity;
    }
    public int getGear(){
        return gear;
    }
    public int getVelocity(){
        return velocity;
    }

}




