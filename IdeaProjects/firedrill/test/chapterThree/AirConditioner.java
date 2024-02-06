package chapterThree;

public class AirConditioner {
    private boolean isOn;

    private int temperature = 16;
    public boolean isOn() {
        return isOn;

    }

    public void toggle() {
        isOn = !isOn;
    }

    public int getTemperature() {
        return temperature;

    }

    public void increaseTemperature() {
        boolean temperatureRangeIsWithingRange = temperature >= 16 && temperature < 30;
        if(isOn && temperatureRangeIsWithingRange) temperature++;
    }

    public void decreaseTemperature() {
        boolean temperatureRangeIsWithingRange = temperature > 16 && temperature < 30;
        if(isOn && temperatureRangeIsWithingRange) temperature--;

    }
}
