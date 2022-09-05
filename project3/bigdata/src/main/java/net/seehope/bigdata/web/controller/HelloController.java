package net.seehope.bigdata.web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

/*
* spring springmvc
*
* servlet
*
* */
/**
 * @author Monty
 * @date 2021/11/05 14:52
 **/
//@Controller
//@RequestMapping("/hello")
public class HelloController {

//    @Autowired
    private RedisTemplate<String,String> redisTemplate;

    @ResponseBody
    @RequestMapping("/1")
    public String hello(){
        System.out.println("hello world");
        return "hello world";
    }

    @ResponseBody
    @RequestMapping("/set")
    public String setRedis(){

        redisTemplate.opsForValue().set("string:1", "123456");

        return "success";
    }

    @ResponseBody
    @RequestMapping("/get")
    public String getRedis(){

        String s = redisTemplate.opsForValue().get("string:1");

        return s;
    }
}
