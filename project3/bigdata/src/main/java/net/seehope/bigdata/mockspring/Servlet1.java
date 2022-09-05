package net.seehope.bigdata.mockspring;

import java.util.HashMap;
import java.util.List;

/**
 * @author Monty
 * @date 2021/11/08 14:48
 **/
public class Servlet1 implements Servlet {

    private int age;
    private String name;
    private List<Integer> ids;
    private HashMap<String, String> keys;
    private int[] ages;
    private HashMap<String, List<Servlet2>> demo;

    public Servlet1() {
    }

    public Servlet1(int age, String name, List<Integer> ids, HashMap<String, String> keys, int[] ages, HashMap<String, List<Servlet2>> demo, Servlet2 servlet2) {
        this.age = age;
        this.name = name;
        this.ids = ids;
        this.keys = keys;
        this.ages = ages;
        this.demo = demo;
        this.servlet2 = servlet2;
    }

    private Servlet2 servlet2;

    public HashMap<String, List<Servlet2>> getDemo() {
        return demo;
    }

    public void setDemo(HashMap<String, List<Servlet2>> demo) {
        this.demo = demo;
    }

    public Servlet2 getServlet2() {
        return servlet2;
    }

    public void setServlet2(Servlet2 servlet2) {
        this.servlet2 = servlet2;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Integer> getIds() {
        return ids;
    }

    public void setIds(List<Integer> ids) {
        this.ids = ids;
    }

    public HashMap<String, String> getKeys() {
        return keys;
    }

    public void setKeys(HashMap<String, String> keys) {
        this.keys = keys;
    }

    public int[] getAges() {
        return ages;
    }

    public void setAges(int[] ages) {
        this.ages = ages;
    }

    @Override
    public void init() {
        System.out.println("init1");
    }

    @Override
    public void service() {
        System.out.println("service1");
    }

    @Override
    public void destory() {
        System.out.println("destory1");
    }
}