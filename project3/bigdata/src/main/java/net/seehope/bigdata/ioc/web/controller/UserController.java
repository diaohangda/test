package net.seehope.bigdata.ioc.web.controller;

import net.seehope.bigdata.ioc.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;

/**
 * @author Monty
 * @date 2021/11/09 11:04
 **/
@Controller
public class UserController {
    @Autowired
    @Qualifier("userServiceImpl")
    private UserService userService;

    public void hello() {
        userService.service();
    }
}
