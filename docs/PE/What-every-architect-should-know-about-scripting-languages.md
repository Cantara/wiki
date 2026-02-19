# What every architect should know about scripting languages

## What is a scripting language

### Dictionary definition

"A high-level programming language that is interpreted by another program at runtime rather than compiled by the computer's processor as other programming languages (such as C and C++) are."

Source: Webopedia

### Common traits

- Weak typing
- Good reflection support
- Meta programming
- Strong at text processing
- Closures

### Examples

- Perl
- Python
- Groovy
- Ruby
- ECMAScript (JavaScript/ActionScript)

### Scripting languages are nothing new

- Perl has long been a dominant language in all sizes of architecture
- JavaScript/ActionScript now unavoidable in web applications

### So why the recent hype?

- Moore's law
- More sophisticated
- Rockstar developers

## What can you do with scripting languages?

### Rapid prototyping

- Play with domain model without created lots of boiler plate

### Glue code

- User interfaces
- Cron jobs
- Maintenance scripts
- Online debugging

### ESB Configuration

```java
class StringListTransformer {
  toList(src) {
    return src.toString().tokenize(",");
  }
  
  toString(src) {
    result="";
    src.each { t | result+= "," + t };
    return result.substring(1);
  }
}
```

### Complex business logic

- Zed Shaw - The ACL is dead
```
# 10 ACLs/Person/Container/Action
def rule_supervisor(person, action, role)
       person.departed &&
       allowed_actions.include?(action) &&
       role == :supervisor
end
```
- All rules including bizarre corner cases applied with about 200 lines of Ruby

### Testing

```java
scenario "null is pushed onto empty stack", {
  given "an empty stack",{
    stack = new Stack()
  }

  when "null is pushed", {
    pushnull = {
      stack.push(null)
    }
  }

  then "an exception should be thrown", {
    ensureThrows(RuntimeException){
      pushnull()
    }
  }

  and "then the stack should still be empty", {
    stack.empty.shouldBe true
  }
}

```

## Why use sciprting languages

### Concise

- Fewer lines of code
- Less time spent
- Less bugs (hopefully)
- Easier to read
- Business experts can verify correctness

### Maintenance projects

- Easily interact with existing infrastructure to produce quick wins
- Perfect for adding CRUD interfaces to existing data sources

### You have no choice

- Almost all modern web applications involve scripting

### But beware...

- Probably too slow for performance critical components
- Must be completely covered with automated tests
