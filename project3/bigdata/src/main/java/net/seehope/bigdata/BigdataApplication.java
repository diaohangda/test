package net.seehope.bigdata;

import net.seehope.bigdata.ioc.web.controller.UserController;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/*
 * IOC/DI
 * AOP
 * */
//@SpringBootApplication
//@ComponentScan(basePackages = {"net.seehope.bigdata",""})
public class BigdataApplication {
    public static void main(String[] args) {
        /*spring 容器用来管理spring组建的创建 生成，以及装配*/
        ApplicationContext cx = new ClassPathXmlApplicationContext("classpath:applicationContext.xml");

        /*cx.getBeansOfType(Servlet.class).keySet().forEach(key -> {
            System.out.println("name:" + key);
        });

        Servlet1 servlet1 = (Servlet1) cx.getBean("servlet1");
        Servlet servlet11 = (Servlet) cx.getBean("servlet1");
        Servlet servlet2 = (Servlet) cx.getBean("servlet2");

        System.out.println(servlet1);
        System.out.println(servlet11);
        System.out.println(servlet2);

        servlet1.service();
        servlet1.getKeys().keySet().forEach(key -> {
            System.out.println("key:" + key + "value:" + servlet1.getKeys().get(key));
        });

        servlet2.service();*/


        /*
         * 控制层用 controller
         * 业务层用service
         * 数据模型层用repository
         * 配置层用configuration
         * 其他层级Component 把当前类注册到容器中
         *
         * controller("XXX")将当前class注册，且在容器中的名字叫做xxx
         *
         * @Autowired 将容器中已经存在的类，注入到当前的变量中
         * 首先按照类型匹配，如果容器中有且只有对应的类型，那么直接注入，如果有两个会报错，
         * 可以通过变量名进一步指定具体匹配的对象，或者通过注解Qualifier区分具体的对象
         *
         * */
        UserController userController = (UserController) cx.getBean("userController");
        userController.hello();
    }
}
