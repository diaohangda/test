package net.seehope.bigdata.ioc.mapper;

import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * @author Monty
 * @date 2021/11/09 11:05
 **/
/*<bean id="userMapper" class="net.seehope.bigdata.ioc.mapper.UserMapper">*/
@Repository
public class UserMapper {

    public void dao(){
        System.out.println("usermapper");
    }
}
