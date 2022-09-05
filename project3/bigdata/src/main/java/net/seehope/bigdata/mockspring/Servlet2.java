package net.seehope.bigdata.mockspring;

/**
 * @author Monty
 * @date 2021/11/08 14:48
 **/
public class Servlet2 implements Servlet{
    @Override
    public void init() {
        System.out.println("init2");
    }

    @Override
    public void service() {
        System.out.println("service2");
    }

    @Override
    public void destory() {
        System.out.println("destory2");
    }
}
