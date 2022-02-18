package com.example.demo.dao;

import com.example.demo.model.Person;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.regex.*;
import java.util.Optional;
import java.util.UUID;
@Repository("postgres")
public class PersonDataAccessService implements PersonDao{

    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public PersonDataAccessService(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }


    @Override
    public int insertPerson(UUID id, Person person) {
        String pattern = "^[A-Za-z0-9]{1,50}+$";
        boolean isMatch = Pattern.matches(pattern, person.getName());
        System.out.println(isMatch);
        if (!(isMatch)){
            System.out.println("asdf");
            return 1;
        }else {
            String sql = "INSERT INTO person (id, name) VALUES (\'" + id + "\', \'" + person.getName() + "\');";
            System.out.println(sql);
            jdbcTemplate.execute(sql);
            return 0;
        }
    }

    @Override
    public List<Person> selectAllPeople() {
        final String sql = "SELECT id, name FROM person";
        List<Person> people = jdbcTemplate.query(sql, (resultSet, i) -> {
            UUID id = UUID.fromString(resultSet.getString("id"));
            String name = resultSet.getString("name");
            return new Person(id, name);
        });
        return people;
    }

    @Override
    public int deletePersonById(UUID id) {
        return 0;
    }

    @Override
    public int updatePersonById(UUID id, Person person) {
        return 0;
    }

    @Override
    public Optional<Person> selectPersonById(UUID id) {
        String sql = "SELECT id, \"name\" FROM \"person\" WHERE id=\'" + id + "\';";
        Person p = jdbcTemplate.query(sql, new );
        System.out.println(Optional.of(p));
        return Optional.of(p);
    }
}
