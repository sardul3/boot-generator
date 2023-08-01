// templates/Main.java
package {{ package_name }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{ main_class }} {
    public static void main(String[] args) {
        SpringApplication.run({{main_class}}.class, args);
    }
}
