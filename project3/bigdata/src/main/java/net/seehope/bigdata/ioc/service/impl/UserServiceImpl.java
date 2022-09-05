package net.seehope.bigdata.ioc.service.impl;

import net.seehope.bigdata.ioc.mapper.UserMapper;
import net.seehope.bigdata.ioc.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * @author Monty
 * @date 2021/11/09 11:04
 **/
@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserMapper userMapper;

    @Override
    public void service() {
        userMapper.dao();
    }
}
